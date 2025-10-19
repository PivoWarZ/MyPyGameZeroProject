from pgzero.actor import Actor


def animate(actor, animation_time, animation_speed, delta_time):
    animation_time += delta_time
    if animation_time > animation_speed:
        animation_time = 0
        index = actor.sprite.image.split("/")[-1]
        number = int(index.split(".")[0])
        next_sprite_number = (number + 1) % 5
        actor.sprite = Actor("character/idle/" + str(next_sprite_number) + ".png")
        actor.sprite.bottomleft = (self.PositionX, self.positionY + 7)