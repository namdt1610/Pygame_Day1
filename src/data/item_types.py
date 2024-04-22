from src.components.inventory import ItemType

item_types = [
    ItemType("Orange", "fruits/orange.png", 64),
    ItemType("Salmon berry", "fruits/salmonberry.png", 64),
    ItemType("Axe", "tools/axe.png", 1, chop_power=5),
    ItemType("Pickaxe", "tools/pickaxe.png", 1, mine_power=5)
]
