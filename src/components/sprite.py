import pygame

from src.core.camera import camera

loaded = {}
image_path = '../content/images'


class Sprite:
    def __init__(self, image, is_ui=False):
        from src.core.engine import engine
        self.entity = None
        global sprites
        self.is_ui = is_ui
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_path + '/' + image).convert_alpha()
            loaded[image] = self.image
        engine.drawables.append(self)

    def set_image(self, image):
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_path + "/" + image)
            loaded[image] = self.image

    def delete(self):
        from src.core.engine import engine
        engine.drawables.remove(self)

    def breakdown(self):
        from src.core.engine import engine
        engine.drawables.remove(self)

    def draw(self, screen):
        pos = (self.entity.x - camera.x, self.entity.y - camera.y) \
            if not self.is_ui else \
            (self.entity.x, self.entity.y)
        screen.blit(self.image, pos)
