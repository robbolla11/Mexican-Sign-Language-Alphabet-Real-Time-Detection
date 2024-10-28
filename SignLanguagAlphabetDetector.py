import pickle
import cv2
import mediapipe as mp
import numpy as np

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.6, max_num_hands=1)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOLA']
letrasDicc = {letra: letra for letra in letras}

letrasGuardadas = []

cap = cv2.VideoCapture(0) #creo que hay que cambiar el 0 por otro num dependiendo del dispositivo

while True:
    dataNorm = []
    xLand = []
    yLand = []
    zLand = []

    ret, img = cap.read()
    img = cv2.flip(img, 1)
    height, width, _ = img.shape

    fuenteLetra = cv2.FONT_HERSHEY_COMPLEX

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    resultados = hands.process(img_rgb)
    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in resultados.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                z = hand_landmarks.landmark[i].z

                xLand.append(x)
                yLand.append(y)
                zLand.append(z)

        #normalizacion, rendimiento no cambia mucho pero siento que es mejor con esta
        #es necesaria pq ya entrene el modelo con normalizacion y que flojera entrenarlo de nuevo
        for i in range(len(hand_landmarks.landmark)):
            x = hand_landmarks.landmark[i].x
            y = hand_landmarks.landmark[i].y
            z = hand_landmarks.landmark[i].z
            dataNorm.append(x - min(xLand))
            dataNorm.append(y - min(yLand))
            dataNorm.append(z - min(zLand))
            #dataNorm.append(xLand)
            #dataNorm.append(yLand)
            #dataNorm.append(zLand)

        x1 = int(min(xLand) * width)
        y1 = int(min(yLand) * height)

        prediccion = model.predict([np.asarray(dataNorm)]) #prediccion con nuestro modelo segun los landmarks
        letraPredicha = letrasDicc[prediccion[0]] #letra que devuelve

        #letra actual con borde negro puesto horrible
        cv2.putText(img, letraPredicha, (x1+10,y1-25), fuenteLetra, 1.6, (0, 0, 0), 6, cv2.LINE_AA) 
        cv2.putText(img, letraPredicha, (x1+10,y1-25), fuenteLetra, 1.6, (255, 255, 255), 2, cv2.LINE_AA)

    key = cv2.waitKey(1)
    if key == 13: #Enter
        letrasGuardadas.append(letraPredicha)
    elif key == 32: #Espacio
        letrasGuardadas.append(' ')
    elif key == 8: #Backspace o como se llame <-
        if letrasGuardadas:
            letrasGuardadas.pop()
    elif key == 27: #Esc
        break

    if len(letrasGuardadas) > 20:
        letrasGuardadas = []

    palabraForm = ''.join(letrasGuardadas)
    cv2.putText(img, palabraForm, (10, height - 10), fuenteLetra, 1.4, (0, 0, 0), 6, cv2.LINE_AA)
    cv2.putText(img, palabraForm, (10, height - 10), fuenteLetra, 1.4, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('img', img)

cap.release()
cv2.destroyAllWindows()
