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

def draw():
    sky.draw()
    background.draw()
    ground.draw()
    sun.draw()
    character.draw()

def update():
    mover.move()




pgzrun.go()
