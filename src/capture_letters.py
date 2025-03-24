import cv2
import mediapipe as mp
import os
import time

# Initialisation Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Création du dossier dataset
dataset_dir = "alphabet_dataset"
os.makedirs(dataset_dir, exist_ok=True)

# Liste des lettres à enregistrer
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Initialisation de la capture vidéo (capture continue pendant tout le processus)
cap = cv2.VideoCapture(0)
time.sleep(1)  # Laisse le temps à la caméra de s'initialiser

if not cap.isOpened():
    print("⚠ Erreur de la caméra.")
    exit()

for letter in alphabet:
    input(f"📸 Place tes mains pour la lettre '{letter}', puis appuie sur 'Entrée' pour capturer...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠ Erreur de capture, redémarrage de la caméra...")
            cap.release()
            time.sleep(1)
            cap = cv2.VideoCapture(0)
            continue

        # Redimensionner l'image pour alléger la charge mémoire
        frame = cv2.resize(frame, (640, 480))  # Résolution plus basse

        # Retourner l'image horizontalement (effet miroir)
        frame = cv2.flip(frame, 1)

        # Conversion de l'image en RGB pour Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Dessiner les landmarks des mains
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Affichage de la fenêtre de capture
        cv2.imshow("Capture de la Lettre", frame)

        # Capture lorsque l'utilisateur appuie sur 's'
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Créer un dossier pour chaque lettre
            letter_folder = os.path.join(dataset_dir, letter)
            os.makedirs(letter_folder, exist_ok=True)
            
            # Sauvegarder l'image capturée
            file_path = os.path.join(letter_folder, f"{len(os.listdir(letter_folder))}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"✅ Image enregistrée pour '{letter}' : {file_path}")
            break  # Passe à la lettre suivante

        # Quitter si l'utilisateur appuie sur 'q'
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
