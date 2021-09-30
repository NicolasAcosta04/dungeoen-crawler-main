import pygame


class Map:
    def __init__(self, window_surface, tile_size):
        self.window_surface = window_surface
        self.floor_tile = None
        self.floor_tile_cracked = None
        self.wall_tile = None
        self.wall_tile_full = None
        self.tile_map = []
        self.map_width = 0
        self.map_height = 0
        self.tile_size = tile_size

    def load_tiles(self):
        self.floor_tile = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorTile.png')
        self.floor_tile_cracked = pygame.image.load(
            'Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorCrackedTile.png')
        self.wall_tile = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorWallTile.png')
        self.wall_tile_full = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorWallFull.png')

        self.tile_map = [
            [self.floor_tile, self.floor_tile, self.floor_tile, self.floor_tile]

        ]

        self.map_width = len(self.tile_map)
        self.map_height = len(self.tile_map[0])

    def draw(self):
        for row in range(len(self.tile_map)):
            for column in range(len(self.tile_map[row])):
                self.window_surface.blit(self.tile_map[row][column], column * self.tile_size, row * self.tile_size)
