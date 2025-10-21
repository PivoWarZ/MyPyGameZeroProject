from pgzero.actor import Actor


class Platform:
    def __init__(self, path, index, positionX, positionY):
        self.actor = Actor(f"{path}/{index}.png")
        self.actor.midbottom = (positionX, positionY)

    def get_actor(self):
        return self.actor