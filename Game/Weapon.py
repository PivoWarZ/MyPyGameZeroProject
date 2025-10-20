from pgzero.actor import Actor

from Game import Animator


class Weapon():
    def __init__(self, path, damage):
        self.actor = Actor(f"{path}\0")
        self.path = path
        self.damage = damage
        self.animate_time = 0
        self.animation_speed = 0.1

    def shoot(self, shoot_point : Actor):
        Animator.animate(self.actor, self.path, False)

    def draw(self):
        self.actor.draw()
