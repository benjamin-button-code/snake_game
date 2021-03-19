import sys
import time
import random
import pygame


class Game:
    def __init__(self):
        # Display
        self.WIDTH = 720
        self.HEIGHT = 460
        self.display_surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Colors
        self.RED = pygame.Color(255, 0, 0)
        self.GREEN = pygame.Color(0, 255, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.BLACK = pygame.Color(0, 0, 0)

        # Time
        self.FPS = 30
        self.FPS_CLOCK = pygame.time.Clock()

        # Score
        self.score = 0

    @staticmethod
    def init_and_check_for_errors():
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            pygame.display.set_caption("Snake Game")

    def update_screen(self):
        pygame.display.update()
        self.FPS_CLOCK.tick(self.FPS)

    def event_loop(self, change_to):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return change_to

    def show_score(self, pos=1):
        ss_font = pygame.font.SysFont("monaco", 24)
        ss_surface = pygame.render(f"Score: {self.score}", True, self.BLACK)
        ss_rect = ss_surface.get_rect()
        if pos == 1:
            ss_rect.midtop = (80, 10)
        else:
            ss_rect.midtop = (360, 120)
        self.display_surface.blit(ss_surface, ss_rect)

    def game_over(self):
        go_font = pygame.font.SysFont("monaco", 72)
        go_surface = pygame.render("Game over", True, self.RED)
        go_rect = go_surface.get_rect()
        self.display_surface.blit(go_surface, go_rect)
        self.show_score(0)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake:
    def __init__(self, snake_color):
        self.snake_color = snake_color
        self.snake_head_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.change_to = self.direction

    def validate_direction_and_change(self):
        if any((self.change_to == "RIGHT" and not self.direction == "LEFT",
                self.change_to == "LEFT" and not self.direction == "RIGHT",
                self.change_to == "UP" and not self.direction == "DOWN",
                self.change_to == "DOWN" and not self.direction == "UP")):
            self.direction = self.change_to

    def change_head_position(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def snake_body_mechanism(self, score, food_pos, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head_pos))
        if (self.snake_head_pos[0] == food_pos[0] and
                self.snake_head_pos[1] == food_pos[1]):
            food_pos = [random.randrange(1, screen_width / 10) * 10,
                        random.randrange(1, screen_height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def check_for_boundaries(self, game_over, screen_width, screen_height):
        if any((self.snake_head_pos[0] > screen_width - 10
                or self.snake_head_pos[0] < 0,
                self.snake_head_pos[1] > screen_height - 10
                or self.snake_head_pos[1] < 0)):
            game_over()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head_pos[0] and
                    block[1] == self.snake_head_pos[1]):
                game_over()


class Food:
    def __init__(self, food_color, screen_width, screen_height):
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]

    def draw_food(self, display_surface):
        pygame.draw.rect(display_surface, self.food_color,
                         pygame.Rect(self.food_pos[0], self.food_pos[1],
                                     self.food_size_x, self.food_size_y))
