from symbol import parameters

from pgzero.actor import Actor


class Character:

    Speed = 55
    PositionX = 30

    def __init__(self, positionY):
        self.sprite = Actor("character/idle/idle1.png")
        self.sprite.bottomleft = (self.PositionX, positionY + 7)

    def draw(self):
        self.sprite.draw()

