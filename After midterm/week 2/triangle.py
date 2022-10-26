import cv2

import numpy as np

import matplotlib.pyplot as plt



img = np.zeros([500,500,3],dtype=np.uint8)

img[:] = 255



point1 = (250, 50)

point2 = (450, 450)

point3 = (50, 450)



cv2.line(img,point1,point2,(0,0,0),6)

cv2.line(img,point2,point3,(0,0,0),6)

cv2.line(img,point3,point1,(0,0,0),6)



font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'Homework 2', (170, 350),

            font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)



cv2.imshow('First Task', img)

cv2.waitKey(0)

cv2.destroyAllWindows()