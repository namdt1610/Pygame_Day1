import pygame

from src.components.entity import active_objs
from src.components.physics import Body, triggers
from src.components.sprite import Sprite
from src.components.support import import_folder
from src.core.camera import camera
from src.core.input import is_key_pressed

movement_speed = 2


class Player:
    def __init__(self):
        active_objs.append(self)
        # self.animations = {}
        # self.import_assets()
        # self.status = 'idle'
        # self.frame_index = 0
        # self.image = self.animations[self.status][self.frame_index]

    def import_assets(self):
        self.animations = {'idle_up': [], 'idle_down': [], 'idle_left': [], 'idle_right': [],
                           'walk_up': [], 'walk_down': [], 'walk_left': [], 'walk_right': [], }

        for animation in self.animations.keys():
            full_path = '../content/images/player/' + animation
            self.animations[animation] = import_folder(full_path)

    def update(self):
        # Save the previous position
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        # Move the player
        if is_key_pressed(pygame.K_w):
            self.entity.y -= movement_speed
        if is_key_pressed(pygame.K_s):
            self.entity.y += movement_speed
        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_d):
            self.entity.x += movement_speed
        if is_key_pressed(pygame.K_a):
            self.entity.x -= movement_speed
        if not body.is_position_valid():
            self.entity.x = previous_x

        # Center the camera on player
        camera.x = self.entity.x - camera.width / 2 + sprite.image.get_width() / 2
        camera.y = self.entity.y - camera.height / 2 + sprite.image.get_height() / 2

        # Check if the player is colliding with a trigger
        for t in triggers:
            if body.is_colliding_with(t):
                t.on()
