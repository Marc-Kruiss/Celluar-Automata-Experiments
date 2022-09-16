import pygame
import numpy as np
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1600, 900
TILE = 5
W, H = WIDTH // TILE, HEIGHT // 2

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = -1


def make_noise_grid(density):
    field = np.array([[0 for i in range(W)] for j in range(H)])
    res = []
    for i in range(W):
        for j in range(H):
            random = randint(1, 100)
            if density > random:
                res.append((i, j))
                field[j, i] = 1
    return field, res


def is_within_map_bounds(localX, localY):
    return 0 <= localX < W and 0 <= localY < H


def apply_cellar_automaton(grid, iterationCount):
    res = []
    for i in range(iterationCount):
        next_grid = deepcopy(grid)
        for globalY in range(1, H):
            for globalX in range(1, W):
                neighbor_wall_count = 0
                for localY in range(globalY - 1, globalY + 2):
                    for localX in range(globalX - 1, globalX + 2):
                        if is_within_map_bounds(localX, localY):
                            if not (localY == globalY and localX == globalX):
                                if grid[localY][localX] == 1:
                                    neighbor_wall_count += 1
                        else:
                            neighbor_wall_count += 1

                if neighbor_wall_count > 4:
                    next_grid[globalY][globalX] = 1
                    res.append((globalX, globalY))
                else:
                    next_grid[globalY][globalX] = 0
    return next_grid, res


if __name__ == '__main__':
    grid, res = make_noise_grid(55)
    ITERAITONS = 5
    iterationCount = 0
    while True:

        surface.fill(pygame.Color('black'))
        [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

        # Draw rects
        # [pygame.draw.rect(surface, pygame.Color('darkorange'),
        #                 (x * TILE + 1, y * TILE + 1, TILE)) for x, y in res]

        # Draw circles
        [pygame.draw.circle(surface, pygame.Color('darkorange'),
                            (x * TILE + 1, y * TILE + 1), TILE) for x, y in res]

        if iterationCount <= ITERAITONS:
            grid, res = apply_cellar_automaton(grid, 1)

        iterationCount += 1

        print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS)
