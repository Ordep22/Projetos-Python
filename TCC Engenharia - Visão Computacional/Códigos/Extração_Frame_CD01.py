
###Próximos passos fazer o programa selecionar as Imagens IHM a cada 1 segunda
import cv2
import numpy as np
import os
import math
from time import sleep

delay = 120  # FPS do vídeo
#É uma função que permite a manipulação de arquivos em diretórios específicos
# Realiza a abertura do vídeo a partir do caminho indicado

vid = cv2.VideoCapture('/Users/PedroVitorPereira/Documents/GitHub/Projetos-Python/TCC Engenhatia Mecatronica/Vídeos Resende - Bobinas CG/c-01-20200722-095244.mov')

##Caso a pasta "Imagens IHM" não tenha sido criada a função os.path.exists irá criá-la
if not os.path.exists('Teste'):
    os.makedirs('Teste')

##Faz a captura dos frames até que ret receba o valo nulo, quando isso acontecer o loop se incerrará



index = 0

while(vid.isOpened()):
    tempo = float(1 / delay)
    sleep(tempo)



    frameId = vid.get(1) #current frame number
    ret, frame = vid.read()

    if (ret != True):
        break

    if index%20 == 0:
        name = './Teste/frame' + str(index) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)


    index+=1


















