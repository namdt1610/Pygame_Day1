import pygame

from src.components.entity import Entity
from src.components.inventory import Inventory
from src.components.label import Label
from src.components.physics import Body, triggers
from src.components.sprite import Sprite
from src.components.ui.inventory_view import InventoryView
from src.core.area import area
from src.core.camera import camera
from src.core.engine import engine
from src.core.input import is_key_pressed
from src.core.math_ext import distance

movement_speed = 2
inventory = Inventory(10)
message_time_seconds = 3


class Player:
    def __init__(self):
        # self.animations = None
        self.entity = None

        self.location_label = Entity(Label("main/Pixellari.ttf", "X:0 Y:0")).get(Label)
        self.message_label = Entity(Label("main/Pixellari.ttf", area.name)).get(Label)
        self.inventory_window = Entity(InventoryView(inventory))

        from src.core.camera import camera
        self.location_label.entity.y = camera.height - 50
        self.location_label.entity.x = 10
        self.message_label.entity.x = 10
        self.show_message(f"Entering {area.name}")

        # self.animations = {}
        # self.import_assets()
        self.status = 'down'
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

    def setup(self):
        pass

    def show_message(self, message):
        self.message_label.set_text(message)
        self.message_countdown = message_time_seconds * 60

    def interact(self, mouse_pos):
        from src.core.engine import engine
        for usable in engine.usables:
            if usable.entity.has(Sprite):
                usable_sprite = usable.entity.get(Sprite)
                x_sprite = usable.entity.x - camera.x
                y_sprite = usable.entity.y - camera.y
                width_sprite = usable_sprite.image.get_width()
                height_sprite = usable_sprite.image.get_height()

                if x_sprite < mouse_pos[0] < x_sprite + width_sprite and \
                        y_sprite < mouse_pos[1] < y_sprite + height_sprite:
                    my_sprite = self.entity.get(Sprite)

                    # Calculate the distance between these two sprites, from their feet
                    d = distance(x_sprite + usable_sprite.image.get_width() / 2,
                                 y_sprite + usable_sprite.image.get_height(),
                                 self.entity.x - camera.x + my_sprite.image.get_width() / 2,
                                 self.entity.y - camera.y + my_sprite.image.get_height())

                    # Call the usable function
                    usable.on(self.entity, d)

                    # We only want to interact with the first thing we click.
                    # Return prevents anymore objects being interacted with on this
                    # click
                    return

    def update(self):
        if self.message_countdown > 0:
            self.message_countdown -= 1
            if self.message_countdown <= 0:
                self.message_label.set_text(" ")
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

        from src.core.input import is_mouse_just_pressed
        mouse_pos = pygame.mouse.get_pos()
        if is_mouse_just_pressed(1):
            self.interact(mouse_pos)

        # Center the camera on player
        camera.x = self.entity.x - camera.width / 2 + sprite.image.get_width() / 2
        camera.y = self.entity.y - camera.height / 2 + sprite.image.get_height() / 2

        # Check if the player is colliding with a trigger
        for t in triggers:
            if body.is_colliding_with(t):
                t.on(self.entity)
