import pygame, sys, os
from data.load_image import load_image

WIDTH, HEIGHT = (1920, 1080)

buttons = pygame.sprite.Group()

music = pygame.mixer.music.load(os.path.join("resources", "music.mp3"))
pygame.mixer.music.play(-1)

font = pygame.font.Font(None, 36)


class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, func, *groups):
        super().__init__(*groups)
        self.image = image
        self.func = func
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def clicked(self, name=None):
        self.func(name)


def terminate():
    pygame.quit()
    sys.exit()


def play(main):
    background = pygame.sprite.Sprite(buttons)
    background.image = load_image("kavkaz.png")
    background.rect = background.image.get_rect().move(0, 0)
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = screen.get_size()
    level_1_text = font.render("Уровень 1", 1, (0, 0, 255))
    level_2_text = font.render("Уровень 2", 1, (0, 0, 255))
    level_3_text = font.render("Уровень 3", 1, (0, 0, 255))
    level_1_but = Button(load_image("play_but.png"), (WIDTH // 3), 10, main, buttons)
    level_2_but = Button(load_image("play_but.png"), (WIDTH // 3), 410, main, buttons)
    level_3_but = Button(load_image("play_but.png"), (WIDTH // 3), 810, main, buttons)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(level_1_but.rect.x, level_1_but.rect.x + level_1_but.image.get_size()[0]):
                    for y in range(level_1_but.rect.y, level_1_but.rect.y + level_1_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            level_1_but.clicked("level_1.txt")
                for x in range(level_2_but.rect.x, level_2_but.rect.x + level_2_but.image.get_size()[0]):
                    for y in range(level_2_but.rect.y, level_2_but.rect.y + level_2_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            level_2_but.clicked("level_2.txt")
                for x in range(level_3_but.rect.x, level_3_but.rect.x + level_3_but.image.get_size()[0]):
                    for y in range(level_3_but.rect.y, level_3_but.rect.y + level_3_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            level_3_but.clicked("level_3.txt")
            elif event.type == pygame.VIDEORESIZE:
                cur_size = event.size
        buttons.draw(virtual_screen)
        virtual_screen.blit(level_1_text, (WIDTH // 3, 0))
        virtual_screen.blit(level_2_text, (WIDTH // 3, 350))
        virtual_screen.blit(level_3_text, (WIDTH // 3, 750))
        scaled_screen = pygame.transform.scale(virtual_screen, cur_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()


def menu(main):
    background = pygame.sprite.Sprite(buttons)
    background.image = load_image("kavkaz.png")
    background.rect = background.image.get_rect().move(0, 0)
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = screen.get_size()
    play_but = Button(load_image("play_but.png"), (WIDTH // 3), 10, play, buttons)
    exit_but = Button(load_image("exit_but.png"), (WIDTH // 3), 810, terminate, buttons)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(play_but.rect.x, play_but.rect.x + play_but.image.get_size()[0]):
                    for y in range(play_but.rect.y, play_but.rect.y + play_but.image.get_size()[1]):
                        if (x, y) == event.pos:
                            play_but.clicked(main)
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
