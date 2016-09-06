from Tkinter import ALL, Canvas, Frame, SUNKEN, Tk
import colorsys
import time


class Wall(object):

    MIN_RED = MIN_GREEN = MIN_BLUE = 0x0
    MAX_RED = MAX_GREEN = MAX_BLUE = 0xFF

    SQUARE_WIDTH = 50

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._tk_init()
        self.pixels = [[(0, 0, 1) for x in range(width)] for y in range(height)] #initialize tuple
                                                                       #with 3 arguments:
                                                                       #hue, saturation and value(or lightning)

    def _tk_init(self):
        self.root = Tk()
        self.root.title("Color wall %dx%d" % (self.width,self.height))
        self.frame = Frame(self.root)
        self.frame.pack()
        self.canvas = Canvas(self.root, width=self.width*self.SQUARE_WIDTH, height=self.height*self.SQUARE_WIDTH)
        self.canvas.pack()
        self.root.update()

    def set_pixel(self, x, y, hsv):
        self.pixels[x][y] = hsv

    def get_pixel(self, x, y):
        return self.pixels[x][y]

    def draw(self):
        self.canvas.delete(ALL)
        for i in range(len(self.pixels)):
            x_0 = i * self.SQUARE_WIDTH
            x_1 = i * self.SQUARE_WIDTH + self.SQUARE_WIDTH
            for j in range(len(self.pixels[0])):
                y_0 = j * self.SQUARE_WIDTH
                y_1 = j * self.SQUARE_WIDTH + self.SQUARE_WIDTH

                s = self._get_rgb(self.pixels[i][j])
                hue = "#%02x%02x%02x" % s
                self.canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=hue)
        self.canvas.update()
        time.sleep(2)

    def clear(self):
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                self.pixels[i][j] = (0, 0, 0)

    def _hsv_to_rgb(self, hsv):
        rgb = colorsys.hsv_to_rgb(*hsv)
        red = self.MAX_RED * rgb[0]
        green = self.MAX_GREEN * rgb[1]
        blue = self.MAX_BLUE * rgb[2]
        return (red, green, blue)

    def _get_rgb(self, hsv):
        red, green, blue = self._hsv_to_rgb(hsv)
        red = int(float(red) / (self.MAX_RED - self.MIN_RED) * 0xFF)
        green = int(float(green) / (self.MAX_GREEN - self.MIN_GREEN) * 0xFF)
        blue = int(float(blue) / (self.MAX_BLUE - self.MIN_BLUE) * 0xFF)
        return (red, green, blue)

