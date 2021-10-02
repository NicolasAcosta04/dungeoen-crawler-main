import pygame
from player_sprites import *
# player is lagging when map is drawn onto the screen, have no idea what is happening


class Player(pygame.sprite.Sprite):
    def __init__(self, window_surface, player_pos_x, player_pos_y):
        super().__init__()
        self.window_surface = window_surface
        self.player_pos_x = player_pos_x
        self.player_pos_y = player_pos_y
        self.x = player_pos_x
        self.x = player_pos_y
        self.speed = 250
        self.hp = 100

        self.w = False
        self.a = False
        self.s = False
        self.d = False

        self.down_idle = []
        self.up_idle = []
        self.left_idle = []
        self.right_idle = []

        self.down_walk = []
        self.up_walk = []
        self.left_walk = []
        self.right_walk = []

        self.moving = 0

        self.direction = 1

        self.currentFrame = 0
        self.currentAnimation = []
        self.timeSinceFrame = 0
        self.timeBetweenSteps = 1 / 12

    def draw(self, window_surface):
        if self.moving == 0:
            if self.direction == 1:
                self.down_idle = down_idle
                self.currentAnimation = self.down_idle
            if self.direction == 0:
                self.up_idle = up_idle
                self.currentAnimation = self.up_idle
            if self.direction == 2:
                self.left_idle = left_idle
                self.currentAnimation = self.left_idle
            if self.direction == 3:
                self.right_idle = right_idle
                self.currentAnimation = self.right_idle

        elif self.moving == 1:
            if self.direction == 0:
                self.up_walk = up_walk
                self.currentAnimation = self.up_walk
            if self.direction == 1:
                self.down_walk = down_walk
                self.currentAnimation = self.down_walk
            if self.direction == 2:
                self.left_walk = left_walk
                self.currentAnimation = self.left_walk
            if self.direction == 3:
                self.right_walk = right_walk
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
            self.moving = 1
            self.player_pos_y -= self.speed * time_delta
        if self.s:
            self.moving = 1
            self.player_pos_y += self.speed * time_delta
        if self.d:
            self.moving = 1
            self.player_pos_x += self.speed * time_delta
        if self.a:
            self.moving = 1
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
