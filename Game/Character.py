from symbol import parameters

from pgzero.actor import Actor


class Character:

    Speed = 55
    PositionX = 30
    JumpForce = 300

    def __init__(self, positionY):
        self.sprite = Actor("character/idle/idle1.png")
        self.sprite.bottomleft = (self.PositionX, positionY + 7)
        self.jump_offset = 25
        self.is_jump = False
        self.starting_point = 0

    def draw(self):
        self.sprite.draw()

    def jump(self):
        self.is_jump = True
        self.starting_point = 0

    def tick(self):
        if self.is_jump:
            print(self.is_jump, self.sprite.y)
            if self.starting_point < self.JumpForce:
                self.sprite.y -= self.jump_offset
                self.starting_point += self.jump_offset
                return
            self.is_jump = False

    def character(self):
        return self.sprite