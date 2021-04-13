import sys
import random

import pygame


pygame.init()

# Settings / Constatns
CELL_SIZE = 40
CELL_NUMBER = 18
WIDTH = CELL_NUMBER * CELL_SIZE
HEIGHT = WIDTH
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 30
GAME_LOOP = True

while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                pass
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                pass
            elif event.key == pygame.K_UP or event.key == ord('w'):
                pass
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                pass
            elif event.key == pygame.K_ESCAPE:
                pass
    
    pygame.display.update()
    CLOCK.tick(FPS)
