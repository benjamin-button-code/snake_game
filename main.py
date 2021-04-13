import sys
import random

import pygame
from pygame.math import Vector2


pygame.font.init()
pygame.init()

# Settings / Constatns
CELL_SIZE = 40
CELL_NUMBER = 18
WIDTH = CELL_NUMBER * CELL_SIZE
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

SPEEDUP = True
GAME_FONT = pygame.font.Font("fonts/Neucha-Regular.ttf", 25)
GAME_LOOP = True

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 9), Vector2(6, 9), Vector2(5, 9)]
        self.direction = RIGTH

    def movement(self, sneck=False):
        self.body.insert(0, self.body[0] + self.direction)
        if not sneck:
            self.body.pop()
        
    def draw(self):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(SCREEN, (0, 255, 0), block_rect)


class Food:
    def __init__(self):
        self.apple = pygame.image.load("Images/apple.png").convert_alpha()
        self.apple = pygame.transform.scale(self.apple, (40, 40))

        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw(self):
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        food_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE - 5, CELL_SIZE - 5)

        SCREEN.blit(self.apple, food_rect)
        # pygame.draw.rect(SCREEN, pygame.Color('red'), food_rect)
    
    def update_position(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
 

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

        self.score = 0
        # Is snake eat food?
        self.sneck = False
    
    def collision_with_wall(self):
        if not 0 <= self.snake.body[0].x < CELL_NUMBER \
            or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
        
    def collision_with_himself(self):
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def collision_with_food(self):
        if self.food.pos == self.snake.body[0]:
            self.score += 1
            self.food.update_position()
            self.sneck = True
        else:
            self.sneck = False

        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.update_position()
    
    def check_collision(self):
        self.collision_with_food()
        self.collision_with_wall()
        self.collision_with_himself()

    def draw_elements(self):
        self.food.draw()
        self.snake.draw()
        self.show_score()
    
    def show_score(self):
        score_text = str(self.score)
        score_surface = GAME_FONT.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_NUMBER * CELL_SIZE - 60)
        score_y = int(CELL_NUMBER * CELL_SIZE - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        SCREEN.blit(score_surface, score_rect)

    def game_over(self):
        pygame.quit()
        sys.exit()
    
    def update(self):
        self.snake.movement(self.sneck)
        self.check_collision()
        self.draw_elements()


game = Game()

while GAME_LOOP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_LOOP = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == ord('d')) and game.snake.direction.x != -1:
                game.snake.direction = RIGTH
                break
            if (event.key == pygame.K_LEFT or event.key == ord('a')) and game.snake.direction.x != 1:
                game.snake.direction = LEFT
                break
            if (event.key == pygame.K_UP or event.key == ord('w')) and game.snake.direction.y != 1:
                game.snake.direction = UP
                break
            if (event.key == pygame.K_DOWN or event.key == ord('s')) and game.snake.direction.y != -1:
                game.snake.direction = DOWN
                break
            if event.key == pygame.K_ESCAPE:
                GAME_LOOP = False


    # Speedup
    if game.score % 5 == 0 and game.score != 0 and SPEEDUP:
        FPS += 1
        SPEEDUP = False
    elif game.score % 5 != 0:
        SPEEDUP = True

    # Draw
    SCREEN.fill((175, 215, 70))
    game.update()
    pygame.display.update()
    CLOCK.tick(FPS)
