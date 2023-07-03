import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)

drawing = mp.solutions.drwing_utils()
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)


while True:
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break