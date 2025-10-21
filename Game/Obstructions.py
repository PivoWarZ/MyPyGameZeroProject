from pgzero.actor import Actor

from Game import Helpers
from Game.Character import Character
from Game.Enemy import Enemy
from Game.GameWindow_config import GameWindow
from Game.Movable import Movable


class Obstructions(Movable):
    def __init__(self, positionY):
        self.positionY = positionY
        self.obstructions = [

            Enemy("obstructions", 3,(800, positionY),True),
            Enemy("obstructions", 3, (1800, positionY), True),
            Enemy("obstructions", 3, (2800, positionY), True),

            Enemy("orc", 10, (4800, positionY), False),
            Enemy("orc", 10, (6800, positionY), False),

            Enemy("platforms/1", 10000, (8000, 850), True),
            Enemy("platforms/1", 10000, (8380, 850), True),
            Enemy("platforms/1", 10000, (8760, 850), True),
            Enemy("platforms/1", 10000, (9140, 850), True),

            Enemy("orc", 10, (11140, positionY), False),
            Enemy("orc", 10, (13140, positionY), False),

            Enemy("platforms/2", 10000, (15000, 850), True),
            Enemy("platforms/2", 10000, (15380, 850), True),
            Enemy("platforms/2", 10000, (15760, 850), True),
            Enemy("platforms/2", 10000, (16140, 850), True),

            Enemy("orc", 10, (20000, positionY), False),
            Enemy("orc", 10, (22000, positionY), False),

            Enemy("obstructions", 3, (23000, positionY), True),
            Enemy("obstructions", 3, (24000, positionY), True),
            Enemy("obstructions", 3, (24500, positionY), True),


        ]


    def draw(self):
        for visible in self.obstructions:
            visible.get_actor().draw()

    def move(self, direction):
        for mover in self.obstructions:
            move_function = mover.get_move_function()
            movable = mover.get_actor()
            move_function(movable, direction)

    def move_function(self, movable, direction):
         movable.x -= Character.Speed * direction

    def tick(self, dt):
        for tickable in self.obstructions:
            tickable.tick(dt)

    def get_obstructions(self):
        enemies = []
        for obstruction in self.obstructions:
            enemies.append(obstruction.get_actor())
        return enemies

    def take_damage(self, actor_index):
        damageable = self.obstructions[actor_index]
        hit_points = damageable.take_damage()
        if hit_points <= 0:
            del self.obstructions[actor_index]
