from pygame.math import Vector2

# SCREEN
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

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
    'plant': 2,
    'main': 7,
}
