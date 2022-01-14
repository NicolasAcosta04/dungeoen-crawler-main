import pygame
from player_sprites import *


class Player(pygame.sprite.Sprite):  # class is initialized
    def __init__(self, window_surface, player_pos_x, player_pos_y):
        super().__init__()  # inherits methods from pygame.sprite.Sprite
        self.window_surface = window_surface  # takes the window surface from the parameter
        self.player_pos_x = player_pos_x  # takes player coordinates from the parameters
        self.player_pos_y = player_pos_y
        self.speed = 250  # this is how fast the player will move when multiplied by time_delta
        self.hp = 100  # this is the player's health points
        # these are the boolean values for the key variables, that are changed when one of them are held down
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        # these are the empty lists that hold the player idle animation spritesheets when they are assigned them
        self.down_idle = []
        self.up_idle = []
        self.left_idle = []
        self.right_idle = []
        # these are the empty lists that hold the player walking animation spritesheets when they are assigned them
        self.down_walk = []
        self.up_walk = []
        self.left_walk = []
        self.right_walk = []

        self.moving = 0  # this variable will indicate whether the player is moving with 1 being moving and 0 idle

        self.direction = 1  # this says what direction the player is facing with 1: down, 0: up, 2: left and 3: right

        self.currentFrame = 0  # this variable is what frame in the current animation the player is in
        self.currentAnimation = []  # this holds the animation of an action that is being actively performed
        self.timeSinceFrame = 0  # this records the time in which the frame has been animated in
        self.timeBetweenSteps = 1 / 12  # this controls how fast the animations are being drawn

    def draw(self, window_surface):
        if self.moving == 0:  # when the player is not moving
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

        elif self.moving == 1:  # when the player is moving
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

        frame = self.currentAnimation[self.currentFrame]  # local variable is assigned the current animation with the
        # current frame as the index
        window_surface.blit(frame, (self.player_pos_x, self.player_pos_y))  # the frame is drawn onto the screen

    def next_animation(self, event):  # this method helps to clear the current animation list when another action is
        # performed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or pygame.K_s or pygame.K_a or pygame.K_d:
                self.currentAnimation = []
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or pygame.K_s or pygame.K_a or pygame.K_d:
                self.currentAnimation = []

    def next_frame(self):
        self.currentFrame += 1  # frames are drawn one by one
        if self.currentFrame >= len(self.currentAnimation):  # this line resets the animation if the value of the
            # current frame is greater than the number of frames in the animation
            self.currentFrame = 0

    def update(self, time_delta):
        self.timeSinceFrame += time_delta
        if self.timeSinceFrame >= self.timeBetweenSteps:  # if the timeSinceFrame is greater than 1/12, the
            # timeSinceFrame is reset to 0 and the next frame is drawn
            self.timeSinceFrame = 0
            self.next_frame()

        if self.w:  # these statements control how far in pixels the player moves when a movement key is pressed
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

        # if self.player_pos_x <= 0 - 32:
        #     self.player_pos_x += self.speed * time_delta
        # if self.player_pos_x >= 800 +-:
        #     self.player_pos_x -= self.speed * time_delta

    def on_key_press(self, event):  # this method handles events that are triggered when a key is pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # when w, a, s or d are pressed, the player starts moving and the direction is
                # changed base on the key that is pressed.
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

    def on_key_release(self, event):  # this method is like on_key_release, except it handles events that involve a key
        # being released after a key has actuated
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:  # when w, a, s or d are released, the player will stop moving
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
