from game import Game

class Camera():
    
    def __init__(self, game):
        self.game = game
        self.width = 1080
        self.height = 720
        self.camera = pg.Rect(0, 0, width, height)

    def update(self, target, screen_width, screen_height):
        x = int(screen_width / 2) - target.rect.centerx

        self.camera = pg.Rect(x, y, self.width, self.height)