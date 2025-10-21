from Game.Character import Character
from Game.GameWindow_config import GameWindow
from Game.Movable import Movable
from Game.Platform import Platform


class PlatforformManager(Movable):
    def __init__(self):
        self.path = "platforms"
        self.platforms = [

            Platform("platforms", 0, 8250, 600),
            Platform("platforms", 0, 8650, 400),

            Platform("platforms", 1, 15500, 600),
            Platform("platforms", 1, 16000, 400)

        ]

    def draw(self):
        for platform in self.platforms:
            platform.get_actor().draw()

    def move(self, direction):
        for mover in self.platforms:
            movable = mover.get_actor()
            self.move_function(movable, direction)

    def move_function(self, movable, direction):
        movable.x -= Character.Speed * direction

    def get_platforms_actor(self):
        list = []
        for platform in self.platforms:
            list.append(platform.get_actor())
        return list
