import random

from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        self.name = 'ball'
        self.isActive = True
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = x, y
        self.realX, self.realY = 0, 0
        self.velocity = velocity

    def get_bb(self):
        return self.realX - 10, self.realY - 10, self.realX + 10, self.realY + 10

    def draw(self):
        self.realX, self.realY = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.realX, self.realY)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_collision(self, other, group):
        if other.name == 'boy':
            self.x = random.randint(10, server.background.w - 10)
            self.y = random.randint(10, server.background.h - 10)

        pass