import pygame
from settings import *
from settings import LAYERS


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z=LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z


class Water(Generic):
    def __init__(self, pos, frames, groups):

        # animation setup
        self.frames = frames
        self.frames_index = 0

        # sprite setup
        super().__init(
            pos=pos,
            surf=self.frames[self.frames_index],
            groups=groups,
            z=LAYERS['water']
        )

    def animate(self, dt):
        self.frames_index += 5 * dt
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.images = self.frames[int(self.frames_index)]

    def update(self, dt):
        self.animate(dt)


class WildFlower(Generic):
    def __init(self, pos, surf, groups):
        super().__init__(pos,  surf, groups)


class Tree(Generic):
    def __init(self, pos, surf, groups):
        super().__init__(pos,  surf, groups)
