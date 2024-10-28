import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

#Solo para probar el como se ven los landmarks en las manos(en las fotos del dataset)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.4, max_num_hands=1)

DATA_DIR = './data'

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        height, width, _ = img.shape
        img = cv2.flip(img, 1)  #la flipeamos para que la mano que dice concuerde, intenytare flipear la camara desde el datasetMaker
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        resultados = hands.process(img_rgb)
        print('Handedness:', resultados.multi_handedness)
        if resultados.multi_hand_landmarks:
            for hand_landmarks in resultados.multi_hand_landmarks:
                mp_drawing.draw_landmarks( #dibujamos lineas ------------
                    img_rgb,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        
        plt.figure()
        plt.imshow(img_rgb)
        plt.show()

hands.close();
