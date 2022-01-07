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

def moveDot(dot_x,dot_y,dot_dir):
    dot_x += math.cos(dot_dir)*10
    dot_y += math.sin(dot_dir)*10
    return int(dot_x), int(dot_y)

dim_x = 600
dim_y = 600
dot_space = np.zeros([dim_x,dim_y])
init_space = np.array([[250, 350],[250,350]])

#init_dot = np.array([dot_x,dot_y])

win_name = 'Dot Space'
cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)


while(True):
    dot_dir = np.random.rand() * 360
    dot_x = int(dim_x / 2)
    dot_y = int(dim_y / 2)

    while (True):
        prev_dot_x = dot_x
        prev_dot_y = dot_y
        dot_space[prev_dot_y, prev_dot_x] = 0
        dot_x, dot_y = moveDot(dot_x, dot_y, dot_dir)
        if dot_x < 0 or dot_x > dim_x:
            break
        if dot_y < 0 or dot_y > dim_y:
            break
        dot_space[dot_y,dot_x] = 256

        cv2.imshow(win_name, dot_space)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

