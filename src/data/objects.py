from src.components.entity import Entity
from src.components.physics import Body
from src.components.player import Player
from src.components.sprite import Sprite
from src.components.teleporter import Teleporter

entity_factories = [
    # 0
    lambda args: Entity(Player(), Sprite("../content/images/player.png"), Body(8, 28, 16, 16)),

    # 1
    lambda args: Entity(Sprite("../content/images/tree/tree_0.png"), Body(14, 64, 16, 32)),

    # 2
    lambda args: Entity(Sprite("../content/images/dirt.png"), Body()),

    # 3
    lambda args: Entity(Teleporter(args[0], args[1], args[2]), Sprite("../content/images/teleporter.png")),
]


def create_entity(id, x, y, data=None):
    factory = entity_factories[id]
    e = factory(data)
    e.x = x * 32
    e.y = y * 32
    return e
