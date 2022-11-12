import cv2
import numpy as np

img_1 = cv2.imread("/TCC-1/img/bobina_01.jpg", cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread("/TCC-1/img/bobina_02.jpg", cv2.IMREAD_GRAYSCALE)

roi_1  = img_1[0:200,600:800]
roi_2  = img_2[0:200,600:800]

sift = cv2.xfeatures2d.SIFT_create()

'''
surf = cv2.xfeatures2d.SURF_create()
Não funciona, mesmo que a patente já tenha vencido. 
Não encontrie um modo de usar esse método.
'''
orb = cv2.ORB_create(nfeatures=2500)


kp_1,dp_1 =orb.detectAndCompute(roi_1,None)
kp_2, dp_2 = orb.detectAndCompute(img_2,None)


##Descritores das regiões de interesse
##-> Proximo passo é construir um banco de dados com os descretores de todas os frames das Imagens IHM
'''
for c in dp_1:
    print(dp_1)
'''


roi_1 = cv2.drawKeypoints(roi_1,kp_1,None)
roi_2 = cv2.drawKeypoints(roi_2,kp_2,None)


cv2.imshow("Reg. de Interesse 1", roi_1)
cv2.imshow("Reg. de Interesse 2",roi_2)
cv2.waitKey(0)
cv2.destroyAllWindows()














