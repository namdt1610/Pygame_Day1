import pygame.display

from src.components.entity import active_objs
from src.components.sprite import sprites
from src.core.area import Area
from src.core.camera import create_screen
from src.core.input import keys_down
from src.data.tile_types import tile_kinds

pygame.init()

# GENERAL SETUP
screen_width = 1280
screen_height = 720
clear_color = (0, 0, 0)
screen = create_screen(screen_width, screen_height, "DayOne")
running = True

area = Area("start.map", tile_kinds)
entities = area.entities

# CAMERA
camera_offset_x = 0

while running:
    # MAIN LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys_down.add(event.key)
        elif event.type == pygame.KEYUP:
            keys_down.remove(event.key)

    screen.fill(clear_color)

    # TOGGLE FULLSCREEN
    keys = pygame.key.get_pressed()
    if keys[pygame.K_TAB]:
        pygame.display.toggle_fullscreen()

    # UPDATE CODE
    for a in active_objs:
        a.update()

    # RENDER YOUR GAME HERE
    area.map.draw(screen)
    for s in sprites:
        s.draw(screen)

    pygame.display.flip()
    # FPS: 1000ms/60s ~ 17
    pygame.time.delay(17)
pygame.quit()
