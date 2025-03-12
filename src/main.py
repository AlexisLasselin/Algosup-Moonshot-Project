import cv2
import mediapipe as mp

# Initialize Mediapipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
face = mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Define keypoints
face_keypoints = {
    "cheek": [205, 123, 192, 425, 416, 352],
    "eyes": [33, 133, 362, 263],
    "ears": [127, 93, 323, 356],
    "forehead": [67, 10, 297],
    "mouth": [61, 291, 13, 14],
    "chin": [170, 199, 395],
    "nose": [2, 5, 6]
}

pose_keypoints = {
    "shoulders": [11, 12],
    "elbows": [13, 14],
    "hips": [23, 24],
    "wrists": [15, 16]
}

# Capture video
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
    pose_results = pose.process(rgb_frame)

    h, w, c = frame.shape  # Get frame dimensions

    # Store wrist positions from hands
    wrist_positions = {"left": None, "right": None}

    # Draw hands and get wrist positions
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get wrist keypoints (0 is the wrist in Mediapipe Hands)
            wrist_x = int(hand_landmarks.landmark[0].x * w)
            wrist_y = int(hand_landmarks.landmark[0].y * h)

            # Determine if it's left or right hand
            hand_label = "right" if wrist_x > w / 2 else "left"
            wrist_positions[hand_label] = (wrist_x, wrist_y)

    # Draw face keypoints
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            keypoint_positions = {}
            for key, indices in face_keypoints.items():
                keypoint_positions[key] = []
                for i in indices:
                    if i < len(face_landmarks.landmark):
                        lm = face_landmarks.landmark[i]
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        keypoint_positions[key].append((cx, cy))

            # Draw face keypoints
            for key, points in keypoint_positions.items():
                for i in range(len(points)):
                    cv2.circle(frame, points[i], 5, (0, 255, 0), cv2.FILLED)

                # Mouth: connect to form a diamond shape
                if key == "mouth":
                    cv2.line(frame, points[0], points[2], (0, 255, 0), 2)  
                    cv2.line(frame, points[1], points[3], (0, 255, 0), 2)  
                    cv2.line(frame, points[2], points[1], (0, 255, 0), 2)  
                    cv2.line(frame, points[3], points[0], (0, 255, 0), 2) 

                # Eyes: connect to form two proper eye shapes
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
    # Draw Pose keypoints (shoulders, elbows, hips)
    if pose_results.pose_landmarks:
        pose_landmarks = pose_results.pose_landmarks.landmark
        keypoint_positions = {}

        # Extract required pose keypoints
        for key, indices in pose_keypoints.items():
            keypoint_positions[key] = []
            for i in indices:
                lm = pose_landmarks[i]
                cx, cy = int(lm.x * w), int(lm.y * h)
                keypoint_positions[key].append((cx, cy))

        # Draw the extracted pose keypoints
        for key, points in keypoint_positions.items():
            for point in points:
                cv2.circle(frame, point, 6, (255, 0, 0), cv2.FILLED)  # Blue circles for pose keypoints

        # Connect shoulders, elbows, and hips
        cv2.line(frame, keypoint_positions["shoulders"][0], keypoint_positions["shoulders"][1], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["shoulders"][0], keypoint_positions["elbows"][0], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["shoulders"][1], keypoint_positions["elbows"][1], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["hips"][0], keypoint_positions["hips"][1], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["shoulders"][0], keypoint_positions["hips"][0], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["shoulders"][1], keypoint_positions["hips"][1], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["elbows"][0], keypoint_positions["wrists"][0], (255, 0, 0), 3)
        cv2.line(frame, keypoint_positions["elbows"][1], keypoint_positions["wrists"][1], (255, 0, 0), 3)

    # Display
    cv2.imshow("Body recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
