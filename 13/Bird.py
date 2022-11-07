import random

from pico2d import *

import game_framework
import game_world

size = [900//5, 500//3]

class Bird:
    def __init__(self):
        self.x, self.y = 100, random.randint(200, 500)
        self.frame = 0
        self.dir, self.face_dir = 1, 'None'
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.speed = random.randint(100,300)
        self.image_Speed = self.speed / 10
        self.image_Frame = (5,5,3)
        self.frame_Count = 0

    def update(self):
        self.frame = self.frame + self.image_Speed * game_framework.frame_Time

        self.x += self.dir * self.speed * game_framework.frame_Time
        self.x = clamp(0, self.x, 1600)

        if self.x <= 50:
            self.dir = 1
            self.face_dir = 'None'
        elif self.x >= 1600 - 50:
            self.dir = -1
            self.face_dir = 'h'

    def draw(self):
        if self.frame >= self.image_Frame[self.frame_Count]:
            self.frame_Count = (self.frame_Count + 1) % 3
            self.frame = 0

        self.image.clip_composite_draw(int(self.frame)*size[0], (2 - self.frame_Count) * size[1], size[0], size[1], 0, self.face_dir, self.x, self.y, 100, 100)