import pygame
from settings import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, group):
        super().__init__(group)

        # general setup
        original_image = pygame.image.load(image_path).convert_alpha()
        scale_factor = 2
        self.sheet = pygame.transform.scale(original_image, (original_image.get_width(
        ) * scale_factor, original_image.get_height() * scale_factor))
        self.rect = self.sheet.get_rect(center=pos)

        # movement atributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # animations attributes
        self.frames = []
        self.frame_index = 0
        self.image = self.sheet
        self.animation_speed = 0.1
        self.current_time = 0
        self.load_frames()

    def load_frames(self):

        frame_width = 96
        frame_height = 96
        for i in range(self.sheet.get_width() // frame_width):
            frame = self.sheet.subsurface(
                (i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, deltaTime):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * deltaTime
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * deltaTime
        self.rect.centery = self.pos.y

    def animate(self, deltaTime):
        self.current_time += deltaTime

        if self.current_time > self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
            self.current_time = 0

    def update(self, deltaTime):
        self.input()
        self.move(deltaTime)
        self.animate(deltaTime)
