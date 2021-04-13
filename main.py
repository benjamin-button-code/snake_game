import sys
import random

import pygame
from pygame.math import Vector2


pygame.init()

# Settings / Constatns
CELL_SIZE = 40
CELL_NUMBER = 18
WIDTH = CELL_NUMBER * CELL_SIZE + 10
HEIGHT = WIDTH
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Time
CLOCK = pygame.time.Clock()
FPS = 5

# Directions
RIGTH = Vector2(1, 0)
LEFT = Vector2(-1, 0)
DOWN = Vector2(0, 1)
UP = Vector2(0, -1)

GAME_LOOP = True

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 9), Vector2(6, 9), Vector2(5, 9)]
        self.direction = RIGTH

    def draw(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(SCREEN, (0, 255, 0), block_rect)

    def movement(self):
        self.body.pop()
        self.body.insert(0, self.body[0] + self.direction)
        


class Food:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw(self):
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        food_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE - 5, CELL_SIZE - 5)
        pygame.draw.rect(SCREEN, pygame.Color('red'), food_rect)

class Main:
    pass


snake = Snake()
food = Food()
main_game = Main()

while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == ord('d')) and snake.direction.x != -1:
                snake.direction = RIGTH
                break
            if (event.key == pygame.K_LEFT or event.key == ord('a')) and snake.direction.x != 1:
                snake.direction = LEFT
                break
            if (event.key == pygame.K_UP or event.key == ord('w')) and snake.direction.y != 1:
                snake.direction = UP
                break
            if (event.key == pygame.K_DOWN or event.key == ord('s')) and snake.direction.y != -1:
                snake.direction = DOWN
                break
            if event.key == pygame.K_ESCAPE:
                GAME_LOOP = False
    snake.movement()
    
    # Draw
    SCREEN.fill((175, 215, 70))
    food.draw()
    snake.draw()
    pygame.display.update()
    CLOCK.tick(FPS)
