import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import os
import time

capture = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)

offset = 20
imgSize = 300

folder = "src/lsf_dataset/Y"  # Change the place where you want to save the images
counter = 0

while True:
    success, img = capture.read()
    hands, img = detector.findHands(img, flipType=True)
    if hands:
        hand = hands[0]
        x, y, w, h = hand["bbox"]

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset : y + h + offset, x - offset : x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - imgResizeShape[1]) / 2)
            imgWhite[0 : imgResizeShape[0], wGap : wGap + imgResizeShape[1]] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - imgResizeShape[0]) / 2)
            imgWhite[hGap : hGap + imgResizeShape[0], 0 : imgResizeShape[1]] = imgResize

        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord("s"):
        cv2.imwrite(f"{folder}/Image_{time.time()}.jpg", imgWhite)
        counter += 1
        print("Saved", counter)
        print("Total images in folder:", len(os.listdir(folder)))

    if key == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
