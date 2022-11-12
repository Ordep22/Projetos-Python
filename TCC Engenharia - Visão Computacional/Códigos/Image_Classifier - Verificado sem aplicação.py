import cv2
import numpy as np
import os

path = '/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM'
orb = cv2.ORB_create(nfeatures=1000)

##Importando as Imagens IHM
images = []
classNames = []
myList = os.listdir(path)
# print(f'O número de arquicos encontrados neste diretório foi: {len(myList)}')

for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
#print(classNames)


##Determinando os descritores das Imagens IHM em uma lista
def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img,None)
        desList.append(des)

    return desList

def finId(img, desList):
    kp2, des2 = orb.detectAndCompute(img,None)
    bf = cv2.BFMatcher()
    for des in desList:
        matches = bf.match(des, des2)
        good = []
        good.append([matches])

desList = findDes(images)
cap = cv2.VideoCapture("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Vídeos Resende - Bobinas CG/c-01-20200722-095244.mov")

while True:
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    finId(img2,desList)
    cv2.imshow('Gravacao',imgOriginal)
    cv2.waitKey(1)
    


###Ainda não entendi
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
# matches = bf.match(des1,des2)
# matches = sorted(matches, key=lambda x:x.distance)
#


#
#
#
##cv2.imshow('Descriptors 1',img1kp1)
##cv2.imshow('Descriptors 2',img2kp2)
# cv2.imshow('Imagem 1 ', img1)
# cv2.imshow('Imagem 2 ', img2)
# cv2.imshow('Imagem 2 ', img3)
# cv2.waitKey(0)
