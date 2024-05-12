import pygame

from src.components.entity import Entity
from src.components.inventory import Inventory
from src.components.label import Label
from src.components.physics import Body, triggers
from src.components.sprite import Sprite
from src.components.ui.bar import Bar
from src.components.ui.inventory_view import InventoryView
from src.core.area import area
from src.core.camera import camera
from src.core.engine import engine
from src.core.input import is_key_pressed, is_key_just_pressed
from src.core.math_ext import distance
from src.data.item_types import item_types

movement_speed = 2
inventory = Inventory(10)
message_time_seconds = 3


def on_player_death(entity):
    from src.core.engine import engine
    inventory.reset()
    engine.switch_to('Menu')


class Player:
    def __init__(self, heath, stamina=100):
        self.stamina_bar = None
        self.message_countdown = None
        from src.core.engine import engine
        engine.active_objs.append(self)
        self.entity = None

        self.location_label = Entity(Label("main/Pixellari.ttf", "X:0 Y:0")).get(Label)
        self.message_label = Entity(Label("main/Pixellari.ttf", area.name)).get(Label)
        self.inventory_window = Entity(InventoryView(inventory))

        from src.core.camera import camera
        self.location_label.entity.y = camera.height - 50
        self.location_label.entity.x = 10
        self.message_label.entity.x = 10
        self.show_message(f"Entering {area.name}")

        from src.core.engine import engine
        engine.active_objs.append(self)

        self.combat = None
        self.health_bar = None
        self.heath = heath
        self.stamina = stamina

        self.has_interacted = False

    def setup(self):
        from src.components.combat import Combat
        combat = Combat(self.heath, on_player_death)
        self.entity.add(combat)
        self.combat = combat
        del self.heath

        self.health_bar = Entity(Bar(self.combat.max_health,
                                     (255, 0, 0),
                                     (0, 255, 0))).get(Bar)

        self.health_bar.entity.x = camera.width // 2 - self.health_bar.width // 2 + 38
        self.health_bar.entity.y = camera.height - 5 - self.health_bar.height
        print("Player setup called")

        self.stamina_bar = Entity(Bar(self.stamina,
                                      (255, 0, 0),
                                      (0, 0, 255))).get(Bar)
        self.stamina_bar.entity.x = camera.width // 2 - self.stamina_bar.width // 2 + 38
        self.stamina_bar.entity.y = camera.height - 40 - self.stamina_bar.height - self.health_bar.height - 5

    def interact(self, mouse_pos):
        for usable in engine.usables:
            if usable.entity.has(Sprite):
                usable_sprite = usable.entity.get(Sprite)

                # Get the x, y, width and height of the usable's sprite
                x_sprite = usable.entity.x - camera.x
                y_sprite = usable.entity.y - camera.y
                width_sprite = usable_sprite.image.get_width()
                height_sprite = usable_sprite.image.get_height()

                # Check if the mouse is clicking this
                if x_sprite < mouse_pos[0] < x_sprite + width_sprite and \
                        y_sprite < mouse_pos[1] < y_sprite + height_sprite:
                    # Get our sprite
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

    def show_message(self, message):
        self.message_label.set_text(message)
        self.message_countdown = message_time_seconds * 60

    def update(self):
        if self.message_countdown > 0:
            self.message_countdown -= 1
            if self.message_countdown <= 0:
                self.message_label.set_text("")
        self.location_label.set_text(f"X: {int(self.entity.x / 32)} - Y: {int(self.entity.y / 32)}")
        previous_x = self.entity.x
        previous_y = self.entity.y
        sprite = self.entity.get(Sprite)
        body = self.entity.get(Body)
        self.health_bar.amount = self.combat.health

        if is_key_pressed(pygame.K_w):
            self.entity.y -= movement_speed
        if is_key_pressed(pygame.K_s):
            self.entity.y += movement_speed
        if not body.is_position_valid():
            self.entity.y = previous_y

        if is_key_pressed(pygame.K_ESCAPE):
            from src.core.engine import engine
            engine.switch_to("Menu")

        from src.core.input import is_mouse_just_pressed
        mouse_pos = pygame.mouse.get_pos()

        if self.combat.equipped is None and inventory.equipped_slot is not None:
            # print("Equipping")
            self.combat.equip(inventory.slots[inventory.equipped_slot].type)

        if self.combat.equipped is not None and inventory.equipped_slot is None:
            print("Unequipping", self.combat.equipped, inventory.equipped_slot)
            self.combat.unequip()

        if is_mouse_just_pressed(1):
            if self.combat.equipped is None:
                self.interact(mouse_pos)
            else:
                self.combat.perform_attack()

        if is_key_pressed(pygame.K_a):
            self.entity.x -= movement_speed
        if is_key_pressed(pygame.K_d):
            self.entity.x += movement_speed
        if not body.is_position_valid():
            self.entity.x = previous_x
        camera.x = self.entity.x - camera.width / 2 + sprite.image.get_width() / 2
        camera.y = self.entity.y - camera.height / 2 + sprite.image.get_height() / 2

        if is_key_pressed(pygame.K_w) or is_key_pressed(pygame.K_s) or is_key_pressed(pygame.K_a) or is_key_pressed(
                pygame.K_d):
            self.stamina -= 0.1  # Adjust this value based on how fast you want the stamina to decrease
            if self.stamina < 0:
                self.stamina = 0
        self.stamina_bar.amount = self.stamina

        # If stamina is 0, start decreasing health
        if self.stamina == 0:
            self.combat.health -= 0.1  # Adjust this value based on how fast you want the health to decrease
            if self.combat.health < 0:
                self.combat.health = 0
        self.health_bar.amount = self.combat.health

        for t in triggers:
            if body.is_colliding_with(t):
                t.on(self.entity)

        if is_key_just_pressed(pygame.K_e):
            print("Key 'E' pressed")
            self.eat_orange()

        if self.combat.health <= 0:
            self.combat.on_death()

    def eat_orange(self):
        print("Eating an orange")
        # Get the ItemType for 'Orange'
        orange_item_type = item_types[0]
        # Check if the player has an orange in their inventory
        if inventory.has(orange_item_type):
            # Remove the orange from the inventory
            inventory.remove(orange_item_type)
            # Increase the player's stamina
            self.stamina += 20  # Adjust this value based on how much stamina you want to recover
            if self.stamina > 100:  # Assuming the maximum stamina is 100
                self.stamina = 100
            self.stamina_bar.amount = self.stamina
            self.show_message("You ate an orange and recovered some stamina!")
        else:
            self.show_message("You don't have any oranges.")
