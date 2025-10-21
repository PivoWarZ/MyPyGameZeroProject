from pgzero.actor import Actor
class Gravity:

    GravityForce = 10
    def __init__(self, ground_objects, *args):
        self.gravity_objects = args
        self.ground_objects = ground_objects
    def tick(self):
        for object in self.gravity_objects:
            current_gravity_object = object.get_current_actor()
            if current_gravity_object.collidelist(self.ground_objects) == -1:
                current_gravity_object.y += self.GravityForce




