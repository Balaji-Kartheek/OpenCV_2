import cv2
# import face_recognition

frame  = cv2.imread("face.jpg")
frame2  = cv2.imread("face.jpg")

IMG_SIZE = 224

# cropping the center part of each frame and working on that

y, x = frame.shape[0:2]
min_dim = min(y, x)
start_x = (x // 2) - (min_dim // 2)
start_y = (y // 2) - (min_dim // 2)
frame = frame[start_y : start_y + min_dim, start_x : start_x + min_dim]






cv2.imshow("Image",frame)
cv2.imshow("Actual Image",frame2)

cv2.waitKey(0)
