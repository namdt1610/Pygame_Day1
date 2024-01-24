import pygame
from settings import *
from player import Player
from overlay import Overlay


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = pygame.sprite.Group()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player((640, 360), self.all_sprites)

    def run(self, deltaTime):
        self.display_surface.fill('light green')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(deltaTime)
        self.overlay.display()
