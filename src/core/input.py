import pygame

keys_down = set()
key_just_pressed = set()
mouse_buttons_down = set()
mouse_buttons_just_pressed = set()


def is_key_pressed(key):
    return key in keys_down


def is_mouse_pressed(button):
    return pygame.mouse.get_pressed()[button]


def is_mouse_just_pressed(button):
    return button in mouse_buttons_just_pressed


def is_key_just_pressed(key):
    if key in key_just_pressed:
        key_just_pressed.remove(key)
        return True
    return False


def is_mouse_hovering(rect):
    return rect.collidepoint(pygame.mouse.get_pos())
