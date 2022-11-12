import cv2
import numpy
from matplotlib import pyplot as plt
import numpy as np
import pip
import  os

def conv_grayscale(path):

    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(os.path.join("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/img","GC_01.jpg"),img)



















