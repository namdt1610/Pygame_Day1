import os
from os import walk

import pygame


def import_folder(path):
    surface_list = []

    frame_width = 48
    frame_height = 48

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()

            # cut the sprite
            for i in range(image_surf.get_width() // frame_width):
                frame = image_surf.subsurface(
                    (i * frame_width, 0, frame_width, frame_height))
                surface_list.append(frame)

    return surface_list


def get_path(path):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, path)

    return full_path
