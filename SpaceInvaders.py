import os
import time

import pygame as pg
from pygame.locals import RLEACCEL
from pygame.locals import K_ESCAPE
from pygame.locals import KEYDOWN
from pygame.locals import QUIT

from SpaceInvaderObjects import Player
from SpaceInvaderObjects import Enemy
from SpaceInvaderObjects import Cloud
from SpaceInvaderObjects import Score

pg.mixer.init()

pg.init()

SOUNDS_DIR = "sounds"
BACKGROUND_MUSIC_PATH = os.path.join(SOUNDS_DIR, "background_music.wav")
EXPLOSION_SOUND_PATH = os.path.join(SOUNDS_DIR, "explosion.mp3")

pg.mixer.music.load(BACKGROUND_MUSIC_PATH)
pg.mixer.music.play(loops=-1)

explosion_sound = pg.mixer.Sound(EXPLOSION_SOUND_PATH)

clock = pg.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
score = Score(SCREEN_WIDTH, SCREEN_HEIGHT)

ADD_ENEMY_EVENT = pg.USEREVENT + 1
pg.time.set_timer(ADD_ENEMY_EVENT, 250)

ADD_CLOUD_EVENT = pg.USEREVENT + 2
pg.time.set_timer(ADD_CLOUD_EVENT, 1000)

enemies = pg.sprite.Group()
clouds = pg.sprite.Group()
all_sprites = pg.sprite.Group()

SPRITES_DIR = "sprites"
PLANE_IMG_PATH = os.path.join(SPRITES_DIR, "explosion.png")

explosion = pg.image.load(PLANE_IMG_PATH).convert()
explosion.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)

running = True

while running:

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADD_ENEMY_EVENT:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADD_CLOUD_EVENT:
            new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pg.key.get_pressed()

    enemies.update()
    clouds.update()

    player.update(pressed_keys)
    score.update()

    screen.fill(pg.color.THECOLORS['skyblue'])

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    screen.blit(player.surf, player.rect)
    screen.blit(score.text, score.rect)

    if pg.sprite.spritecollideany(player, enemies):
        player.kill()
        pg.mixer.music.stop()
        screen.blit(explosion, player.rect)
        pg.display.flip()
        explosion_sound.play()
        time.sleep(2)
        running = False

    pg.display.flip()

    clock.tick(30)

pg.mixer.quit()

pg.quit()
