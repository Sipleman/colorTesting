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
        time.sleep(2)


class HueTest(Effect):
    def run(self):
        hue = 1
        saturation = 1
        value = 1
        hsv = (hue, saturation, value)
        self.wall.clear()
        for i in range(self.wall.width):
            for j in range(self.wall.height):
                self.wall.set_pixel(i, j, hsv)
        start_time = time.time()
        while time.time() - start_time < 10:
            hue += 0.01
            hue %= 1
            self.wall.set_global_hue(hue)
            self.wall.draw()
            time.sleep(0.04)


class SaturationTest(Effect):
    def run(self):
        self.wall.clear()
        hue = 1
        saturation = 1
        value = 1

        self.wall.clear()

        start_time = time.time()

        while time.time() - start_time < 4:
            saturation += 0.01
            saturation %= 1
            for i in range(self.wall.width):
                for j in range(self.wall.height):
                    self.wall.set_pixel(i, j, (hue, saturation, value))
            time.sleep(0.04)
            self.wall.draw()


class SaturationTestWithBlinkEffect(Effect):
    def run(self):
        self.wall.clear()
        hue = 0
        saturation = 1
        value = 1

        self.wall.clear()

        start_time = time.time()

        is_grow = False
        while time.time() - start_time < 4:
            if is_grow:
                saturation += 0.01
            else:
                saturation -= 0.01

            if saturation >= 1:
                is_grow = False
            if saturation <= 0:
                is_grow = True

            for i in range(self.wall.width):
                for j in range(self.wall.height):
                    self.wall.set_pixel(i, j, (hue, saturation, value))
            time.sleep(0.005)
            self.wall.draw()


class SaturationTestWithRandomColor(Effect):
    def run(self):
        self.wall.clear()
        hue = random.random()
        saturation = 1
        value = 1

        self.wall.clear()

        start_time = time.time()

        is_grow = False
        while time.time() - start_time < 4:
            if is_grow:
                saturation += 0.01
            else:
                saturation -= 0.01

            if saturation >= 1:
                is_grow = False
            if saturation <= 0:
                is_grow = True

            for i in range(self.wall.width):
                for j in range(self.wall.height):
                    self.wall.set_pixel(i, j, (hue, saturation, value))
            time.sleep(0.005)
            self.wall.draw()


class ValueTest(Effect):
    def run(self):
        self.wall.clear()
        hue = random.random()
        saturation = 1
        value = 1

        self.wall.clear()

        start_time = time.time()

        while time.time() - start_time < 4:
            value += 0.01
            value %= 1
            for i in range(self.wall.width):
                for j in range(self.wall.height):
                    self.wall.set_pixel(i, j, (hue, saturation, value))
            time.sleep(0.004)
            self.wall.draw()
