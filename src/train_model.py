import cv2
import numpy as np
import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Charger les images et les étiquettes
dataset_dir = "alphabet_dataset"
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

images = []
labels = []

# Charger les images des lettres
for letter in alphabet:
    letter_folder = os.path.join(dataset_dir, letter)
    for img_name in os.listdir(letter_folder):
        img_path = os.path.join(letter_folder, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))  # Redimensionner à 64x64 pixels
        images.append(img)
        labels.append(alphabet.index(letter))  # Étiquette correspondante à la lettre

images = np.array(images)
labels = np.array(labels)

# Normalisation des images
images = images / 255.0

# Conversion des labels en catégories (one-hot encoding)
labels = to_categorical(labels, num_classes=len(alphabet))

# Diviser les données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# Créer le modèle CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(alphabet), activation='softmax')  # Une sortie pour chaque lettre
])

# Compiler le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraîner le modèle
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Sauvegarder le modèle
model.save('lsf_model.h5')

# Évaluer le modèle sur les données de test
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc}")
