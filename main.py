import pygame
import sys

SIZE_WINDOW = (800, 600)


def terminate():
    pygame.quit()
    sys.exit()


def main():
    screen = pygame.display.set_mode(SIZE_WINDOW)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()


if __name__ == "__main__":
    sys.exit(main())
