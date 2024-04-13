from src.components.physics import Trigger
from src.components.player import Player


def teleport(area_file, player_x, player_y):
    # print(f"Teleporting to {area_file} at position ({player_x}, {player_y})")
    from src.core.area import area
    area.load_area_file(area_file)
    # Search for the player and move it to the new position
    if player_x is not None and player_y is not None:
        player = area.search_for_first(Player)
        player.x = player_x * 32
        player.y = player_y * 32


# Teleporter entities are used to teleport the player to another area
class Teleporter(Trigger):
    def __init__(self, area_file, player_x=None, player_y=None, x=0, y=0, width=32, height=32):
        super().__init__(lambda other: teleport(area_file, int(player_x), int(player_y)), x, y, width, height)
        print(area_file)
