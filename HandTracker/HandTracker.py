import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

currtime = 0
prevtime = 0

while True:
    success,img = cap.read()
    imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)

    if results.multi_hand_landmarks:
        for hndmrks in results.multi_hand_landmarks:

            # locating the landmark positions
            for id,lm in enumerate(hndmrks.landmark):
                #print(id,lm)
                h,w,d = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)   # pixel values
                print(id,cx,cy)


                # locating a particular handmark and modifying it
                if id==8:
                    cv2.circle(img , (cx,cy), 20 , (255,255,0), cv2.FILLED)

            mpDraw.draw_landmarks(img,hndmrks,mphands.HAND_CONNECTIONS)

    currtime = time.time()
    fps = 1/(currtime-prevtime)
    prevtime = currtime

    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)
    cv2.imshow("Video",img)

    cv2.waitKey(1)