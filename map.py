import pygame
import csv


class Map:
    def __init__(self, window_surface, level):
        self.obstacle_list = []

        self.window_surface = window_surface
        self.rows = 20
        self.cols = 25
        self.tile_size = 32
        self.tile_types = 4
        self.level = level
        self.r = 0
        self.world_data = []
        self.img_list = []

    def load_images(self):
        self.img_list = []
        for x in range(self.tile_types):
            img = pygame.image.load(f'Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/tile/{x}.png').convert_alpha()
            img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
            self.img_list.append(img)

    def empty_level(self):
        for row in range(self.rows):
            r = [-1] * self.cols
            self.world_data.append(r)

    def open_file(self):
        with open(f'level{self.level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_data[x][y] = int(tile)

    def process_data(self, data):
        #  iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = self.img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * self.tile_size
                    img_rect.y = y * self.tile_size
                    tile_data = (img, img_rect)
                    if 0 <= tile <= 3:
                        self.obstacle_list.append(tile_data)

    def draw(self):
        self.process_data(self.world_data)
        for tile in self.obstacle_list:
            self.window_surface.blit(tile[0], tile[1])

