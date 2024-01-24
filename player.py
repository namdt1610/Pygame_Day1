import pygame
from settings import *
from support import *
from timer import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

        # graphics setup
        self.status = 'idle_left'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # movement atributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.actions = set()

        # animations attributes
        self.animation_speed = 0.1
        self.current_time = 0

        # timer
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200)
        }

        # tools
        self.tools = ['axe', 'sword', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]

    def use_tool(self):
        self.selected_tool

    def import_assets(self):
        self.animations = {'axe_left': [], 'axe_right': [], 'rifle_left': [], 'rifle_right': [],
                           'climb': [], 'craft': [], 'death': [],
                           'hurt': [], 'idle_left': [], 'idle_right': [], 'jump_left': [], 'jump_right': [],
                           'push': [], 'run': [], 'walk_right': [], 'walk_left': []}

        for animation in self.animations.keys():
            full_path = './graphics/Woodcutter/' + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()

        if not self.timers['tool use'].active:
            # directions
            # left direction
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.status = 'walk_left'
                self.direction.x = -1
            # right direction
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.status = 'walk_right'
                self.direction.x = 1
            else:
                self.direction.x = 0

            # up-down-right direction
            # up-right
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and '_right' in self.status:
                self.status = 'walk_right'
                self.direction.y = -1
            # down-right
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and '_right' in self.status:
                self.status = 'walk_right'
                self.direction.y = 1
            # up-down-left direction
            # up-left
            elif (keys[pygame.K_UP] or keys[pygame.K_w]) and '_left' in self.status:
                self.status = 'walk_left'
                self.direction.y = -1
            # down-left
            elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and '_left' in self.status:
                self.status = 'walk_left'
                self.direction.y = 1
            else:
                self.direction.y = 0

            # tool use
            if mouse_buttons[0]:
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0

            # change tool
            if keys[pygame.K_q] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                self.tool_index += 1
                self.tool_index = self.tool_index if self.tool_index < len(
                    self.tools) else 0
                print(self.tool_index)
                self.selected_tool = self.tools[self.tool_index]

    def get_status(self):
        # idle
        if self.direction.magnitude() == 0:
            self.status = 'idle_' + self.status.split('_')[1]

        # tool use
        if self.timers['tool use'].active:
            self.status = self.selected_tool + '_' + self.status.split('_')[1]

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, deltaTime):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * deltaTime
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * deltaTime
        self.rect.centery = self.pos.y

    def animate(self, deltaTime):
        self.current_time += deltaTime

        if self.current_time > self.animation_speed:
            self.frame_index = (self.frame_index +
                                1) % len(self.animations[self.status])
            self.image = self.animations[self.status][self.frame_index]
            self.current_time = 0

    def update(self, deltaTime):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(deltaTime)
        self.animate(deltaTime)
