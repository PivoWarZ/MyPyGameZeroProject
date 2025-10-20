from pgzero.clock import clock


class OnCollisionEntered:
    def __init__(self, *enemies):
        self.enemies = enemies
        self.collision_counter = 15

    def tick(self, actor):
        if actor.collidelist(self.enemies) != -1:
            self.collision_counter -= 1
            clock.schedule(self.refresh, 0.5)
            if self.collision_counter == 0:
                print(f"damage {actor.collidelist(self.enemies)}")

    def refresh(self):
        self.collision_counter = 10
