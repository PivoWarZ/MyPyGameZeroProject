import os

from pgzero.constants import mouse

from Game.OnCollisionEntered import OnCollisionEntered

os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun
from Game.Obstructions import Obstructions
from Game.Gravity import Gravity
from Game.Background import Background
from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Ground import Ground
from Game.Mover import Mover
from Game.Sky import Sky
from Game.Sun import Sun

TITLE, WIDTH, HEIGHT = GameWindow().GetWindowParametres

direction = 0
sky = Sky()
ground = Ground()
sun = Sun()

ground_offset = HEIGHT - ground.GetGroundHeight
background = Background(ground_offset)

character = Character(ground_offset)
obstructions = Obstructions(ground_offset)

gravity = Gravity(ground.GetGround(), character)
mover = Mover( sky, ground, background, sun, obstructions)

on_collision_entered = OnCollisionEntered(obstructions.get_obstructions())


def on_key_down(key):
    if key == key.SPACE:
        character.jump()
def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        character.attack()
        print("attack")

def on_key_up(key):

    global direction

    direction = 0

def draw():
    sky.draw()
    background.draw()
    ground.draw()
    sun.draw()
    character.draw()
    obstructions.draw()

def update(dt):
    move_input()

    if (character.can_move()):
        mover.move(direction)

    gravity.tick()
    character.tick(dt, direction)
    on_collision_entered.tick(character.get_current_actor())


def move_input():
    global direction

    if keyboard.RIGHT:
        direction = 1
    elif keyboard.LEFT:
        direction = -1



pgzrun.go()
