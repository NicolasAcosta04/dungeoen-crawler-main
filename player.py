import pygame
from spritesheet import *

TIMER = pygame.time.Clock()


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

        self.direction = 1
        self.standing = 0

        self.standing = None
        self.currentFrame = 0
        self.currentAnimation = []
        self.timeSinceFrame = 0
        self.timeBetweenSteps = 1/5

    def player_sprite(self):
        down_idle = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Down/Png/WarriorDownIdle.png')
        self.down_idle = down_idle.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])
        up_idle = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Up/Png/WarriorUpIdle.png')
        self.up_idle = up_idle.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])
        left_idle = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Left/Png/WarriorLeftIdle.png')
        self.left_idle = left_idle.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])
        right_idle = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Right/Png/WarriorRightIdle.png')
        self.right_idle = right_idle.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])

        # self.standing = self.down_idle[0]

    def draw(self, window_surface):
        # player_rect = pygame.Rect(self.player_pos_x, self.player_pos_y, 48, 48)
        # pygame.draw.rect(self.window_surface, self.colour, player_rect)
        if self.direction == 0:
            self.currentAnimation = self.up_idle
        if self.direction == 1:
            self.currentAnimation = self.down_idle
        if self.direction == 2:
            self.currentAnimation = self.left_idle
        if self.direction == 3:
            self.currentAnimation = self.right_idle
        frame = self.currentAnimation[self.currentFrame]
        window_surface.blit(frame, (self.player_pos_x, self.player_pos_y))

    def next_frame(self):
        self.currentFrame += 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0
        # if self.direction == 3:
        #     self.player_pos_x += self.speed * time_delta
        # if self.direction == 2:
        #     self.player_pos_x -= self.speed * time_delta
        # if self.direction == 0:
        #     self.player_pos_y -= self.speed * time_delta
        # if self.direction == 1:
        #     self.player_pos_y += self.speed * time_delta

    def update(self, time_delta):
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.timeSinceFrame = 0
            self.next_frame()
            # self.timeSinceFrame -= self.timeBetweenSteps
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
                self.direction = 0
                self.w = True
            if event.key == pygame.K_s:
                self.direction = 1
                self.s = True
            if event.key == pygame.K_a:
                self.direction = 2
                self.a = True
            if event.key == pygame.K_d:
                self.direction = 3
                self.d = True

    def on_key_release(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.w = False
            if event.key == pygame.K_s:
                self.s = False
            if event.key == pygame.K_a:
                self.a = False
            if event.key == pygame.K_d:
                self.d = False
