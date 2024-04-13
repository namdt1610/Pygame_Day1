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
    def __init__(self, font, text, size=32, color=(255, 255, 255), hover_color=(0, 0, 0)):
        self.shadow_surface = None
        from src.core.engine import engine

        self.entity = None
        global labels
        self.text = None
        self.color = color
        self.surface = None
        self.default_color = color
        self.hover_color = hover_color
        self.hover_size = size + 10

        if font in fonts:
            self.font = fonts[font]
        else:
            self.font = pygame.font.Font(font_folder_path + "/" + font, size)

        self.set_text(text)
        engine.ui_drawables.append(self)

    def breakdown(self):
        from src.core.engine import engine
        engine.ui_drawables.remove(self)

    def get_bounds(self):
        return pygame.Rect(0, 0, self.surface.get_width(), self.surface.get_height())

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.get_bounds().collidepoint(mouse_pos):
            print("Hovering")
            self.color = self.hover_color
            self.size = self.hover_size
        else:
            self.color = self.default_color
        self.image = self.font.render(self.text, True, self.color)
        return self

    def set_text(self, text):
        self.text = text
        self.surface = self.font.render(self.text, anti_alias, self.color)
        self.shadow_surface = self.font.render(self.text, anti_alias, (0, 0, 0))

    def draw(self, screen):
        # Draw the shadow
        screen.blit(self.shadow_surface, (self.entity.x + 1, self.entity.y + 1))
        # Draw the text
        screen.blit(self.surface, (self.entity.x, self.entity.y))
