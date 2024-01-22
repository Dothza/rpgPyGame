import pygame
import sys, random, math
from data.load_image import load_image
from data.map import Tile, load_level
from data.characters import Character, EnemyFireball, Fireball, Enemy
from data.game_over import End
from data.menu import menu

WIDTH, HEIGHT = (600, 300)
FPS = 20
TICK = pygame.USEREVENT + 1
TILE_WIDTH = TILE_HEIGHT = 50

all_sprites = pygame.sprite.Group()
characters = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fireballs = pygame.sprite.Group()
enemy_fireballs = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls = pygame.sprite.Group()

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

player_image = load_image('char.png')


def enemy_generate(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            n = random.randrange(len(level[y]))
            if level[y][n] == ".":
                enemy = Enemy(load_image("enemy.png"), (n * TILE_WIDTH) + (TILE_WIDTH // 2),
                              (level.index(level[y]) * TILE_HEIGHT) + (TILE_HEIGHT // 2), all_sprites, enemies,
                              characters)
                return enemy


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, all_sprites, tiles_group)
            elif level[y][x] == '#':
                Tile('wall', x, y, all_sprites, tiles_group, walls)
            elif level[y][x] == '@':
                Tile('empty', x, y, all_sprites, tiles_group)
                new_player = Character(load_image("char.png"),
                                       (level[y].index("@") * TILE_WIDTH) + (TILE_WIDTH // 2),
                                       (level.index(level[y]) * TILE_HEIGHT) + (TILE_HEIGHT // 2),
                                       all_sprites, characters)
    return new_player, x, y


def is_detected(cord_x, cord_y, char_cord_x, char_cord_y):
    if cord_x >= 700:
        return False
    else:
        x_border1 = cord_x - 200
        x_border2 = cord_x + 200
        y_border_1 = cord_y - 200
        y_border_2 = cord_y + 200
        if x_border1 <= char_cord_x <= x_border2 and y_border_1 <= char_cord_y <= y_border_2:
            return True


def terminate():
    pygame.quit()
    sys.exit()


def main():
    global WIDTH, HEIGHT
    kills = 0
    end = None
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    WIDTH, HEIGHT = (1920, 1080)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = (1920, 1080)
    WIDTH, HEIGHT = (600, 300)
    char, level_x, level_y = generate_level(load_level('level_2.txt'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and char.hp > 0:
                if char.dir == 0:
                    Fireball(load_image("fireball.png"), char.rect.x - (char.image.get_size()[0] // 2),
                             char.rect.y - (char.image.get_size()[0] // 2), char.dir, all_sprites, fireballs)
                elif char.dir == 1:
                    Fireball(load_image("fireball.png"), char.rect.x - (4 * char.image.get_size()[0]),
                             char.rect.y - (char.image.get_size()[0] // 2), char.dir, all_sprites, fireballs)
                elif char.dir == 2:
                    Fireball(load_image("fireball.png"), char.rect.x + (char.image.get_size()[0] // 4),
                             char.rect.y - (char.image.get_size()[0] // 2), char.dir, all_sprites, fireballs)
                elif char.dir == 3:
                    Fireball(load_image("fireball.png"), char.rect.x - (char.image.get_size()[0] // 2),
                             char.rect.y - (4 * char.image.get_size()[0]), char.dir, all_sprites, fireballs)
            elif event.type == TICK:
                end.move()
        if random.randrange(5) == random.randrange(70):
            enemy_generate(load_level('level_2.txt'))
        if pygame.sprite.spritecollideany(char, enemy_fireballs):
            char.hp -= 15
        old_cords = {}
        for i in characters:
            old_cords[i] = (i.rect.x, i.rect.y)

        for i in enemies:
            i.update(char.rect.x, char.rect.y, is_detected(i.rect.x, i.rect.y, char.rect.x, char.rect.y), tiles_group,
                     TILE_WIDTH, TILE_HEIGHT)
            if is_detected(i.rect.x, i.rect.y, char.rect.x, char.rect.y) and random.randrange(
                    5) == random.randrange(7) and not end:
                EnemyFireball(load_image("fireball_enemy.png"), i.rect.x, i.rect.y, i.dir, all_sprites,
                              enemy_fireballs)
            if pygame.sprite.spritecollideany(i, fireballs):
                i.hp -= 25

        for i in fireballs:
            if pygame.sprite.spritecollideany(i, walls):
                i.kill()
        for i in enemy_fireballs:
            if pygame.sprite.spritecollideany(i, walls):
                i.kill()

        for i in all_sprites:
            try:
                if i.hp <= 0 and isinstance(i, Enemy):
                    i.kill()
                    kills += 1
                elif i.hp <= 0 and isinstance(i, Character):
                    for j in all_sprites:
                        j.kill()
                    end = End()
                    pygame.time.set_timer(TICK, 100)
            except AttributeError:
                pass
        enemy_fireballs.update()
        fireballs.update()
        char.update()
        for i in characters:
            if pygame.sprite.spritecollideany(i, walls):
                i.rect.x = old_cords[i][0]
                i.rect.y = old_cords[i][1]
        virtual_screen.fill((0, 0, 0))
        all_sprites.draw(virtual_screen)
        characters.draw(virtual_screen)
        if isinstance(end, End):
            end.render(virtual_screen)
            if end.x == 0:
                text = font.render(f"Убийства: {kills}", 1, (180, 0, 0))
                virtual_screen.blit(text, (WIDTH // 2, HEIGHT // 2))
        scaled_screen = pygame.transform.scale(virtual_screen, cur_size)
        screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    sys.exit(menu(main))
