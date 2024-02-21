import random
import sys

import numpy as np
import matplotlib.pyplot as plt
import noise
import pygame as pg

import SpriteFromSrc as sfs


class RenderMap:
    # Kích thước của hình ảnh
    width, height = 1024*16, 1024*16
# Tạo một lưới tiếng ồn Perlin
    scale = 400

    octaves = 3
    persistence = 0.05
    frequency = 1.5
    lacunarity = 2
    world = np.zeros((width, height))
    base = random.randint(1, 100)
# Thuộc tính của noise perlin

    my_dict = dict(key1='soil', key3='water')

    def __init__(self):
        pg.display.init()
        self.screen = pg.display
        self.surface = self.screen.set_mode((2048, 2048))

        self.ground_sprite = sfs.SpriteFromSrc(
            "img/ground_sprites")  # load ground sprite from src
        self.group_sprite = self.ground_sprite.get_sprites()  # convert in to group

        self.water_sprite = sfs.SpriteFromSrc("img/water_sprites")   #
        self.group_water_sprite = self.water_sprite.get_sprites()

    def clamp(self, value, min_value, max_value):
        return int(max(min_value, min(value, max_value)))

    def createDataNoise(self):
        for i in range(0, self.width, 16):
            for j in range(0, self.height, 16):
                self.world[i][j] = noise.pnoise2(i/self.scale * self.frequency,
                                                 j/self.scale*self.frequency,
                                                 octaves=self.octaves,
                                                 persistence=self.persistence,
                                                 lacunarity=self.lacunarity,
                                                 repeatx=1024,
                                                 repeaty=1024,
                                                 base=self.base)
                self.world[i][j] = self.world[i][j]*7
                tempSprite = self.draw(self.world[i][j])
                tempSprite.rect.x = i
                tempSprite.rect.y = j
                self.surface.blit(source=tempSprite.image, dest=(
                    tempSprite.rect.x, tempSprite.rect.y))

        print(len(self.world))

       # plt.imsave(fname="map.png",cmap='gray',format="png",origin='lower',arr=self.world)
        plt.show()

    def draw(self, pervalue):

        list_sprite = self.group_sprite.sprites()
        list_water_sprite = self.group_water_sprite.sprites()
        if (pervalue > -4.5 and pervalue <= -1.45):
            return list_water_sprite[0]  # blue code mean water
        else:
            return list_sprite[random.randint(0, 62)]  # brown for soil

    # Từ âm 4.6 đến -0.67 là nước
    def fromNoiseToMap(self):
        # self.screen.get_surface().get
        print("done")
        # pg.image.save(self.surface,"map.png")
        pg.display.flip()
        pg.image.save(self.surface, "my_map.png")
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
        pg.quit()

        sys.exit()
