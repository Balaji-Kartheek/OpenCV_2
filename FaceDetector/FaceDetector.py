import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture("Resources/data.mp4")
prevtime = 0

mpFaces = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils

# there are 6 points on the face

faceDetection = mpFaces.FaceDetection(0.75)

while True:
    success,img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgrgb)

    #print(results)

    if results.detections:
        for id,detection in enumerate(results.detections):
            # mpDraw.draw_detection(img,detection)
            bboxC = detection.location_data.relative_bounding_box
            h,w,c = img.shape
            bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                   int(bboxC.width * w), int(bboxC.height *h)

            cv2.rectangle(img,bbox,(255,0,255),2)
            cv2.putText(img, f'FPS: {int(detection.score[0]*100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 3,
                        ( 255, 0,255), 3)

    currtime = time.time()
    fps = 1 / (currtime - prevtime)
    prevtime = currtime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 3)

    cv2.imshow("Video", img)
    cv2.waitKey(1)