#  Moving Dots  #
#  Daniel D. Doyle
#  2021-12-19

'''
This program was created to moving dots on a screen in a pre-determined fashion
The first thought was to try to create dots moving in a light-speed fashion
This thought led to trying to provide multiple ways of moving those dots
'''

import numpy as np
import cv2
import math
import dot

dim_x = 600
dim_y = 600
dot_space = np.zeros([dim_x,dim_y])
init_space = np.array([[250, 350],[250,350]])

win_name = 'Dot Space'
cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)

num = 100

while(True):
    dot_x = int(dim_x / 2)
    dot_y = int(dim_y / 2)
    mdots = [dot.Dot(dot_x,dot_y, dim_x, dim_y) for i in range(num)]
    for i, mdot in enumerate(mdots):
        for j in range(i+1):
            mdot.moveDot()

    while (True):
        mdot_data = np.ones(num)
        for i, mdot in enumerate(mdots):
            if mdot.moveDot():
                dot_space[mdot.y,mdot.x] = 256
                dot_space[mdot.prev_y, mdot.prev_x] = 0
            else:
                dot_space[mdot.prev_y, mdot.prev_x] = 0
            mdot_data[i] = mdot.testBoundary()

        cv2.imshow(win_name, dot_space)

        key = cv2.waitKey(10)
        if key & 0xFF == ord('q') or not any(mdot_data):
            break

    if key == ord('q'):
        break


cv2.destroyAllWindows()

