import os

import pygame

fonts = {}
labels = []

anti_alias = True
font_folder_path = '../content/fonts'
if os.path.exists(font_folder_path):
    print("The directory exists")
else:
    print("The directory does not exist")


class Label:
    def __init__(self, font, text, size=32, color=(255, 255, 255)):
        from src.core.engine import engine

        self.entity = None
        global labels
        self.text = None
        self.color = color
        self.surface = None

        if font in fonts:
            self.font = fonts[font]
        else:
            self.font = pygame.font.Font(font_folder_path + "/" + font, size)

        self.set_text(text)
        engine.ui_drawables.append(self)

    def get_bounds(self):
        return pygame.Rect(0, 0, self.surface.get_width(), self.surface.get_height())

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, anti_alias, self.color)

    def draw(self, screen):
        screen.blit(self.surface, (self.entity.x, self.entity.y))
