from pgzero.actor import Actor
class Gravity:

    GravityForce = 5
    def __init__(self, ground_objects, *args):
        self.gravity_objects = args
        self.ground_objects = ground_objects
    def tick(self):
        for object in self.gravity_objects:
            current_gravity_object = object.get_gravity_object()
            if current_gravity_object.collidelist(self.ground_objects) == -1:
                current_gravity_object.y += self.GravityForce




