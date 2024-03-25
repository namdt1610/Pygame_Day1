import pygame

keys_down = set()


def is_key_pressed(key):
    return key in keys_down


def is_mouse_pressed(button):
    return pygame.mouse.get_pressed()[button]
