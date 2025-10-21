class GameManager():
    def __init__(self):
        self.game_state = 0

    def set_state(self, state):
        self.game_state = state

    def start_game(self):
        self.game_state = 1

game_manager = GameManager()