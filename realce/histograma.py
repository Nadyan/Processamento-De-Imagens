import cv2
from matplotlib import pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image


# Histogramas de baixo contraste:

gray_img = cv2.imread('low_ponte.png', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogama low_ponte.png')
plt.show()

#########################################################

gray_img = cv2.imread('low_rio.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma low_rio.jpg')
plt.show()


#########################################################

gray_img = cv2.imread('low_baleia.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma low_baleia.jpg')
plt.show()



# Histogramas de alto contraste:

gray_img = cv2.imread('high_rua.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma high_rua.jpg')
plt.show()


#########################################################

gray_img = cv2.imread('high_trem.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma high_trem.jpg')
plt.show()



