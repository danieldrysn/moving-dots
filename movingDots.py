#  Moving Dots  #
#  Daniel D. Doyle
#  2021-12-19

'''
This program was created to move dots on a screen in a pre-determined fashion
This first iteration creates dots moving in a light-speed fashion
'''

import numpy as np
import cv2
import dot

dim = np.array([600,600])
dot_space = np.zeros(dim)

win_name = 'Dot Space'
cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)
num = 100

init_dot = (dim/2).astype(int)
mdots = [dot.Dot(init_dot, dim) for i in range(num)]
for i, mdot in enumerate(mdots):
    for k in range(i + 1):
        mdot.moveDot(moveType=2,step=50)

while (True):

    for i, mdot in enumerate(mdots):
        if mdot.moveDot(moveType=2,step=3):
            dot_space[tuple(mdot.curr_dot)] = 256
            dot_space[tuple(mdot.prev_dot)] = 0
        else:
            dot_space[tuple(mdot.prev_dot)] = 0
            mdot.curr_dot = init_dot
            mdot.dot_dir = np.random.rand() * 360
            for k in range(i+1):
                mdot.moveDot()

    cv2.imshow(win_name, dot_space)

    key = cv2.waitKey(30)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

