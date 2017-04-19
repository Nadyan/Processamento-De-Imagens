import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from PIL import Image
import cv2

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

im = Image.open('aorta1.jpg')
backtorgb = cv2.cvtColor(im,cv2.COLOR_GRAY2RGB) # converte grayscale em RGB (testar)

out = Image.new("RGB", im.size)
height,width = im.size

for i in range(0,height):
	for j in range(0,width):
		pixel = im.getpixel((i,j))
		out.putpixel((i,j), (M[pixel][0], M[pixel][1], M[pixel][2])) # IndexError: index 82 is out of bounds for axis 1 with size 3 (WHYYYYYYYYYYY?)

out.save("aorta1_Out.jpg", "JPEG")

# histograma equalizado:
#gray_img = cv2.imread('aorta2eq.jpg', cv2.IMREAD_GRAYSCALE)
#hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
#plt.hist(gray_img.ravel(),256,[0,256])
#plt.title('Histograma aorta2eq.jpg')
#plt.show()


