from pgzero.actor import Actor

from Game import Speed_config, Helpers
from Game.Character import Character
from Game.Movable import Movable


class Sky(Movable):

    def __init__(self):
        self.sky = [
            Actor("sky/day"),
        ]

        self.cloud = [
            Actor("sky/cloud"),
            Actor("sky/cloud"),
            Actor("sky/cloud"),
        ]

        Helpers.set_start_position(0, True, self.sky, self.cloud)

    def draw(self):
        Helpers.drawning(self.sky, self.cloud)

    def move(self, _):
        Helpers.moving(self.move_function, _, False, self.cloud)

    def move_function(self, movable, _):
        movable.x -= Character.Speed / Speed_config.Sky_speed_modifier
