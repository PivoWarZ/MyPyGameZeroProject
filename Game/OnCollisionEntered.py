from pgzero.clock import clock
from Game.Obstructions import Obstructions


class OnCollisionEntered:
    def __init__(self, obstructions : Obstructions):
        self.obstructions = obstructions
        self.collision_counter = 15
        self.weapon_collision_counter = 3

    def tick(self, actor, weapon):
        if actor.collidelist(self.obstructions.get_obstructions()) != -1:
            self.collision_counter -= 1
            clock.schedule(self.refresh, 0.5)
            if self.collision_counter == 0:
                pass

        if weapon.collidelist(self.obstructions.get_obstructions()) != -1:
            self.weapon_collision_counter -= 1
            clock.schedule(self.reload, 0.5)
            if self.weapon_collision_counter <= 0:
                obstruction_index = weapon.collidelist(self.obstructions.get_obstructions())
                print(obstruction_index)
                self.obstructions.take_damage(obstruction_index)



    def refresh(self):
        self.collision_counter = 10

    def reload(self):
        self.weapon_collision_counter = 3
