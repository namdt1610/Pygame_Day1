import pygame
from settings import *
from player import Player
from tree import Tree
from overlay import Overlay
from random import randint
from sprites import Generic


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()

        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.player = Player(CENTER_POSITION, self.all_sprites)
        Generic(
            pos=(0, 0),
            surface=pygame.image.load('./graphics/Tiles/FieldsTileset.png'),
            groups=self.all_sprites,
            z=LAYERS['ground']
        )

        for i in range(20):
            random_x = randint(0, 1000)
            random_y = randint(0, 1000)
            self.tree = Tree((random_x, random_y), self.all_sprites)

    def run(self, deltaTime):
        self.display_surface.fill('light green')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(deltaTime)
        self.overlay.display()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH/2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT/2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
