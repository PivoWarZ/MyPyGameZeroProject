import os

from pgzero.constants import mouse

from Game.GameManager import game_manager
from Game.OnCollisionEntered import OnCollisionEntered
from Game.PlatformManager import PlatforformManager
from Game.SoundManager import SoundManager, sound_manager
from Game.StartScreen import StartScreen

os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun
from Game.Obstructions import Obstructions
from Game.Gravity import Gravity
from Game.Background import Background
from Game.Character import Character
from Game.GameWindow_config import GameWindow
from Game.Ground import Ground
from Game.Mover import Mover
from Game.Sky import Sky
from Game.Sun import Sun

TITLE, WIDTH, HEIGHT = GameWindow().GetWindowParametres

direction = 0
sky = Sky()
ground = Ground()
sun = Sun(sky)

ground_offset = HEIGHT - ground.GetGroundHeight
background = Background(ground_offset)

character = Character(ground_offset)
obstructions = Obstructions(ground_offset)
platform_manager = PlatforformManager()

gravity = Gravity(character)

mover = Mover( sky, ground, background, sun, obstructions, platform_manager )

on_collision_entered = OnCollisionEntered(character, obstructions)


sound_manager.play()
sound_manager.play()

start_screen = StartScreen()



def on_key_down(key):
    if key == key.SPACE:
        character.jump()
def on_mouse_down(pos, button):
    start_screen.on_mouse_down(pos)
    if button == mouse.LEFT:
        character.attack()

def on_key_up(key):

    global direction

    direction = 0

def draw():

    if game_manager.game_state == 0:
        start_screen.draw()

    if game_manager.game_state == 0:
        return

    sky.draw()
    background.draw()
    ground.draw()
    sun.draw()
    obstructions.draw()
    platform_manager.draw()
    character.draw()

def update(dt):

    if game_manager.game_state == 0:
        return

    move_input()

    if (character.can_move(direction)):
        mover.move(direction)

    gravity_objects = ground.GetGround() + platform_manager.get_platforms_actor()
    gravity.tick(gravity_objects)
    character.tick(dt, direction)
    obstructions.tick(dt)
    on_collision_entered.tick()


def move_input():
    global direction

    if keyboard.RIGHT or keyboard.D:
        direction = 1
    elif keyboard.LEFT or keyboard.A:
        direction = -1



pgzrun.go()
