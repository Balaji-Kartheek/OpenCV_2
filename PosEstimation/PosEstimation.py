import cv2
import mediapipe as mp
import time


mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture('Resources/video4.mp4')

prevtime = 0
while True:
    success, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgrgb)


    if results.pose_landmarks:
        for lndmrks in results.pose_landmarks.landmark:

            # locating the landmark positions
            for id,lm in enumerate(results.pose_landmarks.landmark):
                #print(id,lm)
                h,w,d = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)   # pixel values
                print(id,cx,cy)


                # locating a particular handmark and modifying it
                if id==12:
                    cv2.circle(img , (cx,cy), 20 , (255,255,0), cv2.FILLED)

        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)

    currtime = time.time()
    fps = 1 / (currtime - prevtime)
    prevtime = currtime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow("myVideo",img)
    cv2.waitKey(1)