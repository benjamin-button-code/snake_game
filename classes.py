import sys
import time
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

    def event_loop(self, direction):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    direction = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    direction = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    direction = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    direction = "DOWN"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return direction

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
        go_surface = pygame.render("Game over", True, self.red)
        go_rect = go_surface.get_rect()
        self.display_surface.blit(go_surface, go_rect)
        self.show_score(0)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        sys.exit()


class Snake:
    def __init__(self):
        pass


class Food:
    def __init__(self):
        pass