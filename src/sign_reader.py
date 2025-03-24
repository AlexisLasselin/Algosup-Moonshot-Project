import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Charger le modèle pré-entraîné
model = tf.keras.models.load_model('lsf_model.h5')

# Initialiser Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Démarrer la capture vidéo
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Effet miroir
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détection des mains
    hand_results = hands.process(rgb_frame)

    h, w, c = frame.shape  # Dimensions du cadre

    # Vérifier les mains détectées
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Convertir l'image de la main en format utilisable par le modèle
            hand_image = frame[100:400, 100:400]  # Zone autour des mains, à ajuster selon tes besoins
            hand_image = cv2.resize(hand_image, (64, 64))
            hand_image = np.expand_dims(hand_image, axis=0)  # Ajouter une dimension pour correspondre à l'entrée du modèle
            hand_image = hand_image / 255.0  # Normaliser l'image

            # Prédire la lettre
            prediction = model.predict(hand_image)
            predicted_class = np.argmax(prediction, axis=1)
            predicted_letter = chr(predicted_class + ord('A'))  # Convertir l'indice en lettre

            # Afficher la lettre prédite sur l'image
            cv2.putText(frame, f"Lettre: {predicted_letter}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Affichage du cadre avec la lettre prédite
    cv2.imshow("Reconnaissance des mains", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
