# Gameplay là quan trọng nhât
import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("DayOne")
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.font = './graphics/Pixellari.ttf'
        self.clock = pygame.time.Clock()
        self.level = Level()

    def display_fps(self):
        game_fps = self.clock.get_fps()
        font = pygame.font.Font(self.font, 36)
        fps_text = font.render(
            f"FPS: {int(game_fps)}", True, (0, 0, 0))
        self.screen.blit(fps_text, (10, 10))

    def display_clock(self):
        game_clock = pygame.time.get_ticks()
        font = pygame.font.Font(self.font, 36)
        clock_text = font.render(
            f"Clock: {(game_clock)/1000}", True, (0, 0, 0))
        self.screen.blit(clock_text, (500, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            deltaTime = self.clock.tick(FPS) / 1000
            self.level.run(deltaTime)
            self.display_fps()
            self.display_clock()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
