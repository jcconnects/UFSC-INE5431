from urllib.request import urlopen
from PIL import Image # package pillow
import math
# Alunos:
# Francisco Bortolanza
# João Pedro Schmidt Cordeiro
# Leonardo Franchini


def criarImagemRGB():
    img = Image.new( "RGB", (512,256))
    raster = img.load()
        
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = (220,219,97,255)
            
    # obtendo o pixel 0,0
    (r, g, b) = img.getpixel((0, 0))
    print("Pixel (0,0) com getpixel:", r, g, b)
    
    # outra forma
    print("Pixel (0,0): com raster", raster[0, 0])
    
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (500,500))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/50)+int(j/50)) % 2 == 0):
                raster[i,j] = 0
            else:
                raster[i,j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img

def reduzirResolucao(img):
    new_w = img.width // 4
    new_h = img.height // 4
    nova = Image.new("RGB", (new_w, new_h))
    src = img.load()
    dst = nova.load()
    for i in range(new_w):
        for j in range(new_h):
            r, g, b = src[i * 4, j * 4][:3]
            dst[i, j] = (r, g, b)
    return nova

def converterCinza(img):
    nova = Image.new("L", (img.width, img.height))
    src = img.load()
    dst = nova.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = src[i, j][:3]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            dst[i, j] = gray
    return nova

def converterBinaria(img, limiar=128):
    nova = Image.new("1", (img.width, img.height))
    src = img.load()
    dst = nova.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = src[i, j][:3]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            dst[i, j] = 1 if gray >= limiar else 0
    return nova

def reduzirBits(img):
    nova = Image.new("RGB", (img.width, img.height))
    src = img.load()
    dst = nova.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = src[i, j][:3]
            dst[i, j] = (r & 0xF0, g & 0xF0, b & 0xF0)
    return nova

def separarCanaisRGB(img):
    img_r = Image.new("RGB", (img.width, img.height))
    img_g = Image.new("RGB", (img.width, img.height))
    img_b = Image.new("RGB", (img.width, img.height))
    src = img.load()
    raster_r = img_r.load()
    raster_g = img_g.load()
    raster_b = img_b.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = src[i, j][:3]
            raster_r[i, j] = (r, 0, 0)
            raster_g[i, j] = (0, g, 0)
            raster_b[i, j] = (0, 0, b)
    return img_r, img_g, img_b

img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/peixe.png"))
print("Largura:", img.width, "Altura:", img.height)
img.show()
criarImagemRGB().show()
criarImagemCinza().show()
criarImagemBinaria().show()

reduzirResolucao(img).show()
converterCinza(img).show()
converterBinaria(img).show()
reduzirBits(img).show()
img_r, img_g, img_b = separarCanaisRGB(img)
img_r.show()
img_g.show()
img_b.show()


