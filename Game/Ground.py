from pgzero.actor import Actor

from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Ground(Movable):

    def __init__(self):
        height = GameWindow.Height
        self.ground = Actor("ground/road")
        self.grass = Actor("ground/grass")
        self.ground.topleft = (0, height - self.ground.height)
        self.grass.topleft = (0, height - self.grass.height)

    def draw(self):
        self.grass.draw()
        self.ground.draw()

    @property
    def GetGroundHeight(self):
        return self.ground.height

    def move(self, direction):
        self.ground.x -= Character.Speed * direction
        self.grass.x -= Character.Speed * direction