from pgzero.actor import Actor

from Game import Speed_config, Helpers
from Game.Character import Character
from Game.GameWindow_config import GameWindow
from Game.Movable import Movable
from Game.Sky import Sky


class Sun(Movable):

    offset = 20

    def __init__(self, sky : Sky):
        self.sky = sky
        self.is_day = True
        self.suns = [
            Actor("sun/0.png"),
            Actor("sun/1.png"),
        ]

        offsetX = 0

        for sun in self.suns:
            sun.topright = (GameWindow.Width - self.offset + offsetX, self.offset)
            offsetX += 1920

    def draw(self):
        for sun in self.suns:
            sun.draw()

    def move(self, _):
        for sun in self.suns:
            self.move_function(sun, _)
            if sun.topleft[0] < 0:
                sun.x += 3960
                self.is_day = not self.is_day
                self.sky.switcher(self.is_day)

    def move_function(self, movable, _):
        movable.x -= Character.Speed / Speed_config.Sun_speed_modifier