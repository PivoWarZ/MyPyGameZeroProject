class GameWindow:

    Title = "KNIGHT ADVENTURE"
    Width = 1920
    Height = 1080

    @property
    def GetWindowParametres(self):
        return (self.Title, self.Width, self.Height)
