import pygame

from src.core.camera import camera
from src.core.engine import engine

loaded = {}


class Sprite:
    def __init__(self, image):
        self.entity = None
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        engine.drawables.append(self)  # Thêm sprite vào list sprites

    def delete(self):
        engine.drawables.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.entity.x - camera.x, self.entity.y - camera.y))
