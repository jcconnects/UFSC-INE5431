"""
INE5431 Sistemas Multimídia
Prof. Roberto Willrich

Aula Prática IV: Compressão de Entropia

"""

from PIL import Image
from Cuif import Cuif
import math


def PSNR(original, decodificada, b):
    try:
        mse = MSE(original, decodificada)
        psnr = 10 * math.log10(((2**b - 1) ** 2) / mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"


def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    sum = 0
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
            mse_r = (ori_r - dec_r) ** 2
            mse_g = (ori_g - dec_g) ** 2
            mse_b = (ori_b - dec_b) ** 2
            sum += mse_r + mse_g + mse_b
    return sum / nsymbols


import os


def taxa_compressao(bmp_path, cuif_path):
    bmp_size = os.path.getsize(bmp_path)
    cuif_size = os.path.getsize(cuif_path)
    return bmp_size / cuif_size


if __name__ == "__main__":

    matriculas = [22104062, 22100628, 23100484]

    for nome in ["lena", "teste"]:
        img = Image.open(f"{nome}.bmp")
        print(f"\n=== {nome}.bmp ===")

        # CUIF.1
        cuif1 = Cuif(img, 1, matriculas)
        cuif1.save(f"{nome}1.cuif")
        cuif1.saveBMP(f"{nome}1.bmp")
        img1 = Image.open(f"{nome}1.bmp")
        print(f"PSNR CUIF.1: {PSNR(img, img1, 8)}")
        print(f"Taxa CUIF.1: {taxa_compressao(nome+'.bmp', nome+'1.cuif'):.4f}")

        # CUIF.2
        cuif2 = Cuif(img, 2, matriculas)
        cuif2.save(f"{nome}2.cuif")
        cuif2.saveBMP(f"{nome}2.bmp")
        img2 = Image.open(f"{nome}2.bmp")
        print(f"PSNR CUIF.2: {PSNR(img, img2, 8)}")
        print(f"Taxa CUIF.2: {taxa_compressao(nome+'.bmp', nome+'2.cuif'):.4f}")

        # CUIF.3
        cuif3 = Cuif(img, 3, matriculas)
        cuif3.save(f"{nome}3.cuif")
        cuif3.saveBMP(f"{nome}3.bmp")
        img3 = Image.open(f"{nome}3.bmp")
        print(f"PSNR CUIF.3: {PSNR(img, img3, 8)}")
        print(f"Taxa CUIF.3: {taxa_compressao(nome+'.bmp', nome+'3.cuif'):.4f}")

        # CUIF.4
        cuif4 = Cuif(img, 4, matriculas)
        cuif4.save(f"{nome}4.cuif")
        cuif4.saveBMP(f"{nome}4.bmp")
        img4 = Image.open(f"{nome}4.bmp")
        print(f"PSNR CUIF.4: {PSNR(img, img4, 8)}")
        print(f"Taxa CUIF.4: {taxa_compressao(nome+'.bmp', nome+'4.cuif'):.4f}")
