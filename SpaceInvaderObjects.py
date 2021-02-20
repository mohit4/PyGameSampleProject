import os
import random

import pygame as pg
from pygame.locals import RLEACCEL
from pygame.locals import K_UP
from pygame.locals import K_DOWN
from pygame.locals import K_LEFT
from pygame.locals import K_RIGHT

SPRITES_DIR = "sprites"
FONTS_DIR = "fonts"
PLANE_IMG_PATH = os.path.join(SPRITES_DIR, "plane1.png")
MISSILE_IMG_PATH = os.path.join(SPRITES_DIR, "missile.png")
CLOUD_IMG_PATH = os.path.join(SPRITES_DIR, "cloud.png")

AVENGERS_FONT_PATH = os.path.join(FONTS_DIR, "heroesassembleexpandital.ttf")


class Score(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(Score, self).__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.score = 0

        self.font = pg.font.Font(AVENGERS_FONT_PATH, 20)
        self.text = self.font.render("Score : " + str(self.score), True, pg.color.THECOLORS['tomato'],
                                     pg.color.THECOLORS['skyblue'])
        self.rect = self.text.get_rect(
            center=(
                80, 20
            )
        )

    def update(self):
        self.score += 1
        self.text = self.font.render("Score : " + str(self.score), True, pg.color.THECOLORS['tomato'],
                                     pg.color.THECOLORS['skyblue'])
        self.rect = self.text.get_rect(
            center=(
                80, 20
            )
        )


class Player(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.surf = pg.image.load(PLANE_IMG_PATH).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                20,
                self.screen_height/2
            )
        )

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height


class Enemy(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(Enemy, self).__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.surf = pg.image.load(MISSILE_IMG_PATH).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20, self.screen_width + 100),
                random.randint(0, self.screen_height)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(Cloud, self).__init__()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.surf = pg.image.load(CLOUD_IMG_PATH).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20, self.screen_width + 100),
                random.randint(0, self.screen_height)
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
