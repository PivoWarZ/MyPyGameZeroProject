from pgzero.actor import Actor

from Game import Speed_config
from Game.Character import Character
from Game.Movable import Movable


class Background(Movable):

    def __init__(self, offsetY):
        self.background = [
            Actor("background/background.png"),
            Actor("background/background.png")
        ]

        offsetX = 0

        for background in self.background:
            background.bottomleft = (offsetX, offsetY)
            offsetX += background.width


    def draw(self):
        for background in self.background:
            background.draw()

    def move(self, direction):
        for background in self.background:
            background.x -= Character.Speed / Speed_config.Background_speed_modifier * direction
