import pygame


class Character:
    def __init__(self, max_hp, sprite, speed, weapons, cords):
        self.max_hp, self.current_hp = max_hp, max_hp
        self.sprite = pygame.image.load(f"resources/{sprite}")
        self.speed = speed
        self.weapons = weapons
        self.pos_x, self.pos_y = cords

    def render(self, screen):
        screen.fill("black")
        screen.blit(self.sprite, (self.pos_x, self.pos_y))
