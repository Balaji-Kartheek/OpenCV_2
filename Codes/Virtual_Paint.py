import cv2
import numpy as np



framewidth = 640
frameheight = 400

cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,150)    # setting up the brightness

# color list

myColors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

# Creating the mask of the color

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        #cv2.imshow(str(color[0]),mask)





while True:
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# to find the colors

