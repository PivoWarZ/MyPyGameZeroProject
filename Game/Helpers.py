from pgzero.actor import Actor


def set_start_position(positionY, isTopLeftAnchor = False, *args):

    for actors in args:

        is_first = True

        for actor in actors:
            if is_first:
                if isTopLeftAnchor:
                    actor.topleft = (0, positionY)
                else:
                    actor.bottomleft = (0, positionY)
            else:
                max_right = max(index.right for index in actors)
                print(max_right)
                if isTopLeftAnchor:
                    actor.topleft = (max_right, positionY)
                else:
                    actor.bottomleft = (max_right, positionY)

            is_first = False
            print("is_first ", is_first)

def Moving(move_function, direction, is_addeble = False, *args):

    for actors in args:
        for movable in actors:
            move_function(movable, direction)
            if is_addeble and movable is actors[-2] and movable.topright[0] <= 0:
                actor_path = f"{movable.image}"
                print(actor_path + "=>" + str(len(actors)))
                new_actor = Actor(movable.image)
                actors.append(new_actor)

                max_right = max(index.right for index in actors)
                new_actor.topleft = (max_right, movable.topleft[1])
def Drawning(*args):
    for arg in args:
        for actor in arg:
            actor.draw()