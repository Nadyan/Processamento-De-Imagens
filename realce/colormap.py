import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image

import cv2
from matplotlib import pyplot as plt

m = list()
fh = open("grayscale_map.txt", "r")
for line in fh:
    aux = line.split() # quebra a linha em uma 'list' de strings

    # monta um vetor com as strings individuais lidas por linhas
    for i, val in enumerate(aux):
        b = np.fromstring(val, dtype=int, sep=' ')
        m.append(b)

M = np.asarray(m)

# converte o vetor M de 256*3 elementos em um array 256x3
M = np.reshape(M,(256,3))

im = Image.open('aorta2.jpg')
out = Image.new("L", im.size) # L = 8bits black and white 0-255
height,width = im.size

for i in range(0,height):
	for j in range(0, width):
		pixel = im.getpixel((i,j))
		out.putpixel((i,j), (M[pixel][0], M[pixel][1], M[pixel][2]))

out.save("aorta2eq.jpg", "JPEG")

# histograma equalizado:
gray_img = cv2.imread('aorta2eq.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histograma aorta2eq.jpg')
plt.show()
