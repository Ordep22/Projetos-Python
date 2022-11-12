import cv2
import numpy as np
import os
##Importando as Imagens IHM
img1 = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina_01.jpg", cv2.IMREAD_GRAYSCALE)[:200, 600:800]
img2 = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina_01.jpg", cv2.IMREAD_GRAYSCALE)
#img2 = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/bobina_01.jpg", cv2.IMREAD_GRAYSCALE)
#Chamando a Função ORB
orb = cv2.ORB_create(nfeatures=1000)




##Destectando que são os descritores das Imagens IHM
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
#img1kp1 = cv2.drawKeypoints(img1,kp1,None)
#img2kp2 = cv2.drawKeypoints(img2,kp2,None)

##Ainda não entendi
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1,des2)
matches = sorted(matches, key=lambda x:x.distance)

##Verificando quais são as melhores conexões menores que 0.75
matching  = cv2.drawMatches(img1,kp1,img2,kp2,matches,None,flags=2)

##Imagem com as boas marcações
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[0:20],None,flags=2)



#cv2.imshow('Descriptors 1',img1kp1)
#cv2.imshow('Descriptors 2',img2kp2)
cv2.imshow('Imagem 1 ', img1)
cv2.imshow('Imagem 2 ', img2)
cv2.imshow('Imagem 3 ', img3)
cv2.waitKey(0)









