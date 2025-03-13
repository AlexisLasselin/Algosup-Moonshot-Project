import cv2
import mediapipe as mp
import json
import os
import collections

# Initialisation Mediapipe
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
face = mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Définition des points clés
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

# Création du dossier dataset
dataset_dir = "data"
os.makedirs(dataset_dir, exist_ok=True)

# Demander le nom du geste
gesture_name = input("Nom du geste (ex: bonjour, merci, oui) : ")
file_path = os.path.join(dataset_dir, f"{gesture_name}.json")

# Initialisation de la capture vidéo
cap = cv2.VideoCapture(0)
sequence_length = 30  # Nombre d'images à enregistrer pour un geste
gesture_sequence = collections.deque(maxlen=sequence_length)

print("Commence à signer ! (Appuie sur 'q' pour arrêter l'enregistrement)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Effet miroir
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détection des mains, du visage et du corps
    hand_results = hands.process(rgb_frame)
    face_results = face.process(rgb_frame)
    pose_results = pose.process(rgb_frame)

    h, w, c = frame.shape  # Dimensions de l'image

    # Stocker les positions pour cette frame
    frame_data = {"hands": [], "face": {}, "pose": {}}

    # Détection des mains
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            hand_data = [[lm.x, lm.y] for lm in hand_landmarks.landmark]
            frame_data["hands"].append(hand_data)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Détection du visage
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            for key, indices in face_keypoints.items():
                frame_data["face"][key] = [[face_landmarks.landmark[i].x, face_landmarks.landmark[i].y] for i in indices]
                for i in indices:
                    cx, cy = int(face_landmarks.landmark[i].x * w), int(face_landmarks.landmark[i].y * h)
                    cv2.circle(frame, (cx, cy), 3, (0, 255, 0), -1)

    # Détection du corps
    if pose_results.pose_landmarks:
        for key, indices in pose_keypoints.items():
            frame_data["pose"][key] = [[pose_results.pose_landmarks.landmark[i].x, pose_results.pose_landmarks.landmark[i].y] for i in indices]
            for i in indices:
                cx, cy = int(pose_results.pose_landmarks.landmark[i].x * w), int(pose_results.pose_landmarks.landmark[i].y * h)
                cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)

    # Correction des erreurs OpenCV (conversion des coordonnées)
    def draw_line(key1, key2, color):
        if key1 in frame_data["pose"] and key2 in frame_data["pose"]:
            pt1 = (int(frame_data["pose"][key1][0][0] * w), int(frame_data["pose"][key1][0][1] * h))
            pt2 = (int(frame_data["pose"][key2][0][0] * w), int(frame_data["pose"][key2][0][1] * h))
            cv2.line(frame, pt1, pt2, color, 3)

    # Connexions entre les points du corps
    draw_line("shoulders", "elbows", (255, 0, 0))
    draw_line("shoulders", "hips", (255, 0, 0))
    draw_line("elbows", "wrists", (255, 0, 0))
    draw_line("hips", "shoulders", (255, 0, 0))

    # Ajouter cette frame à la séquence
    gesture_sequence.append(frame_data)

    # Affichage en temps réel
    cv2.putText(frame, f"Enregistrement: {gesture_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Enregistrement du Geste", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Sauvegarde du fichier JSON
data = {"gesture": gesture_name, "frames": list(gesture_sequence)}
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)

print(f"✅ Geste '{gesture_name}' enregistré avec succès dans {file_path}")
