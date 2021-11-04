import pygame

# pygame.display.set_mode((800, 640))
# pygame.init()
img = pygame.image.load('Foozle_2DT0002_Lucifer_Tileset_1_Pixel_Art/Png/InteriorTileset.png')

map_tiles = {
    '001': img.subsurface(0, (5 * 32), 32, 32),
    '002': img.subsurface(32, (5 * 32), 32, 32),
    '003': img.subsurface(64, (5 * 32), 32, 32),
    '004': img.subsurface(0, (4 * 32), 32, 32),
    '005': img.subsurface(32, 32, 32, 32),
    '006': img.subsurface(156, 154, 40, 70),
}
