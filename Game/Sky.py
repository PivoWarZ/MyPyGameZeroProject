from pgzero.actor import Actor

from Game import Speed_config
from Game.Character import Character
from Game.Movable import Movable


class SpeedConfig_S:
    pass


class Sky(Movable):

    def __init__(self):
        self.sky = Actor("sky/day")
        self.cloud = Actor("sky/cloud")

    def draw(self):
        self.sky.draw()
        self.cloud.draw()

    def move(self, _):
        self.cloud.x -= Character.Speed/Speed_config.Sky_speed_modifier
