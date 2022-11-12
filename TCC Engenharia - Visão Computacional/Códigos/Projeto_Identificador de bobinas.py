import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import os
from time import sleep
from pathlib import Path
import PILasOPENCV as ImageFont

video = cv.VideoCapture("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Vídeos Resende - Bobinas CG/c-01-20200722-095244.mov")
path_01 = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM'
path_02 = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/imagens_grabCut'
path_03 = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Resultados'


def roda_video(x):
    ###Próximos passos fazer o programa selecionar as Imagens IHM a cada 1 segunda
    # É uma função que permite a manipulação de arquivos em diretórios específicos
    # Realiza a abertura do vídeo a partir do caminho indicado

    ##Caso a pasta "Imagens IHM" não tenha sido criada a função os.path.exists irá criá-la
    if not os.path.exists('../Frame vagoes'):
        os.makedirs('../Frame vagoes')

    ##Faz a captura dos frames até que ret receba o valo nulo, quando isso acontecer o loop se incerrará
    index = 0

    while (x.isOpened()):
        frameId = x.get(1)  # current frame number
        ret, frame = x.read()

        if (ret != True):
            break

        #if index % 10 == 0:

        name = './Imagens IHM/' + str(index) + '.jpg'
        print('Creating...' + name)
        cv.imwrite(name, frame)

        index += 1


def grab_cut(a, b):
    ##Caso não exista o repositório o software irá criar
    if not os.path.exists('../Frame vagoes Grabcut'):
        os.makedirs('../Frame vagoes Grabcut')
    index = 0


    arquivos = os.listdir(a)
    lista = sorted(arquivos)

    print(lista)

    for y in lista:
        if y != '.DS_Store':
            path_01 = a + '/' + y
            img = cv.imread(path_01)
            img_00 = img[0:215, 0:1280]


            mask = np.zeros(img_00.shape[:2], np.uint8)
            bgModel = np.zeros((1, 65), np.float64)
            fgModel = np.zeros((1, 65), np.float64)
            rect = (5, 10, 1300, 720)

            cv.grabCut(img_00, mask, rect, bgModel, fgModel, 10,cv.GC_INIT_WITH_RECT)
            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
            img_01 = img_00 * mask2[:, :, np.newaxis]



            #plt.imshow(img_01)
            #plt.show()

            path_02 = b + '/'+ str(index) + '.jpg'
            print('Creating...'+'GrabCut'+ str(index))
            cv.imwrite(path_02, img_01)
            index += 1



def detec_circulo(a, b, c):

    if not os.path.exists('../Resultados'):
        os.makedirs('ciculos')

    index = 0

    arquivos = os.listdir(a)
    lista = sorted(arquivos)

    print(lista)

    for x in lista:

        if x != '.DS_Store':

            # path_a = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/imagens_grabCut'
            # path_b = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Resultados'
            # path_c = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM'


            path_01 = a + '/' + x
            path_02 = c + '/' + x

            #print(path_02)

            img_1 = cv.imread(path_01)
            img_2 = cv.imread(path_02)

            ##Esta paste vai ser importante para o apresentação de resultados, visto que posso criar uma tabela para representar
            ## os melhores parâmtros encontrados

            #Bom resultado com esses parâmetros
            grey = cv.blur(img_1, (9,9))
            grey_01 = cv.GaussianBlur(grey, (9, 9), 3)
            canny = cv.Canny(grey_01, 100, 200)
            circles = cv.HoughCircles(canny, cv.HOUGH_GRADIENT, dp=2,minDist=125,param1=50,param2=31,minRadius=60,maxRadius=105)


            circles = np.uint16(np.around(circles))
            cimg = img_1.copy()

            for i in circles[0, :]:
                # draw the outer circle
                cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                # cv.circle(cimg, (i[0], i[1]), 2, (255, 0, 0), 10)
            print(circles)

            # Convert to PIL Image
            cv2_im_rgb = cv.cvtColor(cimg, cv.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im_rgb)
            draw = ImageDraw.Draw(pil_im)
            # Choose a font

            # Draw the text
            nun_bob = np.shape(circles)
            # draw.text((0, 0), f'O foram identificadas {nun_bob[1]} bobinas', fill = "green",font = 0)
            draw.text((5, 5), f'O foram identificadas {nun_bob[1]} bobinas', fill="white", align="low")


            # Save the imag
            cv_im_processed = pil_im.getim()
            path_03 = b + '/'+ str(index) + '.jpg'
            print('Creating... ciculos' + str(index))
            cv.imwrite(path_03, cv_im_processed)

            #plt.imshow(cv_im_processed)
            #plt.show()


            index = index +1

#frames  = roda_video(video)
#GB = grab_cut(path_01,path_02)
bobinas = detec_circulo(path_02, path_03, path_01)

'''
img = cv.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM/197.jpg")
imgc = img [0:220,0:1280]
plt.imshow(imgc)
plt.show()
'''