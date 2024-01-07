import pygame

clock = pygame.time.Clock()


class Character(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.frames = []
        self.speed = 5
        self.x, self.y = pos_x, pos_y
        self.cut(image, 4, 4)
        self.dir = 0
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(pos_x, pos_y)

    def cut(self, sheet, col, row):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // col,
                                sheet.get_height() // row)
        for j in range(col):
            frames_col = []
            for i in range(row):
                frame_location = (self.rect.w * i, self.rect.h * j)
                frames_col.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
            self.frames.append(frames_col)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -self.speed)
            self.dir = 3
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.dir])

        if keys[pygame.K_a]:
            self.rect = self.rect.move(-self.speed, 0)
            self.dir = 1
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.dir])

        if keys[pygame.K_d]:
            self.rect = self.rect.move(self.speed, 0)
            self.dir = 2
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.dir])

        if keys[pygame.K_s]:
            self.rect = self.rect.move(0, self.speed)
            self.dir = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.frames[self.dir])

        if not any(keys):
            self.cur_frame = 1
        self.image = self.frames[self.dir][self.cur_frame]
        clock.tick(30)
