import cv2

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("lena.jpg")
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


# using the CascadeClassifier instance to detect images
faces = faceCascade.detectMultiScale(imgGrey,1.1,4)  # scale factor, min. neighbours

#creating bounding box

for (x,y,wid,ht) in faces:
    cv2.rectangle(img,(x,y),(x+wid,y+ht),(255,0,0),2)   # initial,corner diagonal, color,thickness

cv2.imshow("Output",img)
cv2.imshow("Grey Image",imgGrey)
cv2.waitKey(0)