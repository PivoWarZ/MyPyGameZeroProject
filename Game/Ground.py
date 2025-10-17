from pgzero.actor import Actor

from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Ground(Movable):

    def __init__(self):

        self.grounds = [
            Actor("ground/road"),
            Actor("ground/road"),
        ]

        self.grass = [
            Actor("ground/grass"),
            Actor("ground/grass"),
        ]

        self.SetStartPosition(self.grounds, self.grass)

    def draw(self):
        self.drawning(self.grass)
        self.drawning(self.grounds)

    @property
    def GetGroundHeight(self):
        return self.grounds[0].height

    def move(self, direction):
        self.moving(self.grounds, direction)
        self.moving(self.grass, direction)

    def moving(self, movables, direction):

        for movable in movables:
            movable.x -= Character.Speed * direction
            if movable.topright[0] < 0:
                max_right = max(actor.right for actor in movables)
                movable.left = max_right

    def drawning(self, actors):
        for actor in actors:
            actor.draw()

    def SetStartPosition(self, *args):

        height = GameWindow.Height
        is_first = True

        for actors in args:
            for actor in actors:

                if is_first:
                    actor.bottomleft = (0, height)
                    is_first = False
                else:
                    max_right = max(index.right for index in actors)
                    actor.bottomleft = (max_right, height)

            is_first = True