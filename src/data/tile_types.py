from src.core.map import TileKind

tile_kinds = [
    TileKind("dirt", "dirt.png", False),  # 0
    TileKind("grass", "grass.png", False),  # 1
    TileKind("water", "/water/0.png", True),  # 2
    TileKind("path", "path.png", False),  # 3
    TileKind("floor", "floor.png", False),  # 4
    # TileKind("rock", "rock.png", False),
    # TileKind("sand", "sand.png", False),
    # TileKind("lava", "lava.png", True),
    # TileKind("ice", "ice.png", False)
]
