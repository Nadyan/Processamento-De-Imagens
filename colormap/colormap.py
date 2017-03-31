import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image

import cv2
from matplotlib import pyplot as plt

m = list()
fh = open("mapa.txt", "r")
for line in fh: 
    aux = line.split() # quebra a linha em uma 'list' de strings

    # monta um vetor com as strings individuais lidas por linhas
    for i, val in enumerate(aux):
        b = np.fromstring(val, dtype=int, sep=' ')
        m.append(b)

M = np.asarray(m)

# converte o vetor M de 256*3 elementos em um array 256x3
M = np.reshape(M,(256,3))

#print(M)

im = Image.open('mapaEUA.jpg')
out = Image.new("RGB", im.size)
height,width = im.size

for i in range(0,height):
	for j in range(0, width):
		pixel = im.getpixel((i,j))
		out.putpixel((i,j), (M[pixel][0], M[pixel][1], M[pixel][2]))

out.save("mapaEUAOut.jpg", "JPEG")


# histograma:
# pip install opencv-python
gray_img = cv2.imread('mapaEUA.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.imshow('GoldenGate',gray_img)
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma para escala de cinza mapaEUA.jpg')
plt.show()
		

