class Gravity:

    GravityForce = 10
    StartGravity = 10
    GravityStep = 0.1
    def __init__(self):
        self.characters = []
        self.grounds = []
    def tick(self, ground_objects):
        self.grounds.clear()
        self.grounds.extend(ground_objects)

        for character in self.characters:
            actor = character.get_current_actor()
            contact_points = 0
            for ground in ground_objects:
                if ground.collidepoint(actor.midbottom):
                    contact_points += 1
            if contact_points == 0:
                actor.y += self.GravityForce
                self.GravityForce += self.GravityStep
            else:
                self.GravityForce = self.StartGravity

    def is_ground(self, actor):
        for ground in self.grounds:
            if ground.collidepoint(actor.midbottom):
                return True
        return False

    def init (self, *args):
        self.characters = args


gravity = Gravity()







