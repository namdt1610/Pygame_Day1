import pygame
from settings import *


class TileKind:
    def __init__(self, name, image, is_solid):
        self.name = name
        self.image = pygame.image.load(image)
        self.is_solid = is_solid


class Map(pygame.sprite.Sprite):
    def __init__(self, map_file, tile_kinds, tile_size, pos, group, z=LAYERS['main']):
        self.display_surface = pygame.display.get_surface()
        self.tile_kinds = tile_kinds  # Image of tiles
        # Initialize rect for the map
        self.grid_rect = pygame.Rect(pos, (0, 0))
        self.group = group
        self.z = z

        # Load the data from the file
        with open(map_file, "r") as file:
            data = file.read()

        # Set up the tiles from loaded data
        self.tiles = []
        for line in data.split('\n'):
            row = []
            for tile_number in line:
                row.append(int(tile_number))
            self.tiles.append(row)

        # How big in pixels are the tiles?
        self.tile_size = tile_size

        # Update the rect based on the size of the map
        self.grid_rect.width = len(self.tiles[0]) * tile_size
        self.grid_rect.height = len(self.tiles) * tile_size

        pygame.draw.rect(self.display_surface, (0, 0, 0), self.grid_rect, 2)

    def draw(self, screen):
        # Go row by row
        for y, row in enumerate(self.tiles):
            # Within the current row, go through each tile
            for x, tile in enumerate(row):
                location = (self.grid_rect.left + x * self.tile_size,
                            self.grid_rect.top + y * self.tile_size)
                image = self.tile_kinds[tile].image
                screen.blit(image, location)
