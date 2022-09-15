import pygame
import numpy as np
from random import randint

RES = WIDTH, HEIGHT = 1600, 900
TILE = 5
W, H = WIDTH // TILE, HEIGHT // 2

pygame.init()
surface = pygame.display.set_mode(RES)

next_field = np.array([[0 for i in range(W)] for j in range(H)])


def make_noise_grid(density):
    res = []
    for i in range(W):
        for j in range(H):
            random = randint(1, 100)
            if density > random:
                res.append((i, j))
    return res


noise_grid = make_noise_grid(25)

while True:
    surface.fill(pygame.Color('black'))
    [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

    [pygame.draw.rect(surface, pygame.Color('darkorange'),
                      (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1)) for x, y in noise_grid]


    pygame.display.flip()
