import cv2
import mediapipe as mp
import microcontroller as mic

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tip_ids = [4, 8, 12, 16, 20]

hands = mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)  # Default to webcam

def hand_gesture_control():
    while True:
        ret, img = cap.read()
        results = hands.process(img)

        if results.multi_hand_landmarks:
            lm_list = []
            for hand_landmark in results.multi_hand_landmarks:
                my_hands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(my_hands.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
                mp_draw.draw_landmarks(img, hand_landmark, mp_hand.HAND_CONNECTIONS)

            fingers = []
            if lm_list:
                if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total = fingers.count(1)

                text = ""
                direction = mic.RCCAR(total)
                if total == 0:
                    text = "BRAKE"

                elif total == 5:
                    text = "FORWARD"

                elif total == 2:
                    text = "RIGHT"

                elif total == 3:
                    text = "LEFT"

                elif total == 4:
                    text = "REVERSE"

                cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow("Hand Gesture Control", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

hand_gesture_control()
