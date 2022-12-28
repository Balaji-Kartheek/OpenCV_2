import cv2
import numpy as np

img = cv2.imread("lena.png")
kernel = np.ones((5,5),np.uint8)  # values range(0-255)

imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(61,61),0)
imgCanny = cv2.Canny(img,100,100)   # detects the edges
imgDialation = cv2.dilate(imgCanny,kernel,iterations =1)  # increases the thickness
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)   # minpooling for dilated image



cv2.imshow("Grey_Scale",imgGrey)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)

