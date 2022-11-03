from pico2d import *
import Game_World

class Ball:
    image = None
    def __init__(self, x=800, y=300, velocity=1):
        self.isActive = True

        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

        self.x, self.y, self.velocity = x, y, velocity
        pass

    def __del__(self):
        pass

    def draw(self):
        if self.isActive is False:
            return

        self.image.draw(self.x, self.y)
        pass

    def update(self):
        if self.x >= 800 or self.x <= 0:
            Game_World.Remove_Object(self)

        self.x += self.velocity
        pass

    pass