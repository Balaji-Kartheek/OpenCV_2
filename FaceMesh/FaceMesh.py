import cv2
import mediapipe as mp
import time


mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 2)
mpDraw = mp.solutions.drawing_utils
drawSpecs = mpDraw.DrawingSpec(thickness=1,circle_radius=2)

cap = cv2.VideoCapture('Resources/video1.mp4')

prevtime = 0
while True:
    success, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgrgb)

    if results.multi_face_landmarks:
        for facelnds in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img,facelnds,mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpecs,drawSpecs)


    currtime = time.time()
    fps = 1 / (currtime - prevtime)
    prevtime = currtime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("myVideo",img)
    cv2.waitKey(1)