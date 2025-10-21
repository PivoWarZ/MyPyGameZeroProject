from pgzero.actor import Actor


class HealthComponent:
    def __init__(self, path, health_points):
        self.actor = Actor(f"{path}/0")
        self.health_points = health_points
        self.is_alive = True

    def print_hearts(self):
        offsetX = 20
        for i in range(self.health_points):
            self.actor.draw()
            self.actor.topleft = (offsetX, 20)
            offsetX += self.actor.width

    def take_damage(self):
        self.health_points = self.health_points - 1
        if self.health_points <= 0:
            self.is_alive = False

    def is_alive(self):
        return self.is_alive

