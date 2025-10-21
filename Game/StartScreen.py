from pgzero.actor import Actor



class StartScreen():
    def __init__(self):
        self.background = Actor("sky/night.png")
        self.knight = Actor("startscreen/0.png")
        self.start_button = Actor("startscreen/1.png")
        self.start_button.topleft = (1000, 200)
        self.sound_button = Actor("startscreen/2.png")
        self.sound_button.topleft = (1100, 500)
        self.music = True
        self.sound = True

    def draw(self):
        self.background.draw()
        self.knight.draw()
        self.start_button.draw()
        self.sound_button.draw()

    def on_mouse_down(self, pos):
        from Game.GameManager import game_manager
        from Game.EntryPoint import sound_manager

        if self.sound_button.collidepoint(pos):
            self.sound = not self.sound
            self.music = not self.music
            sound_manager.set_volume(self.music, self.sound)
            if not sound_manager.on_sound:
                self.sound_button.image = "startscreen/3.png"
            elif sound_manager.on_sound :
                self.sound_button.image = "startscreen/2.png"
            self.draw()
            print(f"{sound_manager.on_music}: {sound_manager.on_sound}")

        if self.start_button.collidepoint(pos):
            game_manager.start_game()
