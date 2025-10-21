class OnCollisionEntered:
    def __init__(self, character, obstructions):
        self.obstructions = obstructions
        self.collision_counter = 30
        self.weapon_collision_counter = 3
        self.character = character

    def tick(self):
        actor = self.character.get_current_actor()
        index = actor.collidelist(self.obstructions.get_obstructions())
        if index != -1:
            collision_actor = self.obstructions.get_obstructions()[index]
            distance = collision_actor.distance_to(actor.center)
            if abs(distance) < actor.width / 2:
                self.collision_counter -= 1
                if self.collision_counter == 0:
                    self.character.take_damage()
                    self.refresh()
        else:
            self.refresh()


        weapon = self.character.get_weapon()

        if weapon.collidelist(self.obstructions.get_obstructions()) != -1:
            self.weapon_collision_counter -= 1
            if self.weapon_collision_counter <= 0:
                obstruction_index = weapon.collidelist(self.obstructions.get_obstructions())
                self.obstructions.take_damage(obstruction_index)
                self.reload()



    def refresh(self):
        self.collision_counter = 10

    def reload(self):
        self.weapon_collision_counter = 3
