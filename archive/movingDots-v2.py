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

dim_x = 600
dim_y = 600
dot_space = np.zeros([dim_x,dim_y])

win_name = 'Dot Space'
cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)

num = 200

dot_x = int(dim_x / 2)
dot_y = int(dim_y / 2)
mdots = [dot.Dot(dot_x,dot_y, dim_x, dim_y) for i in range(num)]
for i, mdot in enumerate(mdots):
    for j in range(i+1):
        mdot.moveDot()

while (True):

    for i, mdot in enumerate(mdots):
        if mdot.moveDot():
            dot_space[mdot.y,mdot.x] = 256
            dot_space[mdot.prev_y,mdot.prev_x] = 0
        else:
            dot_space[mdot.prev_y,mdot.prev_x] = 0
            mdot.x = dot_x
            mdot.y = dot_y
            for k in range(i+1):
                mdot.moveDot()

    cv2.imshow(win_name, dot_space)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

