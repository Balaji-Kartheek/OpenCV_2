import cv2

# video is a sequence of words

cap = cv2.VideoCapture("video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break