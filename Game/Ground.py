from pgzero.actor import Actor

from Game import Helpers
from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Ground(Movable):

    def __init__(self):

        height = GameWindow.Height

        self.grounds = [
            Actor("ground/road"),
            Actor("ground/road"),
            Actor("ground/road")
        ]

        self.grass = [
            Actor("ground/grass"),
            Actor("ground/grass"),
            Actor("ground/grass")
        ]

        Helpers.set_start_position(height, False, self.grounds, self.grass)

    def draw(self):
        self.drawning(self.grass)
        self.drawning(self.grounds)

    @property
    def GetGroundHeight(self):
        return self.grounds[0].height

    def move(self, direction):
        Helpers.moving(self.move_function, direction, True, self.grounds, self.grass)

    def drawning(self, actors):
        for actor in actors:
            actor.draw()

    def move_function (self, movable, direction):
        movable.x -= Character.Speed * direction