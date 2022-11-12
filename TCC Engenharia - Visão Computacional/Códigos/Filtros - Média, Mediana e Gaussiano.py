import cv2 as cv

img  = cv.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img/bobina_01.jpg")
img_01 = cv.blur(img,(5,5))
img_02 = cv.medianBlur(img,5)
img_03 = cv.GaussianBlur(img,(5,5),0)


cv.imshow("Imagem Original",img)
cv.imshow("Imagem Tratada Media",img_01)
cv.imshow("Imagem Tratada Mediana",img_02)
cv.imshow("Imagem Tratada Gaussiana",img_03)





cv.waitKey(0)
cv.destroyAllWindows()