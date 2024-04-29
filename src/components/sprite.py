import pygame

from src.core.camera import camera

loaded = {}
image_path = '../content/images'


class Sprite:
    def __init__(self, image, is_ui=False, animation=None):
        self.entity = None
        self.animation = animation
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image_path + '/' + image).convert_alpha()
            loaded[image] = self.image

        from src.core.engine import engine
        if is_ui:
            engine.ui_drawables.append(self)
        else:
            engine.drawables.append(self)  # Thêm sprite vào list sprites
        self.is_ui = is_ui

    def update(self, dt):
        if self.animation:
            self.animation.update(dt)
            self.image = self.animation.get_current_frame()

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
        if self in engine.drawables:
            engine.drawables.remove(self)

    def draw(self, screen):
        pos = (self.entity.x - camera.x, self.entity.y - camera.y) \
            if not self.is_ui else \
            (self.entity.x, self.entity.y)
        screen.blit(self.image, pos)
