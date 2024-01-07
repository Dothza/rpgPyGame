import pygame
import sys
from data.load_image import load_image
from data.characters import Character
from data.characters import Fireball

SIZE_WINDOW = (800, 600)

all_sprites = pygame.sprite.Group()

char = Character(load_image("char.png"), 100, 100, all_sprites)


def terminate():
    pygame.quit()
    sys.exit()


def main():
    screen = pygame.display.set_mode(SIZE_WINDOW)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        char.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    sys.exit(main())
