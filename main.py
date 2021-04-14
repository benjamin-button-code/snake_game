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

# Load images of snake
snake_head_down = pygame.image.load("Images/snake_head_down.png").convert_alpha()
snake_head_up = pygame.image.load("Images/snake_head_up.png").convert_alpha()
snake_head_right = pygame.image.load("Images/snake_head_right.png").convert_alpha()
snake_head_left = pygame.image.load("Images/snake_head_left.png").convert_alpha()

snake_tail_up = pygame.image.load("Images/snake_tail_up.png").convert_alpha()
snake_tail_down = pygame.image.load("Images/snake_tail_down.png").convert_alpha()
snake_tail_right = pygame.image.load("Images/snake_tail_right.png").convert_alpha()
snake_tail_left = pygame.image.load("Images/snake_tail_left.png").convert_alpha()

snake_body_vertical = pygame.image.load("Images/snake_body_vertical.png").convert_alpha()
snake_body_horizontal = pygame.image.load("Images/snake_body_horizontal.png").convert_alpha()
snake_body_br = pygame.image.load("Images/snake_body_br.png").convert_alpha()
snake_body_bl = pygame.image.load("Images/snake_body_bl.png").convert_alpha()
snake_body_lt = pygame.image.load("Images/snake_body_lt.png").convert_alpha()
snake_body_rt = pygame.image.load("Images/snake_body_rt.png").convert_alpha()

SPEEDUP = True
GAME_FONT = pygame.font.Font("fonts/Neucha-Regular.ttf", 25)
GAME_LOOP = True

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 9), Vector2(6, 9), Vector2(5, 9)]
        self.direction = RIGTH

        # Images
        self.head = snake_head_right
        self.tail = snake_tail_right

    def movement(self, sneck=False):
        self.body.insert(0, self.body[0] + self.direction)
        if not sneck:
            self.body.pop()
        
    def snake_head_update(self):
        if self.direction == RIGTH:
            self.head = snake_head_right
        elif self.direction == LEFT:
            self.head = snake_head_left
        elif self.direction == UP:
            self.head = snake_head_up
        else:
            self.head = snake_head_down
    
    def snake_tail_update(self):
        relation_tail_body = self.body[-1] - self.body[-2]
        if relation_tail_body == RIGTH:
            self.tail = snake_tail_right
        elif relation_tail_body == LEFT:
            self.tail = snake_tail_left
        elif relation_tail_body == UP:
            self.tail = snake_tail_up
        else:
            self.tail = snake_tail_down

    def draw(self):
        self.snake_head_update()
        self.snake_tail_update()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE - 2, CELL_SIZE - 2)

            if index == 0:
                SCREEN.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                SCREEN.blit(self.tail, block_rect)
            else:
                previos_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previos_block.x == next_block.x:
                    SCREEN.blit(snake_body_vertical, block_rect)
                elif previos_block.y == next_block.y:
                    SCREEN.blit(snake_body_horizontal, block_rect)
                else:
                    if next_block.x == 1 and previos_block.y == 1 or \
                        next_block.y == 1 and previos_block.x == 1:
                        SCREEN.blit(snake_body_br, block_rect)
                    elif next_block.x == -1 and previos_block.y == 1 or \
                        next_block.y == 1 and previos_block.x == -1:
                        SCREEN.blit(snake_body_bl, block_rect)
                    elif next_block.x == 1 and previos_block.y == -1 or \
                        next_block.y == -1 and previos_block.x == 1:
                        SCREEN.blit(snake_body_rt, block_rect)
                    else:
                        SCREEN.blit(snake_body_lt, block_rect)


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
    
    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(CELL_NUMBER):
            for col in range(CELL_NUMBER):
                grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if col % 2 == 0 and row % 2 == 0:
                    pygame.draw.rect(SCREEN, grass_color, grass_rect)
                elif col % 2 != 0 and row % 2 != 0:
                    pygame.draw.rect(SCREEN, grass_color, grass_rect)

    def draw_elements(self):
        self.draw_grass()
        self.food.draw()
        self.snake.draw()
        self.show_score()
    
    def show_score(self):
        score_text = str(self.score)
        score_surface = GAME_FONT.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_NUMBER * CELL_SIZE - 60)
        score_y = int(CELL_NUMBER * CELL_SIZE - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.food.apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, 
                            apple_rect.width + score_rect.width + 10, apple_rect.height)

        pygame.draw.rect(SCREEN, (167, 209, 51), bg_rect)
        SCREEN.blit(score_surface, score_rect)
        SCREEN.blit(self.food.apple, apple_rect)
        pygame.draw.rect(SCREEN, (56, 74, 12), bg_rect, 2)

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.sneck = False

    def game_over(self):
        done = True
        while done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                        done = False
                    elif event.type == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        done = False
        return
    
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
        FPS += 2
        SPEEDUP = False
    elif game.score % 5 != 0:
        SPEEDUP = True

    # Draw
    SCREEN.fill((175, 215, 70))
    game.update()
    pygame.display.update()
    CLOCK.tick(FPS)
