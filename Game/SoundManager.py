from pgzero import music


class SoundManager:
    def __init__(self):
        self.on_music = True
        self.on_sound = True

    def set_volume(self, music_vol, sound):
        self.on_music = music_vol
        self.on_sound = sound

        if not self.on_music:
            self.stop()
        elif not music.is_playing("bird.wav"):
            self.play()

    def play(self):
        if self.on_music:
            music.play("bird.wav")

    def stop(self):
        music.stop()


sound_manager = SoundManager()





