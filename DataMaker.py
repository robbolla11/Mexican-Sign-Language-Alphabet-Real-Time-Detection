import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOLA']

letras = ['P','U','V','D','Z']
#TODO tal vez agregar palabras si es que hay formas de hacerlas(investigar)

#porfavor no me hagan volver a tomar las fotos
nFotos = 100

cam = cv2.VideoCapture(0)


def begin(letra_actual):

    message = 'Presiona cualquier tecla para iniciar'
    while True:
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        text_size = cv2.getTextSize(message, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = int((frame.shape[1] - text_size[0]) / 2)
        cv2.putText(frame, message, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        #cv2.imshow('frame', cv2.flip(frame, 1))
        #esto hace que el texto salga invertido
        key = cv2.waitKey(1) & 0xFF
        if key != 255:  
            break

def capture_letter_photos(letra_actual):
    carpetaLetra = os.path.join(DATA_DIR, letra_actual)

    if not os.path.exists(carpetaLetra):
        os.makedirs(carpetaLetra)

    while True:
        contador = 0
        while contador < nFotos:
            ret, frame = cam.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
            #cv2.imshow('frame', cv2.flip(frame, 1))
            cv2.waitKey(50)
            nombreFoto = f'{letra_actual}_{contador}_D.jpg'
            rutaFoto = os.path.join(carpetaLetra, nombreFoto)
            cv2.imwrite(rutaFoto, frame)
            contador += 1

        while True:
            ret, frame = cam.read()
            frame = cv2.flip(frame, 1)
            text = f'R para reiniciar, Enter para continuar'
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
            text_x = int((frame.shape[1] - text_size[0]) / 2)
            cv2.putText(frame, text, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            #cv2.imshow('frame', cv2.flip(frame, 1))
            key = cv2.waitKey(1) & 0xFF
            if key == ord('r'):
                #Eliminar
                files = os.listdir(carpetaLetra)
                for file_name in files:
                    file_path = os.path.join(carpetaLetra, file_name)
                    os.remove(file_path)
                print(f'Archivos eliminados en {carpetaLetra}')
                break
            elif key == 13:  #Enter
                return

def capture_letter_photos2(letra_actual):
    carpetaLetra = os.path.join(DATA_DIR, letra_actual)

    if not os.path.exists(carpetaLetra):
        os.makedirs(carpetaLetra)

    while True:
        contador = 0
        while contador < nFotos:
            ret, frame = cam.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
            #cv2.imshow('frame', cv2.flip(frame, 1))
            cv2.waitKey(50)
            nombreFoto = f'{letra_actual}_{contador}_I.jpg'
            rutaFoto = os.path.join(carpetaLetra, nombreFoto)
            cv2.imwrite(rutaFoto, frame)
            contador += 1

        while True:
            ret, frame = cam.read()
            frame = cv2.flip(frame, 1)
            text = f'R para reiniciar, Enter para continuar'
            text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
            text_x = int((frame.shape[1] - text_size[0]) / 2)
            cv2.putText(frame, text, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            #cv2.imshow('frame', cv2.flip(frame, 1))
            key = cv2.waitKey(1) & 0xFF
            if key == ord('r'):
                #Eliminar
                files = os.listdir(carpetaLetra)
                for file_name in files:
                    file_path = os.path.join(carpetaLetra, file_name)
                    os.remove(file_path)
                print(f'Archivos eliminados en {carpetaLetra}')
                break
            elif key == 13:  #Enter
                return

begin('Inicio')

for letra in letras:
    capture_letter_photos(letra)
    capture_letter_photos2(letra) #esto es una mamada pero sirve

cam.release()
cv2.destroyAllWindows()

