import random
import time


class Effect(object):
    def __init__(self, wall):
        self.wall = wall
        wall.clear()

    def run(self):
        pass


class PaintInRed(Effect):
    def run(self):
        hue = 1
        saturation = 1
        value = 1

        hsv = (hue, saturation, value)

        for i in range(self.wall.width):
            for j in range(self.wall.height):
                self.wall.set_pixel(i, j, hsv)
        self.wall.draw()


