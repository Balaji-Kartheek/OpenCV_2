import cv2


img = cv2.imread("merci.jpg")

print(img.shape)
# resize image

imgResize = cv2.resize(img,(200,180))   #wid*height
print(imgResize.shape)

imgCropped = img[0:200,200:500]     # ht*width

cv2.imshow("Image",img)
cv2.imshow("Resize Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)
