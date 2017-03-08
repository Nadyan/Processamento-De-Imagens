from PIL import Image

print("Abrindo Imagens...")
pil1 = Image.open('C:\Users\Nadyan\Desktop\PIM - T1\happy.jpg')
pil2 = Image.open('C:\Users\Nadyan\Desktop\PIM - T1\angry.jpg')

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
u2 = 0.6 #parametro para interpolacao da imagem 2

out = Image.new(pil1.mode, (l, h))

print("Calculando...")
for j in range(0, h):
    for i in range(0, l):
        u = (1-u1) * pil1.getpixel(i, j) + u1 * pil2.getpixel(i, j) #interpolacao dos pixels
        out1.putpixel((i,j), u) #insere a interpolacao na imagem de saida

        u = (1-u2) * pil1.getpixel(i, j) + u2 * pil2.getpixel(i, j)
        out2.putpixel((i, j), u)

#out.show()
out1.save("outMorph1.jpg", "JPEG")
out2.save("outMorph2.jpg", "JPEG")

print("Pronto! Arquivos de saida: outMorph1.jpg e outMorph2.jpg")
