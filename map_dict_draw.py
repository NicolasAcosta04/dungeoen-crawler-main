import pygame
import csv


class Map:  # class is initialized
    def __init__(self, window_surface, level, wall):
        self.window_surface = window_surface
        self.level = level
        self.wall = wall
        self.img_list = []
        self.img = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorTileset.png')
        self.map_tiles = {
            '0': self.img.subsurface(0, (5 * 32), 32, 32),  # floor tile
            '1': self.img.subsurface(32, (5 * 32), 32, 32),  # floor tile
            '2': self.img.subsurface(64, (5 * 32), 32, 32),  # floor tile
            '3': self.img.subsurface(0, (4 * 32), 32, 32),  # floor tile
            '4': self.img.subsurface(32, 32, 32, 32),  # floor tile
            '5': self.img.subsurface(158, 154, 36, 70),  # wall tile
            '6': self.img.subsurface(96, 0, 32, 32)
        }
        self.world_floor = []
        self.world_wall = []  # create empty lists for the wall and floor tiles to be processed separately
        self.floor_list = []
        self.wall_list = []  # creates empty lists for the tiles to be drawn
        self.rows = 20
        self.cols = 25
        self.tiles = 6  # number of rows, columns and tiles are defined with the same values as in the tile editor

    def empty_floor(self):
        for row in range(self.rows):
            r = [-1] * self.cols
            self.world_floor.append(r)  # creates an empty floor file full of -1s

    def empty_wall(self):
        for row in range(self.rows):
            r = [-1] * self.cols
            self.world_wall.append(r)  # creates and empty wall file full of -1s

    def open_floor_file(self):
        with open(f'level{self.level}_data.csv', newline='') as csvfile:  # opens floor file based on self.level
            reader = csv.reader(csvfile, delimiter=',')  # reads the data inbetween commas
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_floor[x][y] = int(tile)
        self.process_data(self.world_floor)  # the data is then sent to the process_data method

    def open_wall_file(self):
        with open(f'wall{self.wall}_data.csv', newline='') as csvfile:  # opens wall file based on self.wall
            reader = csv.reader(csvfile, delimiter=',')  # reads data inbetween commas
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    self.world_wall[x][y] = int(tile)
        self.process_data(self.world_wall)  # the data is then sent to the process_data method

    def process_data(self, data):  # this method takes the data from reading both files and appending them to the
        # correct lists
        for y, row in enumerate(data):  # data is processed row by row
            for x, tile in enumerate(row):  # in every row, each tile number is processed and assigned to the right list
                if 0 <= int(tile) <= 4:  # this is the range of numbers that represent the floor tiles
                    img = self.map_tiles.get(str(tile))
                    img_rect = img.get_rect()  # this line and the lines 063, 063 get the rect of the tile img and the
                    # coordinates of the image
                    img_rect.x = x * 32
                    img_rect.y = y * 32
                    tile_data = (img, img_rect)
                    self.floor_list.append(tile_data)  # each tile that is processed in this if statement is appended to
                    # this list
                if int(tile) == 5:  # this is number that represents the floor tile
                    img = self.map_tiles.get(str(tile))
                    img_rect = img.get_rect()  # 070, 071, 072 get the rect and the coordinates of each tile image
                    img_rect.x = x * 36
                    img_rect.y = y * 70
                    tile_data = (img, img_rect)
                    self.wall_list.append(tile_data)  # each tile that is processed in this if statement is apoended to
                    # this list
                if int(tile) == 6:
                    img = self.map_tiles.get(str(tile))
                    img_rect = img.get_rect()
                    img_rect.x = x * 32
                    img_rect.y = y * 32
                    tile_data = (img, img_rect)
                    self.floor_list.append(tile_data)

    def draw(self):
        for tile in self.floor_list:
            self.window_surface.blit(tile[0], tile[1])  # draws all the tiles in the floor list
        for tile in self.wall_list:
            self.window_surface.blit(tile[0], tile[1]) # draws all the tiles in the wall list
