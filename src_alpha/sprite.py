import pygame.sprite
from settings import *
from support import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, image, group, z=LAYERS['main']):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z


class Tree(Generic):
    def __init__(self, pos, surf, groups, name, player_add):
        super().__init__(pos, surf, groups)

        # tree attributes
        self.health = 5
        self.alive = True
        stump_path = get_path(
            f'../graphics/stumps/{"small" if name == "Small" else "large"}.png')
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()

        # fruit
        fruit_path = get_path('../graphics/fruit/apple.png')
        self.fruit_surf = pygame.image.load(fruit_path)
        self.fruit_surf = FRUIT_POS[name]
        self.fruit_sprites = pygame.sprite.Group()
        # self.create_fruit()

        self.player_add = player_add

        # sounds
        axe_sound_path = get_path('../audio/axe.mp3')
        self.axe_sound = pygame.mixer.Sound(axe_sound_path)
