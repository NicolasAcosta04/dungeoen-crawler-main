import pygame
from spritesheet import *

pygame.display.set_mode((800, 600))
pygame.init()

# idle animations

di = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Down/Png/WarriorDownIdle.png')
down_idle = di.images_at([(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])

ui = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Up/Png/WarriorUpIdle.png')
up_idle = ui.images_at([(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])

li = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Left/Png/WarriorLeftIdle.png')
left_idle = li.images_at([(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])

ri = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Right/Png/WarriorRightIdle.png')
right_idle = ri.images_at([(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48)])

# walking animations

dw = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Down/Png/WarriorDownWalk.png')
down_walk = dw.images_at(
    [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
     (288, 0, 48, 48), (336, 0, 48, 48)])

uw = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Up/Png/WarriorUpWalk.png')
up_walk = uw.images_at(
    [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
     (288, 0, 48, 48), (336, 0, 48, 48)])

lw = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Left/Png/WarriorLeftWalk.png')
left_walk = lw.images_at(
    [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
     (288, 0, 48, 48), (336, 0, 48, 48)])

rw = SpriteSheet('Foozle_2DC0009_Lucifer_Warrior_Pixel_Art/Right/Png/WarriorRightWalk.png')
right_walk = rw.images_at(
    [(0, 0, 48, 48), (48, 0, 48, 48), (96, 0, 48, 48), (144, 0, 48, 48), (192, 0, 48, 48), (240, 0, 48, 48),
     (288, 0, 48, 48), (336, 0, 48, 48)])
