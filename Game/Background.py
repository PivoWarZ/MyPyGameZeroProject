from pgzero.actor import Actor

from Game import Speed_config, Helpers
from Game.Character import Character
from Game.Movable import Movable


class Background(Movable):

    def __init__(self, offsetY):
        self.background = [
            Actor("background/0.png"),
            Actor("background/0.png"),
            Actor("background/1.png"),
            Actor("background/1.png"),
            Actor("background/1.png"),
            Actor("background/2.png"),
            Actor("background/2.png"),
            Actor("background/2.png"),
            Actor("background/0.png"),
            Actor("background/0.png"),
            Actor("background/1.png"),
            Actor("background/1.png"),
            Actor("background/1.png"),
            Actor("background/2.png"),
            Actor("background/2.png"),
            Actor("background/2.png")
        ]

        offsetX = 1920

        for background in self.background:
            background.bottomleft = (offsetX, offsetY)
            offsetX += background.width

    def draw(self):
        for background in self.background:
            background.draw()

    def move(self, direction):
        Helpers.moving(self.move_function, direction, True, False, self.background)

    def move_function(self, movable, direction):
            movable.x -= Character.Speed / Speed_config.Background_speed_modifier * direction