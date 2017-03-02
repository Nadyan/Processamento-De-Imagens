# Teste de script para abrir arquivos

from PIL import Image
from pylab import *
import matplotlib.pyplot as plt

pil1 = Image.open('imagem.png')
#pil1.show()

out = pil1.rotate(45)
pil1.show()

# para ler a imagem como um array
im = array(Image.open('imagem2.png'))
imshow(im)

plt.show()
