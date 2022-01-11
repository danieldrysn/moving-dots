#  Moving Dots  #
#  Daniel D. Doyle
#  2021-12-19

'''
This program was created to move dots on a screen in a pre-determined fashion
This first iteration creates dots moving in a light-speed fashion
'''
import imageio
import numpy as np
import cv2
import dot

size = 300
dim = np.array([size,size])
dot_space = np.zeros([size,size,3], dtype="uint8")

win_name = 'Dot Space'
cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)
num = 100

thickness = 3
init_dot = (dim/2).astype(int)
mdots = [dot.Dot(init_dot, dim) for i in range(num)]
for i, mdot in enumerate(mdots):
    for k in range(i%5+1):
        mdot.setStep(np.random.rand()*10)
        mdot.setTranslation(np.array([int(np.random.rand()*dim[0]),int(np.random.rand()*dim[1])]))
        mdot.moveDot(moveType=1)
    mdot.init_dot = mdot.curr_dot
    mdot.thickness = int(np.random.rand()*3)+1

frames = []
while (True):

    for i, mdot in enumerate(mdots):
        if mdot.moveDot(moveType=1):
            cv2.line(dot_space, mdot.curr_dot, mdot.curr_dot, mdot.color,mdot.thickness)
            cv2.line(dot_space, mdot.prev_dot, mdot.prev_dot, (0, 0, 0), mdot.thickness)
        else:
            cv2.line(dot_space, mdot.prev_dot, mdot.prev_dot, (0, 0, 0), mdot.thickness)
            mdot.curr_dot = init_dot
            mdot.setTranslation(np.array([int(np.random.rand() * dim[0]), int(np.random.rand() * dim[1])]))
            mdot.setStep(np.random.rand() * 10)
            mdot.dot_dir = np.random.rand() * 360
            for k in range(i%5+1):
                mdot.moveDot()
            mdot.setStep(2)
            mdot.init_dot = mdot.curr_dot
            mdot.thickness = int(np.random.rand() * 3) + 1

    rgb_frame = cv2.cvtColor(dot_space, cv2.COLOR_BGR2RGB)
    frames.append(rgb_frame)
    cv2.imshow(win_name, dot_space)
    key = cv2.waitKey(30)
    if key & 0xFF == ord('q') or key & 0xFF == ord('Q'):
        break

with imageio.get_writer('./images/Moving_Dots.gif', mode='I') as writer:
    for idx, frame in enumerate(frames):
        print('Adding frame to GIF file:', idx+1)
        filename = f'./images/gif{idx+1:03}.png'
        if idx > 10:
            writer.append_data(frame)

cv2.destroyAllWindows()




