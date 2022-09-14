import pygame
from random import randint
from copy import deepcopy
import numpy as np
from numba import njit

RES = WIDTH, HEIGHT = 1600, 900
TILE = 2
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 0
RATIO = 0

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = np.array([[0 for i in range(W)] for j in range(H)])
# default config
current_field_default = np.array([[randint(0, 1) for i in range(W)] for j in range(H)])
# cross config
current_field_cross = np.array([[0 for i in range(W)] for j in range(H)])
for i in range(H):
    current_field_cross[i][i + (W - H) // 2] = 1
    current_field_cross[H - i - 1][i + (W - H) // 2] = 1


selected_current_field = current_field_cross


@njit(fastmath=True)
def check_cells(current_field, next_field):
    res = []
    for x in range(RATIO, W - RATIO):
        for y in range(RATIO, H - RATIO):
            count = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j % H][i % W] == 1:
                        count += 1

            if current_field[y, x] == 1:
                count -= 1
                if count == 2 or count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0

    return next_field, res


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw life
    next_field, res = check_cells(selected_current_field, next_field)
    [pygame.draw.rect(surface, pygame.Color('darkorange'),
                      (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1)) for x, y in res]

    selected_current_field = deepcopy(next_field)

    print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)
