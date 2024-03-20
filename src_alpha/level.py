from overlay import Overlay
from player import Player
from settings import *
from support import *
from sprite import Generic

zoom = 1.0


def get_scaled_size(size):
    return int(size * zoom)


class Level:
    def __init__(self):
        # lây surf màn hình
        self.display_surface = pygame.display.get_surface()

        # setup các thứ trên level
        self.all_sprites = CameraGroup()
        self.player = Player(CENTER_POSITION, self.all_sprites)
        map_path = get_path('../MapWithNoise/src/my_map.png')
        self.overlay = Overlay(self.player)
        Generic(pos=(0, 0), image=pygame.image.load(map_path).convert_alpha(), group=self.all_sprites, z=['ground'])

    def run(self, delta_time):
        self.display_surface.fill('black')
        self.all_sprites.player_focus_camera(self.player)
        self.all_sprites.update(delta_time)
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

        # ground
        self.ground_surf = pygame.image.load('../MapWithNoise/src/my_map.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))

        # các thuộc tính để zoom
        self.zoom_scale = 1.2  # thông số zoom
        self.internal_surf_size = (1280, 720)
        self.internal_surf = pygame.Surface(
            self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(
            center=(self.half_w, self.half_h))
        self.internal_surf_size_vector = pygame.math.Vector2(
            self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

        # Thuộc tính để vẽ hitbox
        self.draw_rect_enabled = False
        self.toggle_time = 0
        self.toggle_delay = 200

    # vẽ trên camera
    def player_focus_camera(self, player):
        # self.mouse_control()
        # self.keyboard_control()
        #
        # # fill internal_surf
        # self.internal_surf.fill((0, 0, 0, 0))
        #
        # # ground (di chuyển theo player)
        # ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        # self.internal_surf.blit(self.ground_surf, ground_offset)
        #
        # # camera offset (theo dõi player)
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        # phân layer
        # for layer in LAYERS.values():
        #     for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
        #         if sprite.z == layer:
        #             offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
        #             self.internal_surf.blit(sprite.image, offset_pos)
        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
        # # surface khi thu phóng
        # scaled_surf = pygame.transform.scale(self.internal_surf, self.internal_surf_size_vector * self.zoom_scale)
        # scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))
        #
        # self.display_surface.blit(scaled_surf, scaled_rect)
        #
        # # vẽ hitbox
        # if self.draw_rect_enabled:
        #     # hitbox camera
        #     scaled_hitbox = scaled_surf.get_rect()
        #     self.draw_hitbox(scaled_hitbox)

    # vẽ hitbox
    def draw_hitbox(self, rect):
        pygame.draw.rect(self.display_surface, (0, 0, 0), rect, 2)

    # điều khiển bằng chuột
    def mouse_control(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom_scale += 0.05
                elif event.button == 5:
                    self.zoom_scale -= 0.05
                    if self.zoom_scale >= 5:
                        pass

    # điều khiển bằng bàn phím
    def keyboard_control(self):
        keys = pygame.key.get_pressed()
        if 0 < self.zoom_scale < 3:
            if keys[pygame.K_EQUALS]:
                self.zoom_scale += 0.05
                if self.zoom_scale > 2.9:
                    self.zoom_scale = 2.9
            elif keys[pygame.K_MINUS]:
                self.zoom_scale -= 0.05
                print(self.zoom_scale)
                if self.zoom_scale < 0.1:  # Đảm bảo không âm
                    self.zoom_scale = 0.1
            if keys[pygame.K_i] and pygame.time.get_ticks() - self.toggle_time > self.toggle_delay:
                self.draw_rect_enabled = not self.draw_rect_enabled
                self.toggle_time = pygame.time.get_ticks()
