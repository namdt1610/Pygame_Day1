from src.components.inventory import ItemType

item_types = [
    # 0
    ItemType("Orange", "fruits/orange.png", "food", 64, heal=5),
    # 1
    ItemType("Salmon berry", "fruits/salmon_berry.png", "food", 64, heal=7),
    # 2
    ItemType("Axe", "tools/axe.png", "weapon", 1, chop_power=5, cooldown=1, range=50),
    # 3
    ItemType("Pickaxe", "tools/pickaxe.png", "tool", 1, mine_power=5),
    # 4
    ItemType("Cracked Sword", "weapons/sword_1.png", "weapon", 1, damage=5, cooldown=1, range=50),
    # 5
    ItemType("Sword", "weapons/sword_2.png", "weapon", 1, damage=7, cooldown=1, range=50)
]
