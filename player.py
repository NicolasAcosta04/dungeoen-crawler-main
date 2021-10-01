import pygame
from player_sprites import *


class Player(pygame.sprite.Sprite):
    def __init__(self, window_surface, player_pos_x, player_pos_y):
        super().__init__()
        self.window_surface = window_surface
        # self.colour = colour
        self.player_pos_x = player_pos_x
        self.player_pos_y = player_pos_y
        # self.player_pos = pygame.math.Vector2(player_pos_x, player_pos_y)
        self.speed = 250
        self.hp = 100

        self.w = False
        self.a = False
        self.s = False
        self.d = False

        self.down_idle = None
        self.up_idle = None
        self.left_idle = None
        self.right_idle = None

        self.down_walk = None
        self.up_walk = None
        self.left_walk = None
        self.right_walk = None

        self.moving = 0

        self.direction = 1

        self.currentFrame = 0
        self.currentAnimation = []
        self.timeSinceFrame = 0
        self.timeBetweenSteps = 1 / 12

    def draw(self, window_surface):
        if self.moving == 0:
            if self.direction == 1:
                self.currentAnimation = down_idle
            if self.direction == 0:
                self.currentAnimation = up_idle
            if self.direction == 2:
                self.currentAnimation = left_idle
            if self.direction == 3:
                self.currentAnimation = right_idle

        elif self.moving == 1:
            if self.direction == 0:
                self.currentAnimation = up_walk
            if self.direction == 1:
                self.currentAnimation = down_walk
            if self.direction == 2:
                self.currentAnimation = left_walk
            if self.direction == 3:
                self.currentAnimation = right_walk

        frame = self.currentAnimation[self.currentFrame]
        window_surface.blit(frame, (self.player_pos_x, self.player_pos_y))

    def next_animation(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or pygame.K_s or pygame.K_a or pygame.K_d:
                self.currentAnimation = []
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or pygame.K_s or pygame.K_a or pygame.K_d:
                self.currentAnimation = []

    def next_frame(self):
        self.currentFrame += 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0

    def update(self, time_delta):
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.timeSinceFrame = 0
            self.next_frame()

        if self.w:
            self.player_pos_y -= self.speed * time_delta
        if self.s:
            self.player_pos_y += self.speed * time_delta
        if self.d:
            self.player_pos_x += self.speed * time_delta
        if self.a:
            self.player_pos_x -= self.speed * time_delta

    def on_key_press(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.next_animation(event)
                self.w = True
                self.moving = 1
                self.currentFrame = 0
                self.direction = 0
            elif event.key == pygame.K_s:
                self.next_animation(event)
                self.s = True
                self.moving = 1
                self.currentFrame = 0
                self.direction = 1
            elif event.key == pygame.K_a:
                self.next_animation(event)
                self.a = True
                self.moving = 1
                self.currentFrame = 0
                self.direction = 2
            elif event.key == pygame.K_d:
                self.next_animation(event)
                self.d = True
                self.moving = 1
                self.currentFrame = 0
                self.direction = 3

    def on_key_release(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.next_animation(event)
                self.w = False
                self.moving = 0
                self.currentFrame = 0
            elif event.key == pygame.K_s:
                self.next_animation(event)
                self.s = False
                self.moving = 0
                self.currentFrame = 0
            elif event.key == pygame.K_a:
                self.next_animation(event)
                self.a = False
                self.moving = 0
                self.currentFrame = 0
            elif event.key == pygame.K_d:
                self.next_animation(event)
                self.d = False
                self.moving = 0
                self.currentFrame = 0
