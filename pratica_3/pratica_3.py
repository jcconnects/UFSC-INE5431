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


if __name__ == "__main__":
    filepath = "lena.bmp"
    img = Image.open(filepath)
    matriculas = [22104062, 22100628, 23100484]

    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img, 1, matriculas)

    # imprime cabeçalho Cuif
    cuif.printHeader()

    # gera o arquivo Cuif.1
    cuif.save("lena1.cuif")

    # Abre um arquivo Cuif e gera o objeto Cuif
    cuif1 = Cuif.openCUIF("lena1.cuif")

    # Converte arquivo Cuif em BMP e mostra
    cuif1.saveBMP("lena1.bmp")
    cuif1.show()
    img1 = Image.open("lena1.bmp")

    # Cálculo do PSNR
    psnr = PSNR(img, img1, 8)
    print(f"Cálculo do PSNR: {psnr}")
