import pygame
from settings import *
from player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        player_image_path = './graphics/1 Woodcutter/idle/Woodcutter_idle.png'
        self.player = Player(player_image_path, (640, 360), self.all_sprites)

    def run(self, deltaTime):
        self.display_surface.fill('white')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(deltaTime)
