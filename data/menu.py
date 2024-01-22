import pygame, sys

WIDTH, HEIGHT = (600, 300)


class Button(pygame.sprite.Sprite):
    def __init__(self, image, *groups):
        super().__init__(*groups)
        self.image = image


def terminate():
    pygame.quit()
    sys.exit()


def menu():
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = screen.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        scaled_screen = pygame.transform.scale(virtual_screen, cur_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()
