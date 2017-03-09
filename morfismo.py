from PIL import Image

print("Abrindo Imagens...")
pil1 = Image.open('happy.jpg')
pil2 = Image.open('angry.jpg')

(l1, h1) = pil1.size
(l2, h2) = pil2.size

print("Conferindo dimensoes...")
if l1 != l2 or h1 != h2: #confere se as duas imagens possuem a mesma dimensao
    pint("ERRO! Imagens de dimensoes diferentes!")
    print(l1, h1)
    print(l2, h2)
    exit()

(l, h) = (l1, h1) #atribui a dimensao da imagem de saida

u1 = 0.4 #parametro para interpolacao da imagem 1
u2 = 0.8 #parametro para interpolacao da imagem 2

out1 = Image.new(pil1.mode, (l, h))
out2 = Image.new(pil1.mode, (l, h))

print("Calculando...")
for j in range(0, h):
    for i in range(0, l):
        # INTERPOLACAO PARA A IMAGEM 1:
        x = (tuple([(1-u1) * x for x in pil1.getpixel((i, j))])) # primeira parte da interpolacao com u1
        y = (tuple([u1 * x for x in pil2.getpixel((i, j))]))     # segunda parte da interpolacao com u1
        u = tuple(map(sum, zip(x, y)))                           # soma das partes da interpolacao
        u = (tuple([int(x) for x in u]))                         # passar a tupla u de float para int

        out1.putpixel((i,j), u)                                  # insere os pixels interpolados na imagem1

        # INTERPOLACAO PARA A IMAGEM 2:
        x = (tuple([(1-u2) * x for x in pil1.getpixel((i, j))])) # primeira parte da interpolacao com u2
        y = (tuple([u2 * x for x in pil2.getpixel((i, j))]))     # segunda parte da interpolacao com u2
        u = tuple(map(sum, zip(x, y)))                           # soma das partes da interpolacao
        u = (tuple([int(x) for x in u]))                         # passar a tupla u de float para int
        
        out2.putpixel((i, j), u)                                 # insere os pixels interpolados na imagem2

#out.show()
out1.save("outMorph1.jpg", "JPEG")
out2.save("outMorph2.jpg", "JPEG")

print("Pronto! Arquivos de saida: outMorph1.jpg e outMorph2.jpg")
