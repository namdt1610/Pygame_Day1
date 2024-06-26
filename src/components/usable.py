import random

from src.data.item_types import item_types


class Action:
    def __init__(self, name, on):
        self.name = name
        self.on = on


class Usable:
    def __init__(self, obj_name):
        self.obj_name = obj_name
        from src.core.engine import engine
        engine.usables.append(self)

    def breakdown(self):
        from src.core.engine import engine
        engine.usables.remove(self)

    def on(self, other, distance):
        print("Base on function called")


class Choppable(Usable):
    def __init__(self, obj_name, chopped_image):
        super().__init__(obj_name)
        self.entity = None
        self.chopped_image = chopped_image
        self.is_chopped = False

    def on(self, other, distance):
        from src.components.player import Player, inventory
        from src.components.sprite import Sprite
        player = other.get(Player)
        if self.is_chopped:
            orange_item_type = item_types[0]  # Get the ItemType for 'Orange'
            num_oranges = random.randint(1, 3)  # Get a random number between 2 and 3
            inventory.add(orange_item_type, num_oranges)
            player.show_message(f"You chopped a tree and found {num_oranges} oranges!")
            return
        chop_best = inventory.get_best("chop_power")
        if chop_best["power"] <= 0:
            player.show_message("You need an axe to chop this " + self.obj_name)
            return
        from src.core.effect import Effect
        Effect(other.x, other.y, 0, 1, 10, chop_best["item"].icon)
        if distance < 60:
            player.show_message("Chopping " + self.obj_name)
            self.entity.get(Sprite).set_image(self.chopped_image)
            self.is_chopped = True
        else:
            player.show_message("I need to get closer")


class Minable(Usable):
    def __init__(self, obj_name):
        super().__init__(obj_name)
        self.entity = None

    def on(self, other, distance):
        from src.components.player import Player, inventory
        player = other.get(Player)
        mine_best = inventory.get_best("mine_power")
        if mine_best["power"] <= 0:
            player.show_message("You need a pickaxe to mine this " + self.obj_name)
            return
        from src.core.effect import Effect
        Effect(other.x, other.y, 0, 1, 10, mine_best["item"].icon)
        if distance < 60:
            player.show_message("Mining " + self.obj_name)
            from src.core.area import area
            area.remove_entity(self.entity)
        else:
            player.show_message("I need to get closer")


class NPC(Usable):

    def __init__(self, obj_name):
        super().__init__(obj_name)

    def on(self, other, distance):
        from src.components.player import Player
        player = other.get(Player)
        if distance < 60:
            player.show_message("Talking to " + self.obj_name)
        else:
            player.show_message("I need to get closer")


class Enemy(Usable):
    def __init__(self, obj_name):
        super().__init__(obj_name)

    def on(self, other, distance):
        from src.components.player import Player
        player = other.get(Player)
        if distance < 60:
            player.show_message("Attacking " + self.obj_name)
        else:
            player.show_message("I need to get closer")
