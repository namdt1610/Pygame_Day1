from os import walk
import pygame


def import_folder(path):
    surface_list = []

    frame_width = 96
    frame_height = 96
    scale = 2

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()

            # scale up 2x the image
            sprite_sheet = pygame.transform.scale(image_surf, (image_surf.get_width(
            ) * scale, image_surf.get_height() * scale))

            # cut the sprite
            for i in range(sprite_sheet.get_width() // frame_width):
                frame = sprite_sheet.subsurface(
                    (i * frame_width, 0, frame_width, frame_height))
                surface_list.append(frame)

    return surface_list
