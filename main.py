import pygame
import sys
from data.load_image import load_image
from data.characters import Character, Enemy_Fireball
from data.characters import Fireball
from data.characters import Enemy
import random

SIZE_WINDOW = (800, 600)
all_sprites = pygame.sprite.Group()
fireballs = pygame.sprite.Group()

clock = pygame.time.Clock()
char = Character(load_image("char.png"), 350, 500, all_sprites)
enemy = Enemy(load_image("enemy.png"), 50, 50, all_sprites)


def is_detected(cord_x, cord_y, char_cord_x, char_cord_y):
    if cord_x >= 700:
        detection = False
        return detection
    else:
        x_border1 = cord_x - 200
        x_border2 = cord_x + 200
        y_border_1 = cord_y - 200
        y_border_2 = cord_y + 200
        if x_border1 <= char_cord_x <= x_border2 and y_border_1 <= char_cord_y <= y_border_2:
            detection = True
            return detection


def terminate():
    pygame.quit()
    sys.exit()


def main():
    screen = pygame.display.set_mode(SIZE_WINDOW)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Fireball(load_image("fireball.png"), char.rect.x,
                         char.rect.y, char.dir, all_sprites, fireballs)

        char.update()
        enemy.update(char.rect.x, char.rect.y, is_detected(enemy.rect.x, enemy.rect.y, char.rect.x, char.rect.y))
        if is_detected(enemy.rect.x, enemy.rect.y, char.rect.x, char.rect.y) and random.randint(1, 4) == 3:
            Enemy_Fireball(load_image("fireball_enemy.png"), enemy.rect.x, enemy.rect.y, enemy.dir, all_sprites,
                           fireballs)
            clock.tick()
        fireballs.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    sys.exit(main())
