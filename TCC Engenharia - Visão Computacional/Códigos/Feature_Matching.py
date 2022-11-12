import cv2
import numpy as np

img_1  = cv2.imread("/TCC-1/img/bobina_01.jpg", cv2.IMREAD_GRAYSCALE)
img_2 = cv2.imread("/TCC-1/img/bobina_02.jpg", cv2.IMREAD_GRAYSCALE)

roi_1  = img_1[:200,600:800]
roi_2  = img_2[:200,600:800]

#Usando o detector ORB
orb = cv2.ORB_create(nfeatures=2500)

kp_1,dp_1 =orb.detectAndCompute(roi_1,None)
kp_2, dp_2 = orb.detectAndCompute(roi_2,None)


##Verificando a correlação entre as Imagens IHM

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(dp_1,dp_2)
matches = sorted(matches, key=lambda x:x.distance)

matching  = cv2.drawMatches(roi_1,kp_1,roi_2,kp_2,matches,None,flags=2)

print(len(matches))
cv2.imshow("Reg. de interesse 1",roi_1)
cv2.imshow("Reg. de interesse 2", roi_2)
cv2.imshow("Resultado de correspodencia",matching)
cv2.waitKey(0)
cv2.destroyAllWindows()






