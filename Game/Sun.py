from pgzero.actor import Actor

from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Sun(Movable):

    Speed_modifier = 40
    offset = 20

    def __init__(self):
        self.sun = Actor("sun/sun.png")
        self.sun.topright = (GameWindow.Width - self.offset, self.offset)

    def draw(self):
        self.sun.draw()

    def move(self):
        self.sun.x -= Character.Speed / self.Speed_modifier