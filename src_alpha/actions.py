import pygame


def jump(self):
    keys = pygame.key.get_pressed()

    if self.directions.x < 0 and keys[pygame.K_SPACE]:
        self.status = 'jump_left'
    elif keys[pygame.K_SPACE] and self.directions == [1]:
        self.status = 'jump_right'
