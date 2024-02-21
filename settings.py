from pygame.math import Vector2


# SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 32
FPS = 60

# GENERAL
GRID_WIDTH = SCREEN_WIDTH / TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / TILE_SIZE

# OVERLAY POSITION
OVERLAY_POSITIONS = {
    'tool box': (64, SCREEN_HEIGHT),
    'tool': (64, SCREEN_HEIGHT)
}

CENTER_POSITION = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
TOPLEFT_POSITION = (0, 0)
TOPRIGHT_POSITION = (SCREEN_WIDTH, 0)

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10,
}
