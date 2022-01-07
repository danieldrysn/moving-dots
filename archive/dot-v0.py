# Dot Class
# Daniel D. Doyle
# 2021-12-20

'''
This dot class is used to help set up the contents of moving dots
The moving dots will provide a prescribed or random behavior for
displaying in a given scene
'''

import numpy as np
import math

class Dot:
    def __init__(self, init_x, init_y, dim_x, dim_y):
        self.dot_dir = np.random.rand() * 360
        self.prev_x = init_x
        self.prev_y = init_y
        self.x = init_x
        self.y = init_y
        self.dimx = dim_x
        self.dimy = dim_y

    def moveDot(self):
        if self.testBoundary():
            self.prev_x = self.x
            self.prev_y = self.y
        self.lineMovement()
        return self.testBoundary()

    def lineMovement(self):
        self.x += int(math.cos(self.dot_dir) * 10)
        self.y += int(math.sin(self.dot_dir) * 10)

    def randomMovement(self):
        step = 2
        self.x += -step if np.random.randn() < 0 else step
        self.y += -step if np.random.randn() < 0 else step

    def testBoundary(self):
        if self.x < 2 or self.x > self.dimx-2:
            return False
        if self.y < 2 or self.y > self.dimy-2:
            return False
        return True

    def __del__(self):
        del self
