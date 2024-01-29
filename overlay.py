import pygame
from settings import *


class Overlay:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        # import
        overlay_path = './graphics/overlay/'
        self.tool_surf = {tool: pygame.image.load(
            f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.tool_box = pygame.image.load(
            f'{overlay_path}tool_box.png').convert_alpha()

    def display(self):

        # tool
        tool_surf = self.tool_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        tool_box_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool box'])

        # tool box
        self.display_surface.blit(self.tool_box, tool_box_rect)
        self.display_surface.blit(tool_surf, tool_rect)
