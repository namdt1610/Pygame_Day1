from src.components.enemy import Enemy
from src.components.entity import Entity
from src.components.inventory import DroppedItem
from src.components.npc import NPC
from src.components.physics import Body
from src.components.player import Player
from src.components.sprite import Sprite
from src.components.teleporter import Teleporter
from src.components.usable import Choppable
from src.data.item_types import item_types

entity_factories = [
    # 0
    lambda args: Entity(Player(100), Sprite("player/player.png"), Body(6, 40, 16, 16)),

    # 1
    lambda args: Entity(Sprite("env/tree_0.png"), Body(50, 150, 60, 50), Choppable("tree", "env/tree_0_chopped.png")),

    # 2
    lambda args: Entity(Sprite("env/grass.png"), Body()),

    # 3
    lambda args: Entity(Teleporter(args[0], args[1], args[2]), Sprite("teleporter.png")),

    # 4
    lambda args: Entity(DroppedItem(item_types[int(args[0])], int(args[1])),
                        Sprite(item_types[int(args[0])].icon_name)),

    # 5
    lambda args: Entity(Sprite("house.png"), Body(0, 160, 224, 140)),

    # 6
    lambda args: Entity(Sprite(args[1]), NPC(args[0], args[2])),

    # 7
    lambda args: Entity(Sprite(args[0]), Enemy(10, 4), Body(0, 0, 32, 32)),
]


def create_entity(id, x, y, data=None):
    factory = entity_factories[id]
    e = factory(data)
    e.x = x * 32
    e.y = y * 32
    return e
