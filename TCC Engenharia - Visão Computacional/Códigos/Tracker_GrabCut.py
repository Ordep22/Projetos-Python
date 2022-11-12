import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
from tracker import *

tracker = EuclideanDistTracker()
video = cv2.VideoCapture("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Vídeos Resende - Bobinas CG/c-01-20200722-095244.ts",cv2.IMREAD_GRAYSCALE)



while True:
    ret, frame = video.read()
    roi = frame[0:680, 0:720]
    rect = (481, 10, 441, 225)

    ###############################
    #Tenho que otimizar essa parte está travando o código

    mask = np.zeros(roi.shape[:2],np.uint8)
    bgModel = np.zeros((1,65),np.float64)
    fgModel = np.zeros((1,65),np.float64)

    cv2.grabCut(roi,mask,rect,bgModel,fgModel,1,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    roi = roi * mask2[:, :, np.newaxis]
    ###################################################################



    cv2.imshow("Resgiao de interesse", frame)
    cv2.imshow("Grabcut", roi)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()









