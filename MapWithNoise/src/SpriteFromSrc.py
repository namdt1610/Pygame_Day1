import pygame as pg
import os
class SpriteFromSrc(pg.sprite.Sprite):


    def __init__(self,img_src_path):
        self.all_sprite= pg.sprite.Group()
        self.img_src_path=img_src_path
        self.set_sprite()
    def set_sprite(self):
        for image in os.listdir(self.img_src_path):
            if( image.endswith("png")):
                image_rect= pg.image.load(self.img_src_path+'/'+image).convert()
                #
                _rect=image_rect.get_rect(center=(0,0))     # draw at center return rectangle
                _rect.width=32
                _rect.height=32

                # width and height of rectangle in pixel
                sprite = pg.sprite.Sprite()

                sprite.image= image_rect
                sprite.rect =_rect
                self.all_sprite.add(sprite)


    def get_sprites(self):
        return self.all_sprite





