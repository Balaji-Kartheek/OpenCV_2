import cv2




'''
# read image
#img = cv2.imread('Resources/profile.jpeg')


cv2.imshow("Image_Output",img)
cv2.waitKey(5)

'''

# read an video
#cap = cv2.VideoCapture('Resources/how-to-download-youtube-videos-youtube-video-kaise-download-kare-easy-tips.mp4')


# Online Videocapturing
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


while True:
    success,img = cap.read()
    cv2.imshow("Video",img)
    if(cv2.waitKey(1)  & 0xFF  == ord('q')):
        break 
