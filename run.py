import argparse, sys

import effects
from wall import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--width", dest="width", type=int,
                        action="store", default=8)
    parser.add_argument("-t", "--height", dest="height", type=int,
                        action="store", default=8)

    args = parser.parse_args()

    print args.width
    print args.height

    wall = Wall(args.width, args.height)

    eff = effects.PaintInBlue(wall)
    eff.run()


