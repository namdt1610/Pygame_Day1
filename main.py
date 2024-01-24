import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DayOne")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.font = './graphics/Pixellari.ttf'

    def display_fps(self):
        game_fps = self.clock.get_fps()
        font = pygame.font.Font(self.font, 36)
        fps_text_game = font.render(
            f"FPS: {int(game_fps)}", True, (0, 0, 0))
        self.screen.blit(fps_text_game, (10, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.clock.tick(60) / 1000
            self.level.run(deltaTime)
            self.display_fps()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
