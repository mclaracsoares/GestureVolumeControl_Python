import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL

def set_volume(level):
    """
    Ajusta o volume do sistema com base no número de dedos levantados.
    - level: Número de dedos levantados (0 a 5).
    """
    volume = level / 5  # Converte o número de dedos para uma escala de 0.0 a 1.0
    devices = AudioUtilities.GetAllSessions()

    for session in devices:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            volume_interface.SetMasterVolume(volume, None)

# Inicializa a captura de vídeo (webcam)
video = cv2.VideoCapture(0)
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDesenho = mp.solutions.drawing_utils

while True:
    sucess, img = video.read()
    fRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resultado = Hands.process(fRGB)
    handPoints = resultado.multi_hand_landmarks

    h, w, _ = img.shape
    coordenadas = []

    if handPoints:
        for pontosMao in handPoints:
            mpDesenho.draw_landmarks(img, pontosMao, hands.HAND_CONNECTIONS)
            for id, cord in enumerate(pontosMao.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                coordenadas.append((cx, cy))

            finger = [8, 12, 16, 20]
            cont = 0

            if coordenadas:
                if coordenadas[4][0] < coordenadas[3][0]:
                    cont += 1
                for x in finger:
                    if coordenadas[x][1] < coordenadas[x-2][1]:
                        cont += 1

            print(f"Número de dedos levantados: {cont}")
            set_volume(cont)

            cv2.rectangle(img, (80, 10), (200, 110), (255, 0, 0), -1)
            cv2.putText(img, str(cont), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)

    cv2.imshow('Imagem', img)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        break

video.release()
cv2.destroyAllWindows()
