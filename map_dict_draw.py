import pygame
import map_dict
import csv


class Map:
    def __init__(self, window_surface, level):
        self.window_surface = window_surface
        self.level = level
        self.img_list = []
        self.img = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorTileset.png')
        self.map_tiles = {
            '0': self.img.subsurface(0, (5 * 32), 32, 32),
            '1': self.img.subsurface(32, (5 * 32), 32, 32),
            '2': self.img.subsurface(64, (5 * 32), 32, 32),
            '3': self.img.subsurface(0, (4 * 32), 32, 32),
            '4': self.img.subsurface(32, 32, 32, 32),
            '5': self.img.subsurface(156, 154, 40, 70),
        }
        self.world_floor = []
        self.obstacle_list = []
        self.rows = 20
        self.cols = 25
        self.tiles = 6
        self.tile = 32

    # def load_images(self):
    #     img = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorTileset.png')
    #     self.map_tiles = {
    #         '0': img.subsurface(0, (5 * 32), 32, 32),
    #         '1': img.subsurface(32, (5 * 32), 32, 32),
    #         '2': img.subsurface(64, (5 * 32), 32, 32),
    #         '3': img.subsurface(0, (4 * 32), 32, 32),
    #         '4': img.subsurface(32, 32, 32, 32),
    #         '5': img.subsurface(156, 154, 40, 70),
    #     }
        # self.img_list = []
        # for key, value in self.map_tiles.items():
        #     self.img_list.append(value)

    def empty_floor(self):
        for row in range(self.rows):
            r = [-1] * self.cols
            self.world_floor.append(r)

    def open_file(self):
        with open(f'level{self.level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_floor[x][y] = int(tile)
        self.process_data(self.world_floor)

    def process_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if int(tile) >= 0:
                    # key = self.map_tiles.items()
                    # value = self.map_tiles[key]
                    img = self.map_tiles.get(str(tile))
                    img_rect = img.get_rect()
                    img_rect.x = x * self.tile
                    img_rect.y = y * self.tile
                    tile_data = (img, img_rect)
                    self.obstacle_list.append(tile_data)

    # def process_floor(self, data):
    #     for y, row in enumerate(data):
    #         for x, tile in enumerate(row):
    #             if int(tile) >= 0:
    #                 img = self.img_list[tile]
    #                 img_rect = img.get_rect()
    #                 img_rect.x = x * self.tile
    #                 img_rect.y = y * self.tile
    #                 tile_data = (img, img_rect)
    #                 self.obstacle_list.append(tile_data)

    def draw(self):
        for tile in self.obstacle_list:
            self.window_surface.blit(tile[0], tile[1])
