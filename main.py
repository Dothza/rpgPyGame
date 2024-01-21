import pygame
import sys, random
from data.load_image import load_image
from data.characters import Character, EnemyFireball, Fireball, Enemy
from data.game_over import End


WIDTH, HEIGHT = (600, 300)
FPS = 30
TICK = pygame.USEREVENT + 1

all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
fireballs = pygame.sprite.Group()
enemy_fireballs = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
enemy = Enemy(load_image("enemy.png"), 50, 50, all_sprites, enemies)

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('char.png')

tile_width = tile_height = 50

player = None

def load_level(filename):
    filename = "resources/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

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

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Character(load_image("char.png"), 350, 200, all_sprites, player_sprites)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y

def terminate():
    pygame.quit()
    sys.exit()


def main():
    kills = 0
    end = None
    virtual_screen = pygame.Surface((WIDTH, HEIGHT))
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    cur_size = screen.get_size()
    char, level_x, level_y = generate_level(load_level('level_1.txt'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and char.hp >= 0:
                Fireball(load_image("fireball.png"), char.rect.x,
                         char.rect.y, char.dir, all_sprites, fireballs)
            elif event.type == pygame.VIDEORESIZE:
                cur_size = event.size
            elif event.type == TICK:
                end.move()

        for i in enemies:
            i.update(char.rect.x, char.rect.y, is_detected(enemy.rect.x, enemy.rect.y, char.rect.x, char.rect.y))
        if is_detected(enemy.rect.x, enemy.rect.y, char.rect.x, char.rect.y) and random.randrange(
                5) == random.randrange(5) and not end:
            EnemyFireball(load_image("fireball_enemy.png"), enemy.rect.x, enemy.rect.y, enemy.dir, all_sprites,
                          enemy_fireballs)
        if pygame.sprite.spritecollideany(char, enemy_fireballs):
            char.hp -= 15
        if pygame.sprite.spritecollideany(enemy, fireballs):
            enemy.hp -= 25
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
        virtual_screen.fill((0, 0, 0))
        all_sprites.draw(virtual_screen)
        enemies.draw(virtual_screen)
        player_sprites.draw(virtual_screen)

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
    sys.exit(main())
