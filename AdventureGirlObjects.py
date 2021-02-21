import enum

import pygame as pg
from pygame.locals import RLEACCEL
from pygame.locals import K_LEFT
from pygame.locals import K_RIGHT
from pygame.locals import K_SPACE
from pygame.locals import K_z
from pygame.locals import K_x
from pygame.locals import K_a
from pygame.locals import K_q

from animation import PLAYER_IDLE_SEQ
from animation import PLAYER_JUMP_SEQ
from animation import PLAYER_RUN_SEQ
from animation import PLAYER_SLIDE_SEQ
from animation import PLAYER_SHOOT_SEQ
from animation import PLAYER_MELEE_SEQ
from animation import PLAYER_DEAD_SEQ


class State:

    def __init__(self):

        self.state_animation = PLAYER_IDLE_SEQ
        self.state_animation_seq = 0

    def is_state_finished(self):
        if self.state_animation == PLAYER_IDLE_SEQ:
            return True

    def get_state(self):
        current_state = self.state_animation[self.state_animation_seq]
        self.state_animation_seq += 1
        if self.state_animation_seq >= len(self.state_animation):
            self.state_animation = PLAYER_IDLE_SEQ
            self.state_animation_seq = 0
        return current_state


class Direction(enum.Enum):
    LEFT = 1
    RIGHT = 2


class Player(pg.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.state = State()

        self.direction = Direction.RIGHT

        (image_path, position_offset) = self.state.get_state()
        self.surf = pg.image.load(image_path).convert()
        self.surf = pg.transform.scale(self.surf, (236, 200))
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                200,
                400
            )
        )

    def update(self, pressed_keys):
        (image_path, position_offset) = self.state.get_state()
        self.surf = pg.image.load(image_path).convert()
        self.surf = pg.transform.scale(self.surf, (236, 200))
        if self.direction == Direction.LEFT:
            self.surf = pg.transform.flip(self.surf, True, False)
            position_offset = (-1*position_offset[0], position_offset[1])
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)
        self.rect.move_ip(position_offset[0], position_offset[1])

        if pressed_keys[K_LEFT] and self.state.is_state_finished():
            self.direction = Direction.LEFT
            self.state.state_animation = PLAYER_RUN_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_RIGHT] and self.state.is_state_finished():
            self.direction = Direction.RIGHT
            self.state.state_animation = PLAYER_RUN_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_SPACE] and self.state.is_state_finished():
            self.state.state_animation = PLAYER_JUMP_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_z] and self.state.is_state_finished():
            self.state.state_animation = PLAYER_SLIDE_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_x] and self.state.is_state_finished():
            self.state.state_animation = PLAYER_SHOOT_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_a] and self.state.is_state_finished():
            self.state.state_animation = PLAYER_MELEE_SEQ
            self.state.state_animation_seq = 0
        if pressed_keys[K_q] and self.state.is_state_finished():
            self.state.state_animation = PLAYER_DEAD_SEQ
            self.state.state_animation_seq = 0
