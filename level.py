import pygame
from settings import *
from player import Player
from overlay import Overlay
from map import TileKind, Map
from support import *


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        # setup MAP
        tile_kinds = [
            TileKind("dirt", "./graphics/Tiles/dirt.png", False),
            TileKind(
                "water", "./graphics/Sprout Lands - Sprites - Basic pack/Tilesets/water.png", False),
        ]
        self.map = Map("./start.map", tile_kinds, 32, (0, 0),
                       self.all_sprites, z=LAYERS['ground'])
        self.player = Player(CENTER_POSITION, self.all_sprites)

        # Kích thước và vị trí ban đầu của bản đồ
        # Generic(
        #     pos=(0, 0),
        #     surf=pygame.image.load(
        #         './graphics/map/map2k.png').convert_alpha(),
        #     groups=self.all_sprites,
        #     z=LAYERS['ground']
        # )

    def run(self, deltaTime):
        self.display_surface.fill('#71ddee')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(deltaTime)
        self.overlay.display()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        self.keyboard_speed = 5
        self.mouse_speed = 0.4
        self.zoom_scale = 1
        self.internal_surf_size = (2000, 2000)
        self.internal_surf = pygame.Surface(
            self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(
            center=(self.half_w, self.half_h))
        self.internal_surf_size_vector = pygame.math.Vector2(
            self.internal_surf_size)
        self.draw_rect_enabled = False
        self.toggle_time = 0
        self.toggle_delay = 200

    def custom_draw(self, player):
        # setup
        self.mouse_control()
        self.keyboard_control()
        self.internal_surf.fill('#71ddee')

        self.offset.x = (player.rect.centerx) - SCREEN_WIDTH / 2
        self.offset.y = (player.rect.centery) - SCREEN_HEIGHT / 2

        scaled_surf_size = pygame.math.Vector2(
            *self.internal_surf_size) * self.zoom_scale
        scaled_surf = pygame.transform.scale(
            self.internal_surf, scaled_surf_size)
        new_center = pygame.math.Vector2(
            (player.rect.centerx - self.offset.x) *
            self.zoom_scale + self.half_w,
            (player.rect.centery - self.offset.y) * self.zoom_scale + self.half_h
        )

        self.display_surface.blit(scaled_surf, new_center)

        # phân layer
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

        # vẽ hitbox
        if self.draw_rect_enabled:
            scaled_hitbox = scaled_surf.get_rect(center=new_center)
            self.draw_hitbox(scaled_hitbox)

    # vẽ hitbox
    def draw_hitbox(self, rect):
        pygame.draw.rect(self.display_surface, (0, 0, 0), rect, 2)

    # điều khiển bằng chuột
    def mouse_control(self):
        events = pygame.event.get(pygame.MOUSEBUTTONDOWN)
        pygame.event.clear(pygame.MOUSEBUTTONDOWN)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom_scale += 0.01
                elif event.button == 5:
                    self.zoom_scale -= 0.01

    # điều khiển bằng bàn phím
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.zoom_scale -= 0.01
        if keys[pygame.K_p]:
            self.zoom_scale += 0.01
        if keys[pygame.K_i] and pygame.time.get_ticks() - self.toggle_time > self.toggle_delay:
            self.draw_rect_enabled = not self.draw_rect_enabled
            self.toggle_time = pygame.time.get_ticks()
