import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

imgOriginal = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Imagens IHM/3.jpg")
imCorte = imgOriginal[10:220,0:1280]
imgTratada = cv2.blur(imCorte, (6,6))
print(imgOriginal.shape)

mask = np.zeros(imgTratada.shape[:2], np.uint8)
bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)
'''''
Este é rect = (start_x, start_y, width, height).

Este é o retângulo que cobre nosso objeto principal. 
O objetivo principal é encontrar as coordenadas adequadas com base 
na entrada que damos, a fim de alcançar o resultado adequado
'''

rect = (0, 10, 1300, 700)

cv2.grabCut(imgTratada, mask, rect, bgModel, fgModel, 10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = imgTratada * mask2[:, :, np.newaxis]


cv2.imwrite(os.path.join("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img","Result_01.jpg"),img)
''''
plt.subplot(121)
plt.imshow(cv2.cvtColor(cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina_01.jpg"),cv2.COLOR_BGR2GRAY), cmap='gray')
plt.title("original")
plt.xticks([])
plt.yticks([])
'''

#plt.subplot(122)
#plt.title("GrabCut")
plt.xticks([])
plt.yticks([])
plt.imshow(img)
plt.show()
