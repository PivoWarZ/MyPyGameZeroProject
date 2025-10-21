from pgzero.actor import Actor

from Game import Animator
from Game.Character import Character


class Enemy():
    def __init__(self, path, hit_points, isStatic = True, sprite_count = 10):
        self.sprite = Actor(f"{path}/0.png")
        self.hit_points = hit_points
        self.sprite_count = sprite_count
        self.is_static = isStatic
        self.move_offset = 300
        self.start_positionX = 0
        self.current_positionX = 0
        self.path = path
        self.animate_time = 0
        self.animation_speed = 0.1
        self.direction = 1
        self.speed = 10

    def tick(self, dt):
        if self.is_static:
            return

        self.animate_time += dt
        if self.animate_time >= self.animation_speed:
            can_flip = self.direction > 0
            path = self.set_path(can_flip)
            self.set_path(can_flip)
            self.sprite = Animator.animate(self.sprite, path, True, self.sprite_count)
            self.animate_time = 0

    def set_path(self, can_flip):
        if can_flip:
            new_path = f"{self.path}/flip"
            return new_path
        return self.path

    def take_damage(self, damage):
        self.hit_points -= damage
        return self.hit_points

    def get_actor(self):
        return self.sprite

    def set_position(self, positionX, positionY):
        self.start_positionX = positionX
        self.sprite.midbottom = (positionX, positionY)

    def move_function_dynamic(self, movable, direction):
        movable.x -= self.speed * self.direction + Character.Speed * direction
        self.start_positionX -= Character.Speed * direction
        if abs(self.start_positionX - self.sprite.x) >= self.move_offset:
            self.direction = self.direction * -1

    def move_function_static(self, movable, direction):
        from Game.Character import Character
        movable.x -= Character.Speed * direction

    def get_move_function(self):
        if self.is_static:
            return self.move_function_static
        return self.move_function_dynamic

