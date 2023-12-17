import pygame

from data.load_image import load_image


class Character(pygame.sprite.Sprite):
    image = load_image("enemy_01.png")

    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = Character.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
