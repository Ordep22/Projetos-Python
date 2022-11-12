import numpy
import numpy as np
from matplotlib import pyplot
from PIL import Image
import matplotlib.pyplot as plt
from scipy import signal
import cv2



img = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina/01.jpg",cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/frame1774.jpg",cv2.IMREAD_GRAYSCALE)
#ret, limite = cv2.threshold (img, 200,255, cv2.THRESH_TRUNC)
#ret1, limite1 = cv2.threshold (img1, 200,255, cv2.THRESH_TRUNC)

##Filtros passa Baxixas

##Filtro Média
img2 = cv2.blur(img,(9,9))
img3 = cv2.blur(img1,(9,9))


#Filtro de mediana
##img4 = cv2.medianBlur(img,9)
##img5 = cv2.medianBlur(img1,9)

#Filtro Gaussiano
##img6 = cv2.GaussianBlur(img,(9,9),0)
#img7 = cv2.GaussianBlur(img1,(9,9),0)


#SEparando o vagão do fundo da imagem
roi_1 = cv2.absdiff(img3, img2)
#roi_2 = cv2.absdiff(img4, img5)
#roi_3 = cv2.absdiff(img6, img7)


##Printando os três resultados dos filtros
''''
plt.imshow(roi_1,cmap='gray')
plt.show()

plt.imshow(roi_2,cmap='gray')
plt.show()

plt.imshow(roi_3,cmap='gray')
plt.show()
'''

##Binarizando as Imagens IHM
##Truncada
''''
limiar_1, imglimiar_1 = cv2.threshold(roi_1,20,100,cv2.THRESH_TRUNC)
limiar_2, imglimiar_2 = cv2.threshold(roi_2,20,100,cv2.THRESH_TRUNC)
limiar_3, imglimiar_3 = cv2.threshold(roi_3,20,100,cv2.THRESH_TRUNC)
'''
##To Zero
''''
limiar_1, imglimiar_1 = cv2.threshold(roi_1,80,255,cv2.THRESH_TRUNC)
limiar_2, imglimiar_2 = cv2.threshold(roi_2,80,255,cv2.THRESH_TRUNC)
limiar_3, imglimiar_3 = cv2.threshold(roi_3,80,255,cv2.THRESH_TRUNC)


##To Zero Inverso 
limiar_1, imglimiar_1 = cv2.threshold(roi_1,80,255,cv2.THRESH_TRUNC)
limiar_2, imglimiar_2 = cv2.threshold(roi_2,80,255,cv2.THRESH_TRUNC)
limiar_3, imglimiar_3 = cv2.threshold(roi_3,80,255,cv2.THRESH_TRUNC)
'''

##Binarizada
limiar_1, imglimiar_1 = cv2.threshold(img2,160,255,cv2.THRESH_BINARY)
limiar_2, imglimiar_2 = cv2.threshold(img3,160,255,cv2.THRESH_BINARY)
limiar_3, imglimiar_3 = cv2.threshold(roi_1,40,255,cv2.THRESH_BINARY)






##Binarizada Inversa
'''
limiar_1, imglimiar_1 = cv2.threshold(roi_1,30,255,cv2.THRESH_BINARY_INV)
limiar_2, imglimiar_2 = cv2.threshold(roi_2,30,255,cv2.THRESH_BINARY_INV)
limiar_3, imglimiar_3 = cv2.threshold(roi_3,30,255,cv2.THRESH_BINARY_INV)
'''




##Transformando as Imagens IHM em matrizes

res_0 = numpy.asarray(imglimiar_1) ## Imagem com bobina
res_1 = numpy.asarray(imglimiar_2) ## Imagem sem bobina
res_2 = numpy.asarray(imglimiar_3)  ## Subtação das Imagens IHM
print(res_0.shape)


##Printando a imagem com vagão, sem vagão e a subtração (Binarizadas)

fig = plt.figure(figsize=(20,50))
ax4 = fig.add_subplot(131)
plt.imshow(imglimiar_1,cmap='gray')
plt.title('Imagem com Vagão')

ax5 = fig.add_subplot(132)
plt.imshow(imglimiar_2,cmap='gray')
plt.title('Imagem sem vagão')

ax6 = fig.add_subplot(133)
plt.imshow(imglimiar_3,cmap='gray')
plt.title('Subtração das Imagens IHM')
plt.show()


##Fazer um algoritimo para multiplicar cada a(0,0) por todos os elementos da outra matriz
# e guardar e um outro vetor de pois mostrar a imagem
##Calculando a convolução da imagem original com a de fundo retirado

#res = signal.convolve(res_1, res_0)

vet = []
for i in range(0,720):
    res = []
    x = []
    for j in range(0,1280):


        x = (res_0[i][j]) * (res_2[i][j])

## Imagem com bobina res_0
## Imagem sem bobina# res_1
##Subtação das Imagens IHM res_2


        res.append(x)


    vet.append(res)
print(vet)

produto = np.asarray(vet)

fig = plt.figure(figsize=(20,50))
ax4 = fig.add_subplot(131)
plt.imshow(res_0,cmap='gray')
plt.title('Com Bobinas')

ax5 = fig.add_subplot(132)
plt.imshow(res_2,cmap='gray')
plt.title('Subutação das Imagens IHM')


ax6 = fig.add_subplot(133)
plt.imshow(produto,cmap="gray")
plt.title('Convolução das Imagens IHM')

plt.show()




