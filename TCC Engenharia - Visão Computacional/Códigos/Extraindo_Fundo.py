import cv2
import numpy as np

import os

path = "/Users/PedroVitorPereira/Documents/GitHub/Projetos-Python/TCC Engenhatia Mecatronica/Frame vagoes"
img = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM/frame1966.jpg")

mylist = os.listdir(path)
imgesderetorio = []
classname = []
des = []
for m in mylist:
    img1 = cv2.imread(f'{path}/{m}', 0)
    imgesderetorio.append(img1)
    classname.append(os.path.splitext(m)[0])

print(type(classname))
print(type(imgesderetorio))
print(type(img1))











