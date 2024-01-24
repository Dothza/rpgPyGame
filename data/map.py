import pygame, os
from data.load_image import load_image

TILE_WIDTH = TILE_HEIGHT = 50

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}


def load_level(filename):
    filename = os.path.join("resources", filename)
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.type = tile_type
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x, TILE_HEIGHT * pos_y)
