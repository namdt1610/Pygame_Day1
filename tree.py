import pygame
from support import *
from settings import *


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        original_image = pygame.image.load(
            './graphics/Tree/Curved_tree1.png').convert_alpha()

        scale = 2
        self.image = pygame.transform.scale(original_image, (int(
            original_image.get_width() * scale), int(original_image.get_height() * scale)))
        self.rect = self.image.get_rect(topleft=pos)
        self.z = LAYERS['plant']
