import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

#img[:] = 255,255,0
#print(img.shape)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  # starting, ending,color,thickness
cv2.rectangle(img,(0,0),(250,250),(255,0,0),cv2.FILLED)
cv2.circle(img,(350,100),50,(0,0,255),5)
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,200.8),2)  # 1 is scale

cv2.imshow("Image",img)
cv2.waitKey(0)