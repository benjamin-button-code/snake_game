import sys
import pygame


class Game:
    def __init__(self):
        # Scales
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

    def event_loop(self):
        pass

    def show_score(self, pos=1):
        pass

    def game_over(self):
        pass


class Snake:
    def __init__(self):
        pass


class Food:
    def __init__(self):
        pass