import pygame

from src.core.input import is_mouse_pressed


class Button:
    def __init__(self, on, click=pygame.Rect(0, 0, 32, 32)):
        from src.core.engine import engine
        engine.active_objs.append(self)
        self.click = click
        self.on = on

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        x = self.click.x + self.entity.x
        y = self.click.y + self.entity.y

        if is_mouse_pressed(0):
            if x <= mouse_pos[0] <= x + self.click.width and \
                    y <= mouse_pos[1] <= y + self.click.height:
                self.on()
