import cv2
import os

def video_to_frames(video, path_output_dir):
    # Vérifie si le dossier de sortie existe, sinon le crée
    if not os.path.exists(path_output_dir):
        os.makedirs(path_output_dir)

    # Ouvre la vidéo
    vidcap = cv2.VideoCapture(video)
    count = 0
    
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            # Sauvegarde l'image avec un nom basé sur l'index du frame
            cv2.imwrite(os.path.join(path_output_dir, f"{count}.png"), image)
            count += 1
        else:
            break

    # Libère les ressources
    vidcap.release()
    cv2.destroyAllWindows()

# Exemple d'utilisation
video_to_frames('videos/test.mp4', 'frames/')
