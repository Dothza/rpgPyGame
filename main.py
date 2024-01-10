import pygame
import sys
from data.load_image import load_image
from data.characters import Character
from data.characters import Fireball
from data.characters import Enemy

SIZE_WINDOW = (800, 600)
all_sprites = pygame.sprite.Group()
fireballs = pygame.sprite.Group()

clock = pygame.time.Clock()
char = Character(load_image("char.png"), 100, 100, all_sprites)
enemy = Enemy(load_image("enemy.png"), 50, 50, all_sprites)


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
        enemy.update()
        fireballs.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    sys.exit(main())
