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

        self.down_walk = None
        self.up_walk = None
        self.left_walk = None
        self.right_walk = None

        # self.moving = 0

        self.direction = 1

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        # self.up = False
        # self.down = False
        # self.left = False
        # self.right = False
        # self.standing = 1

        self.currentFrame = 0
        self.currentAnimation = []
        self.timeSinceFrame = 0
        self.timeBetweenSteps = 1 / 10

    def player_sprite(self):
        # idle spritesheets

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

        # walking spritesheets

        down_walk = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Down/Png/WarriorDownWalk.png')
        self.down_walk = down_walk.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
             (288, 0, 48, 48), (336, 0, 48, 48)])
        up_walk = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Up/Png/WarriorUpWalk.png')
        self.up_walk = up_walk.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
             (288, 0, 48, 48), (336, 0, 48, 48)])
        left_walk = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Left/Png/WarriorLeftWalk.png')
        self.left_walk = left_walk.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
             (288, 0, 48, 48), (336, 0, 48, 48)])
        right_walk = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Right/Png/WarriorRightWalk.png')
        self.right_walk = right_walk.images_at(
            [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
             (288, 0, 48, 48), (336, 0, 48, 48)])

    def draw(self, window_surface):
        if self.direction == 0 and not self.moving_up:
            self.currentAnimation = self.up_idle
        if self.direction == 0 and self.moving_up:
            self.currentAnimation = self.up_walk

        if self.direction == 1 and not self.moving_down:
            self.currentAnimation = self.down_idle
        if self.direction == 1 and self.moving_down:
            self.currentAnimation = self.down_walk

        if self.direction == 2 and not self.moving_left:
            self.currentAnimation = self.left_idle
        if self.direction == 2 and self.moving_left:
            self.currentAnimation = self.left_walk

        if self.direction == 3 and not self.moving_right:
            self.currentAnimation = self.right_idle
        if self.direction == 3 and self.moving_right:
            self.currentAnimation = self.right_walk

        # if self.direction == 0 and self.moving_up:
        #     self.currentAnimation = self.up_walk
        # if self.direction == 1 and self.moving_down:
        #     self.currentAnimation = self.down_walk
        # if self.direction == 2 and self.moving_left:
        #     self.currentAnimation = self.left_walk
        # if self.direction == 3 and self.moving_right:
        #     self.currentAnimation = self.right_walk

        # if self.moving == 0:
        #     if self.direction == 0:
        #         self.currentAnimation = self.up_idle
        #     elif self.direction == 1:
        #         self.currentAnimation = self.down_idle
        #     elif self.direction == 2:
        #         self.currentAnimation = self.left_idle
        #     elif self.direction == 3:
        #         self.currentAnimation = self.right_idle
        #
        # if self.moving == 1:
        #     if self.direction == 0:
        #         self.currentAnimation = self.up_walk
        #     if self.direction == 1:
        #         self.currentAnimation = self.down_walk
        #     if self.direction == 2:
        #         self.currentAnimation = self.left_walk
        #     if self.direction == 3:
        #         self.currentAnimation = self.right_walk

        frame = self.currentAnimation[self.currentFrame]
        window_surface.blit(frame, (self.player_pos_x, self.player_pos_y))

    def next_frame(self):
        self.currentFrame += 1
        if self.currentFrame >= len(self.currentAnimation):
            self.currentFrame = 0

        # self.currentFrame = 0
        # if self.currentAnimation != self.currentAnimation:
        #     self.currentFrame //= 8

    # def next_animation(self, event):
    #     if event.type == pygame.KEYDOWN:
    #         self.draw()

    def update(self, time_delta):
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:
            self.timeSinceFrame = 0
            self.next_frame()

        # if self.w or self.s or self.a or self.d:
        #     self.timeSinceFrame
        #     self.next_frame()

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
                self.w = True
                self.moving_up = True
                # self.moving = 1
                self.direction = 0
            if event.key == pygame.K_s:
                self.s = True
                self.moving_down = True
                # self.moving = 1
                self.direction = 1
            if event.key == pygame.K_a:
                self.a = True
                self.moving_left = True
                # self.moving = 1
                self.direction = 2
            if event.key == pygame.K_d:
                self.d = True
                self.moving_right = True
                # self.moving = 1
                self.direction = 3

    def on_key_release(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                # self.moving = 0
                self.w = False
                self.moving_up = False
            if event.key == pygame.K_s:
                # self.moving = 0
                self.s = False
                self.moving_down = False
            if event.key == pygame.K_a:
                # self.moving = 0
                self.a = False
                self.moving_left = False
            if event.key == pygame.K_d:
                # self.moving = 0
                self.d = False
                self.moving_right = False
