from pgzero.actor import Actor

from Game import Helpers
from Game.Character import Character
from Game.Enemy import Enemy
from Game.GameWindow import GameWindow
from Game.Movable import Movable


class Obstructions(Movable):
    def __init__(self, positionY):
        self.obstructions = {
            0: {"actor": Enemy("orc", False), "hit_points": 3},
            1: {"actor": Enemy("obstructions", True), "hit_points": 2}
        }
        self.killed_count = 0
        self.obstructions[0]["actor"].set_position(GameWindow.Width / 2, positionY)
        self.obstructions[1]["actor"].set_position(GameWindow.Width, positionY)

    def draw(self):
        visibles = self.get_obstructions()
        for visible in visibles:
            visible.draw()

    def move(self, direction):
        move_list = self.get_enemies()
        for mover in move_list:
            move_function = mover.get_move_function()
            movable = mover.get_actor()
            move_function(movable, direction)

    def move_function(self, movable, direction):
         movable.x -= Character.Speed * direction

    def tick(self, dt):
        for tickable in self.get_enemies():
            tickable.tick(dt)

    def get_obstructions(self):
        list = []
        for obstruction in self.obstructions.values():
            sprite = obstruction["actor"].get_actor()
            list.append(sprite)
        return list

    def get_enemies(self):
        list = []
        for obstruction in self.obstructions.values():
            sprite = obstruction["actor"]
            list.append(sprite)
        return list
    def take_damage(self, actor_index):
        print(actor_index, self.killed_count)
        damageable = self.obstructions[actor_index + self.killed_count]
        damageable["hit_points"] -= 1
        hit_points = damageable["hit_points"]
        if hit_points <= 0:
            del self.obstructions[actor_index + self.killed_count]
            self.killed_count += 1
        print(f"damage {actor_index} : HIT points {damageable['hit_points']}")
