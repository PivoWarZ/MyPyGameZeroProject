from pgzero.actor import Actor

from Game import Animator, Helpers


class Weapon():
    def __init__(self, path):
        self.actor = Actor(f"{path}/0.png")
        self.path = path
        self.animate_time = 0
        self.animation_speed = 0.1

    def shoot(self):
        self.actor = Animator.animate(self.actor, self.path, False)
        number = Helpers.get_sprite_number(self.actor)

    def draw(self, sprite : Actor):
        self.actor.midleft = sprite.center
        self.actor.draw()

    def reload(self):
        self.actor = Actor(f"{self.path}/0.png")

    def get_current_weapon(self):
        return self.actor

