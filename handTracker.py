import cv2
import mediapipe as mp
import math
#test
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def lineLength(wx, wy):
    wx1, wy1 = wx[1], wx[2]
    wx2, wy2 = wy[1], wy[2]
    return math.sqrt(((wx2 - wx1) ** 2) + ((wy2 - wy1) ** 2))

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        counter = 0
        landmarks = []
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmarks.append([counter, cx, cy])
                counter += 1
                if counter > 20:
                    counter = 0 

            #thumb
            print(lineLength(landmarks[4], landmarks[2]))
            #index
            print(lineLength(landmarks[8], landmarks[5]))
            #middle
            print(lineLength(landmarks[12], landmarks[9]))
            #ring
            print(lineLength(landmarks[16], landmarks[13]))
            #pinkie
            print(lineLength(landmarks[20], landmarks[17]))
            #index to middle
            print(lineLength(landmarks[8], landmarks[12]))
            #ring to middle
            print(lineLength(landmarks[16], landmarks[12]))
            #pinkie to ring
            print(lineLength(landmarks[16], landmarks[20]))


            landmarks = []
            mpDraw.draw_landmarks(image,handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracker", image)
    cv2.waitKey(1)