import cv2
import mediapipe as mp

# Init mediapipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
face = mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Face keypoints
face_keypoints = {
    "cheek": [205, 123, 192, 425, 416, 352],
    "eyes": [33, 133, 362, 263],
    "ears": [127, 93, 323, 356],
    "forehead": [67, 10, 297],
    "mouth": [61, 291, 13, 14],
    "chin": [170, 199, 395],
    "nose": [2, 5, 6]
}

# Capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detection
    hand_results = hands.process(rgb_frame)
    face_results = face.process(rgb_frame)

    # Draw hands (if needed)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Draw only face keypoints and connect them
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            # Get face keypoints
            keypoint_positions = {}
            for key, value in face_keypoints.items():
                keypoint_positions[key] = []
                for i in value:
                    if i < len(face_landmarks.landmark):
                        lm = face_landmarks.landmark[i]
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        keypoint_positions[key].append((cx, cy))

            # Draw circles and connect the keypoints
            for key, points in keypoint_positions.items():
                for i in range(len(points)):
                    cv2.circle(frame, points[i], 5, (0, 255, 0), cv2.FILLED)

                # Mouth: connect to form a diamond shape
                if key == "mouth":
                    cv2.line(frame, points[0], points[2], (0, 255, 0), 2)  
                    cv2.line(frame, points[1], points[3], (0, 255, 0), 2)  
                    cv2.line(frame, points[2], points[1], (0, 255, 0), 2)  
                    cv2.line(frame, points[3], points[0], (0, 255, 0), 2) 

                # Eyes: connect the points to form complete eyes (not two lines)
                if key == "eyes":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[2], points[3], (0, 255, 0), 2) 
                
                if key == "nose":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[1], points[2], (0, 255, 0), 2)

                if key == "forehead":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[1], points[2], (0, 255, 0), 2)

                if key == "chin":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[1], points[2], (0, 255, 0), 2)

                if key == "ears":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[2], points[3], (0, 255, 0), 2)

                if key == "cheek":
                    cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                    cv2.line(frame, points[1], points[2], (0, 255, 0), 2)
                    cv2.line(frame, points[2], points[0], (0, 255, 0), 2)
                    cv2.line(frame, points[3], points[4], (0, 255, 0), 2)
                    cv2.line(frame, points[4], points[5], (0, 255, 0), 2)
                    cv2.line(frame, points[5], points[3], (0, 255, 0), 2)

    # Display
    cv2.imshow("LSF Dataset Capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
