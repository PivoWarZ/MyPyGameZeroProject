from pgzero.actor import Actor

from Game import Animator


class Character:

    Speed = 20
    PositionX = 30
    JumpForce = 500

    def __init__(self, positionY):
        self.sprite = Actor("character/idle/0.png")
        self.start_position = (self.PositionX, positionY)
        self.sprite.bottomleft = self.start_position
        self.jump_offset = 25
        self.is_jump = False
        self.is_attack = False
        self.starting_point = 0
        self.animate_time = 0
        self.animation_speed = 0.1

    def draw(self):
        self.sprite.draw()

    def jump(self):
        self.is_jump = True
        self.starting_point = 0

    def tick(self, dt, direction=0):
        self.animate_time += dt

        if self.is_attack:
            path = "character/attack"
            self.sprite = Animator.animate(self.sprite, path)
            print(f"is attack: {self.is_attack}")
            sprite_count = self.get_sprite_number(self.sprite)
            self.is_attack = sprite_count  < 4 and self.is_attack == True
            print(f"sprite count: {sprite_count}, sprite number: {self.get_sprite_number(self.sprite)}")
            print(self.is_attack)
            self.animate_time = 0
            return

        if self.animate_time > self.animation_speed and not self.is_jump:
            self.animated(direction)
            self.animate_time = 0

        if self.is_jump:
            path = "character/jump"
            self.sprite = Animator.animate(self.sprite, path, False)
            self.is_jump = self.jumped()
            self.animate_time = 0

    def get_current_actor(self):
        return self.sprite

    def jumped(self):
        if self.starting_point < self.JumpForce:
            self.sprite.y -= self.jump_offset
            self.starting_point += self.jump_offset
            return True
        return False

    def animated(self, direction):
        if direction == 0:
            path = "character/idle"
            self.sprite = Animator.animate(self.sprite, path)
        if direction != 0:
            path = "character/run"
            self.sprite = Animator.animate(self.sprite, path)

    def get_sprite_number(self, actor):
        index = actor.image.split("/")[-1]
        number = int(index.split(".")[0])
        return int(number)

    def attack(self):
        self.is_attack = True

    def can_move(self):
        return not self.is_attack


