from src.components.inventory import ItemType

item_types = [
    # 0
    ItemType("Orange", "fruits/orange.png", 64),
    # 1
    ItemType("Salmon berry", "fruits/salmonberry.png", 64),
    # 2
    ItemType("Axe", "tools/axe.png", 1, chop_power=5),
    # 3
    ItemType("Pickaxe", "tools/pickaxe.png", 1, mine_power=5),
    # 4
    ItemType("Cracked Sword", "weapons/sword_1.png", 1, damage=5, cooldown=1, range=50),
    # 5
    ItemType("Sword", "weapons/sword_2.png", 1, damage=7, cooldown=1, range=50)
]
