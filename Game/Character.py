

from pgzero.actor import Actor
from pgzero.loaders import sounds

from Game import Animator, Helpers
from Game.HealthComponent import HealthComponent
from Game.SoundManager import sound_manager
from Game.Weapon import Weapon


class Character:

    Speed = 20
    PositionX = 30
    JumpForce = 500
    Health_Point = 10

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
        self.weapon = Weapon("splash")
        self.health_component = HealthComponent("heart", self.Health_Point)
        self.is_sound = False

    def draw(self):
        self.sprite.draw()
        self.health_component.print_hearts()

        if self.is_attack:
            self.weapon.draw(self.sprite)

    def jump(self):
        self.is_jump = True
        self.starting_point = 0

    def tick(self, dt, direction=0):
        self.animate_time += dt

        if self.is_attack:
            path = "character/attack"
            self.sprite = Animator.animate(self.sprite, path)
            self.weapon.shoot()
            sprite_count = Helpers.get_sprite_number(self.sprite)
            self.is_attack = sprite_count  < 4 and self.is_attack == True

            if not self.is_attack:
                self.weapon.reload()

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

        self.play_steps(direction)

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

    def attack(self):
        self.is_attack = True

        if sound_manager.on_sound:
            self.play_sword()

    def can_move(self, direction):
        if  not self.health_component.is_alive:
            return False
        return True

    def get_weapon(self):
        return self.weapon.get_current_weapon()

    def is_alive(self):
        return self.health_component.is_alive

    def take_damage(self):
        self.health_component.take_damage()

    def play_steps(self, direction):

        if not sound_manager.on_sound:
            return

        if direction != 0 and not self.is_sound:
            sounds.run.play()
            self.is_sound = True
        elif direction == 0:
            sounds.run.stop()
            self.is_sound = False

    def play_sword(self):
        sounds.sword.play()

