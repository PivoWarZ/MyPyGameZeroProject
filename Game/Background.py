from pgzero.actor import Actor

from Game.Character import Character
from Game.Movable import Movable


class Background(Movable):

    Speed_modifier = 7

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

    def move(self):
        for background in self.background:
            background.x -= Character.Speed / self.Speed_modifier
