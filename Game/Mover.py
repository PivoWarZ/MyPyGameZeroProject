class Mover():

    def __init__(self, *args):
        self.movers = args

    def move(self):
        for mover in self.movers:
            mover.move()