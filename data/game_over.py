import pygame
from data.load_image import load_image


class End(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("gameover.png")
        self.speed = 200
        self.x = -600
        self.y = 0

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x < 0:
            self.x += self.speed
