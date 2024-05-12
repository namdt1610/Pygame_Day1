from math import ceil

from src.components.entity import Entity
from src.components.label import Label
from src.components.sprite import Sprite
from src.components.ui.window import Window
from src.components.ui.window import create_window

items_per_row = 10
padding_size = 5
gap_size = 5
item_size = 32
avatar_width = 76
message_time_seconds = 3


class InventoryView:
    def __init__(self, inventory, avatar_image="avatar.png", slot_image="inventory_slot.png",
                 selected_slot_image="inventory_slot_selected.png"):
        self.message_label = None
        self.message_countdown = None
        self.inventory = inventory
        self.avatar_image = avatar_image
        self.slot_image = slot_image
        self.selected_slot_image = selected_slot_image

        width = padding_size + (items_per_row * item_size) + (
                (items_per_row - 1) * gap_size) + padding_size + avatar_width
        rows = ceil(inventory.capacity / items_per_row)
        height = padding_size + (rows * item_size) + ((rows - 1) * gap_size) + padding_size

        from src.core.camera import camera
        x = camera.width // 2 - width // 2
        y = camera.height - 25 - height

        self.window = create_window(x, y, width, height)
        self.slot_container_sprites = []
        self.slot_sprites = []

        from src.core.engine import engine
        engine.active_objs.append(self)

        inventory.listener = self

        self.render()

    def update(self):
        import pygame
        from src.core.input import is_mouse_just_pressed
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse is clicking on the inventory
        if is_mouse_just_pressed(1):
            if (self.window.x + avatar_width) <= mouse_pos[0] <= self.window.x + self.window.get(Window).width and \
                    self.window.y <= mouse_pos[1] <= self.window.y + self.window.get(Window).height:

                # Find the exact slot the mouse is on, instead of searching them all.
                x = mouse_pos[0] - self.window.x - avatar_width
                y = mouse_pos[1] - self.window.y
                x_slot = int((x - padding_size) / (item_size + gap_size))
                y_slot = int((y - padding_size) / (item_size + gap_size))

                # Useful for checking that the mouse is not in the gap.
                x_local_pos = x % (item_size + gap_size)
                y_local_pos = y % (item_size + gap_size)

                # print(x, y, x_slot, y_slot, x_local_pos, y_local_pos)

                if 0 < x_local_pos < item_size and 0 < y_local_pos < item_size:
                    index = int(x_slot + (y_slot * items_per_row))
                    if self.inventory.equipped_slot == index:
                        self.inventory.equipped_slot = None
                    else:
                        self.inventory.equipped_slot = index
                    self.refresh()

                    if index > 0:
                        print("Inventory Slot", self.inventory.equipped_slot)
                    else:
                        print("Inventory Slot None")

    def render(self):
        print("Called render")
        row = 0
        column = 0

        # Tạo Entity cho avatar sprite
        avatar_sprite = Entity(Sprite(self.avatar_image, True), x=self.window.x, y=self.window.y)
        self.window.get(Window).items.append(avatar_sprite)

        # Tạo Entity cho các slot
        for index, slot in enumerate(self.inventory.slots):
            if index < 10:
                x = column * (item_size + gap_size) + (self.window.x + avatar_width) + padding_size
                y = row * (item_size + gap_size) + self.window.y + padding_size

                slot_image = self.selected_slot_image if index == self.inventory.equipped_slot else self.slot_image
                container_sprite = Entity(Sprite(slot_image, True), x=x, y=y)
                self.window.get(Window).items.append(container_sprite)
                if slot.type is not None:
                    print(slot.type.name)
                    item_sprite = Entity(Sprite(slot.type.icon_name, True), x=x, y=y)
                    if slot.type.stack_size > 1:
                        label = Entity(Label("main/Pixellari.ttf", str(slot.amount), color=(255, 255, 0), size=30),
                                       x=x, y=y)
                        self.window.get(Window).items.append(label)
                    self.window.get(Window).items.append(item_sprite)
                column += 1
                if column >= items_per_row:
                    column = 0
                    row += 1

    def clear(self):
        for i in self.window.get(Window).items:
            if i.has(Sprite):
                i.get(Sprite).breakdown()
            elif i.has(Label):
                i.get(Label).breakdown()
        self.window.get(Window).items.clear()

    def refresh(self):
        self.clear()
        self.render()

    def breakdown(self):
        pass

    def show_message(self, message):
        self.message_label.set_text(message)
        self.message_countdown = message_time_seconds * 60
