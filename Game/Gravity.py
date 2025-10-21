class Gravity:

    GravityForce = 10
    def __init__(self,  *args):
        self.characters = args
    def tick(self, ground_objects):
        for character in self.characters:
            actor = character.get_current_actor()
            contact_points = 0
            for ground in ground_objects:
                if ground.collidepoint(actor.midbottom):
                    contact_points += 1
            if contact_points == 0:
                actor.y += self.GravityForce







