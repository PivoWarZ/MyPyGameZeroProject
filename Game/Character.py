from symbol import parameters

from pgzero.actor import Actor


class Character:

    Speed = 55
    PositionX = 30
    JumpForce = 300

    def __init__(self, positionY):
        self.sprite = Actor("character/idle/0.png")
        self.start_position = (self.PositionX, positionY)
        self.sprite.bottomleft = self.start_position
        self.jump_offset = 25
        self.is_jump = False
        self.starting_point = 0
        self.animate_time = 0
        self.animation_speed = 0.1
        self.positionY = positionY

    def draw(self):
        self.sprite.draw()

    def jump(self):
        self.is_jump = True
        self.starting_point = 0

    def tick(self, dt, direction=0):
        if self.is_jump:
            if self.starting_point < self.JumpForce:
                self.sprite.y -= self.jump_offset
                self.starting_point += self.jump_offset
                return
            self.is_jump = False

        if direction != 0:
            self.run_animation(dt)
            return

        if self.sprite.bottomleft[1] < self.start_position[1]:
            return

        self.idle_animation(dt)


    def get_gravity_object(self):
        return self.sprite

    def idle_animation(self, dt):
        position = self.sprite.center
        self.animate_time += dt
        if self.animate_time > self.animation_speed:
            self.animate_time = 0
            index = self.sprite.image.split("/")[-1]
            number = int(index.split(".")[0])
            next_sprite_number = (number + 1) % 5
            self.sprite = Actor("character/idle/" + str(next_sprite_number) + ".png")
            self.sprite.center = (position[0], position[1])


    def run_animation(self, dt):
        position = self.sprite.center
        self.animate_time += dt
        animation_speed = self.animation_speed / 2
        if self.animate_time > animation_speed:
            self.animate_time = 0
            index = self.sprite.image.split("/")[-1]
            number = int(index.split(".")[0])
            next_sprite_number = (number + 1) % 5
            self.sprite = Actor("character/run/" + str(next_sprite_number) + ".png")
            self.sprite.center = (position[0], position[1])

