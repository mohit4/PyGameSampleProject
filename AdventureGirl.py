import pygame as pg
from pygame.locals import K_ESCAPE
from pygame.locals import KEYDOWN
from pygame.locals import QUIT

from AdventureGirlObjects import Player

pg.init()
clock = pg.time.Clock()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

running = True
while running:

    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pg.key.get_pressed()

    screen.fill(pg.color.THECOLORS['black'])

    player.update(pressed_keys)

    screen.blit(player.surf, player.rect)

    pg.display.flip()
    clock.tick(15)

pg.quit()
