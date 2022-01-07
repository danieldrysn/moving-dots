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
    def __init__(self, init_dot, dim):
        self.history = None
        self.step = 1
        self.init_dot = init_dot
        self.color = np.array([np.random.rand() * 256,np.random.rand() * 256,np.random.rand() * 256])
        self.dot_dir = np.random.rand() * 360
        self.curr_dot = init_dot
        self.dim = dim
        self.thickness = 1

    def setTranslation(self, translation):
        self.curr_dot = translation

    def setStep(self, step):
        self.step = step

    def moveDot(self, moveType = 1):
        self.prev_dot = self.curr_dot
        if moveType == 1: self.curr_dot = self.lineMovement(self.step)
        if moveType == 2: self.curr_dot = self.randomMovement(self.step)
        return self.testBoundary()

    def lineMovement(self,step=1):
        return self.curr_dot + np.array([int(math.sin(self.dot_dir) * 10*step),
                                   int(math.cos(self.dot_dir) * 10*step)])

    def randomMovement(self, step=2):
        return self.curr_dot + np.array([-step if np.random.randn() < 0 else step,
                                        -step if np.random.randn() < 0 else step])

    def dotHistory(self,prev_dot,size=10):
        self.history.append(prev_dot)
        if len(self.history) > size:
            self.history.pop()
        return self.history

    def testBoundary(self):
        if (self.curr_dot > np.array([0,0])).all() and (self.curr_dot < self.dim).all():
            return True
        else:
            self.curr_dot = self.prev_dot
            return False

    def printDotInfo(self, i):
        print(f'i={i}, angle={self.dot_dir:3.2f}, prev={self.prev_dot}, curr={self.curr_dot}')


