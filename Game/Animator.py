from pgzero.actor import Actor


def animate(actor: Actor, path, is_loop=True, sprite_count=5):
    position = actor.center
    first_sprite = f"{path}/0.png"
    current_path = "/".join(actor.image.split("/")[:-1])

    if current_path != path:
        actor = Actor(first_sprite)
        actor.center = (position[0], position[1])
        return actor

    index = actor.image.split("/")[-1]
    number = int(index.split(".")[0])

    next_sprite_number = (number + 1) % sprite_count

    if not is_loop and next_sprite_number == 0:
        next_sprite_number = 4

    actor = Actor(f"{path}/{str(next_sprite_number)}.png")
    actor.center = (position[0], position[1])
    return actor

