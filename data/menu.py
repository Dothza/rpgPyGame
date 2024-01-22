import pygame, sys, os
from data.load_image import load_image

WIDTH, HEIGHT = (1920, 1080)

buttons = pygame.sprite.Group()

music = pygame.mixer.music.load(os.path.join("resources", "music.mp3"))
pygame.mixer.music.play(-1)


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, func, *groups):
        super().__init__(*groups)
        self.image = image
        self.func = func
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def clicked(self):
        self.func()


def terminate():
    pygame.quit()
    sys.exit()


def main():
    print("Playing")


def menu(play):
    background = pygame.sprite.Sprite(buttons)
    background.image = load_image("kavkaz.png")
    background.rect = background.image.get_rect().move(0, 0)
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = screen.get_size()
    play_but = Button(load_image("play_but.png"), (WIDTH // 3), 10, play, buttons)
    exit_but = Button(load_image("exit_but.png"), (WIDTH // 3), 610, terminate, buttons)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(play_but.rect.x, play_but.rect.x + play_but.image.get_size()[0]):
                    for y in range(play_but.rect.y, play_but.rect.y + play_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            play_but.clicked()
                for x in range(exit_but.rect.x, exit_but.rect.x + exit_but.image.get_size()[0]):
                    for y in range(exit_but.rect.y, exit_but.rect.y + exit_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            exit_but.clicked()
            elif event.type == pygame.VIDEORESIZE:
                cur_size = event.size
        buttons.draw(virtual_screen)
        scaled_screen = pygame.transform.scale(virtual_screen, cur_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()
