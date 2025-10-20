from pgzero.actor import Actor


def set_start_position(positionY, isTopLeftAnchor=False, *args):
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
                if isTopLeftAnchor:
                    actor.topleft = (max_right, positionY)
                else:
                    actor.bottomleft = (max_right, positionY)

            is_first = False


def moving(move_function, direction, is_addeble=False, is_static =False, *args):
    for actors in args:
        for movable in actors:
            move_function(movable, direction)

            if is_static:
                continue

            if movable.topright[0] > 0:
                continue

            max_right = max(index.right for index in actors)

            if not is_addeble:
                movable.topleft = (max_right, movable.topleft[1])
                continue

            if is_addeble and movable is actors[-2]:
                actor_path = f"{movable.image}"
                new_actor = Actor(movable.image)
                actors.append(new_actor)
                new_actor.topleft = (max_right, movable.topleft[1])


def drawning(*args):
    for arg in args:
        for actor in arg:
            actor.draw()
