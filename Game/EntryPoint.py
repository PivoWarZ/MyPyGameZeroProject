import os

from Game.Gravity import Gravity

os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun
from Game.Background import Background
from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Ground import Ground
from Game.Mover import Mover
from Game.Sky import Sky
from Game.Sun import Sun

TITLE, WIDTH, HEIGHT = GameWindow().GetWindowParametres

sky = Sky()
ground = Ground()

background_offset = HEIGHT - ground.GetGroundHeight
background = Background(background_offset)

sun = Sun()

character = Character(background_offset)

mover = Mover( sky, ground, background, sun)

direction = 0

gravity = Gravity(ground.GetGround(), character.character())

def on_key_down(key):
    if key == key.SPACE:
        character.jump()

def on_key_up(key):

    global direction

    direction = 0

def draw():
    sky.draw()
    background.draw()
    ground.draw()
    sun.draw()
    character.draw()

def update():
    character.tick()
    move_input()
    mover.move(direction)
    gravity.tick()


def move_input():
    global direction

    if keyboard.RIGHT:
        direction = 1
    elif keyboard.LEFT:
        direction = -1



pgzrun.go()
