from pgzero.actor import Actor

from Game import Speed_config, Helpers
from Game.Character import Character
from Game.Movable import Movable


class Sky(Movable):

    def __init__(self):
        self.sky = [
            Actor("sky/day"),
        ]

        self.clouds = [
            Actor("sky/cloud"),
            Actor("sky/cloud"),
            Actor("sky/cloud"),
        ]

        Helpers.set_start_position(0, True, self.sky, self.clouds)

    def draw(self):
        Helpers.drawning(self.sky, self.clouds)

    def move(self, _):
        Helpers.moving(self.move_function, _, False, False, self.clouds)

    def move_function(self, movable, _):
        movable.x -= Character.Speed / Speed_config.Sky_speed_modifier

    def switcher (self, is_day):
        if not is_day:
            self.sky[0].image = "sky/night"
            for cloud in self.clouds:
                cloud.image = "sky/cloudnight"
        else:
            self.sky[0].image = "sky/day"
            for cloud in self.clouds:
                cloud.image = "sky/cloud"
