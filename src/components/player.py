import pygame

from src.components.entity import Entity
from src.components.label import Label
from src.components.physics import Body, triggers
from src.components.sprite import Sprite
from src.core.area import area
from src.core.camera import camera
from src.core.engine import engine
from src.core.input import is_key_pressed

movement_speed = 2


class Player:
    def __init__(self):
        # self.animations = None
        self.entity = None

        self.location_label = Entity(Label("main/Pixellari.ttf", "X:0 Y:0")).get(Label)
        self.area_name_label = Entity(Label("main/Pixellari.ttf", area.name)).get(Label)
        self.location_label.entity.y = camera.height - 50
        self.location_label.entity.x = 10
        self.area_name_label.entity.x = 10

        # self.animations = {}
        # self.import_assets()
        # self.status = 'down'
        # self.frame_index = 0
        # self.image = self.animations[self.status][self.frame_index]

        # def import_assets(self):
        #     self.animations = {'idle_up': [], 'idle_down': [], 'idle_left': [], 'idle_right': [],
        #                        'run_up': [], 'run_down': [], 'run_left': [], 'run_right': [], }
        #
        #     for animation in self.animations.keys():
        #         full_path = '../content/images/player/' + animation
        #         self.animations[animation] = import_folder(full_path)

        from src.core.engine import engine
        engine.active_objs.append(self)

    def update(self):
        # Update the player's location
        self.location_label.set_text(f"X:{self.entity.x // 32} Y:{self.entity.y // 32}")

        # Save the previous position
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)

        # Move the player
        if is_key_pressed(pygame.K_w):
            self.status = 'run_up'
            self.entity.y -= movement_speed
        if is_key_pressed(pygame.K_s):
            self.status = 'run_down'
            self.entity.y += movement_speed
        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_d):
            self.status = 'run_right'
            self.entity.x += movement_speed
        if is_key_pressed(pygame.K_a):
            self.status = 'run_left'
            self.entity.x -= movement_speed
        if not body.is_position_valid():
            self.entity.x = previous_x

        if is_key_pressed(pygame.K_ESCAPE):
            engine.switch_to('Menu')

        # Center the camera on player
        camera.x = self.entity.x - camera.width / 2 + sprite.image.get_width() / 2
        camera.y = self.entity.y - camera.height / 2 + sprite.image.get_height() / 2

        # Check if the player is colliding with a trigger
        for t in triggers:
            if body.is_colliding_with(t):
                t.on()
