import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

while True:
    _, frame = cam.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    landmark_points = results.multi_face_landmarks
    h_frame, w_frame, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks:
            x = int(landmark.x * w_frame)
            y = int(landmark.y * h_frame)
            cv2.circle(frame, (x,y), 2, (0,255,0), -1)
            print(x, y)

    print(landmarks)
    cv2.imshow('Cam Feed', frame)
    cv2.waitKey(1)