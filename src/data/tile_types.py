from src.core.map import TileKind

tile_kinds = [
    TileKind("collision", "empty.png", True),  # 0
    TileKind("dirt", "env/dirt.png", False),  # 1
    TileKind("grass", "env/grass.png", False),  # 2
    TileKind("water", "/water/0.png", True),  # 3
    TileKind("path", "path.png", False),  # 4
    TileKind("floor", "floor.png", False),  # 5
    # TileKind("rock", "rock.png", False),
    # TileKind("sand", "sand.png", False),
    # TileKind("lava", "lava.png", True),
    # TileKind("ice", "ice.png", False)
]
