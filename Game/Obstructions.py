from pgzero.actor import Actor

from Game import Helpers
from Game.Character import Character
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Obstructions(Movable):
    def __init__(self, positionY):
        self.obstructions = [
            Actor("obstructions/cactus.png")
        ]

        self.obstructions[0].midbottom = (GameWindow.Width / 2, positionY)

    def draw(self):
        self.obstructions[0].draw()

    def move(self, direction):
        Helpers.moving(self.move_function, direction, False, True, self.obstructions)

    def move_function(self, movable, direction):
            movable.x -= Character.Speed * direction

    def get_obstructions(self):
        return self.obstructions

