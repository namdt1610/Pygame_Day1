from src.components.entity import Entity


class Window:
    def __init__(self, width=32, height=32):
        self.entity = None
        self.surface = None
        self.width = width
        self.height = height
        self.items = []

    def draw(self, screen):
        screen.blit(self.surface, (self.entity.x, self.entity.y))


def create_window(x, y, width, height):
    return Entity(Window(width, height), x=x, y=y)
