from pgzero.actor import Actor

from Game.Character import Character
from Game.Movable import Movable


class Sky(Movable):

    Speed_modifier = 20

    def __init__(self):
        self.sky = Actor("sky/day")
        self.cloud = Actor("sky/cloud")

    def draw(self):
        self.sky.draw()
        self.cloud.draw()

    def move(self):
        self.cloud.x -= Character.Speed/self.Speed_modifier
