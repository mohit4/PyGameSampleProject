import os

import pygame as pg
pg.mixer.init()

SOUNDS_DIR = os.path.join("sounds", "adventure_girl")
PLAYER_JUMP_SOUND_PATH = os.path.join(SOUNDS_DIR, "jump.wav")
PLAYER_MELEE_SOUND_PATH = os.path.join(SOUNDS_DIR, "melee.wav")
PLAYER_RUN_SOUND_PATH = os.path.join(SOUNDS_DIR, "run.wav")
PLAYER_SHOOT_SOUND_PATH = os.path.join(SOUNDS_DIR, "shoot.wav")
PLAYER_SLIDE_SOUND_PATH = os.path.join(SOUNDS_DIR, "slide.wav")

player_jump_sound = pg.mixer.Sound(PLAYER_JUMP_SOUND_PATH)
player_melee_sound = pg.mixer.Sound(PLAYER_MELEE_SOUND_PATH)
player_run_sound = pg.mixer.Sound(PLAYER_RUN_SOUND_PATH)
player_shoot_sound = pg.mixer.Sound(PLAYER_SHOOT_SOUND_PATH)
player_slide_sound = pg.mixer.Sound(PLAYER_SLIDE_SOUND_PATH)
