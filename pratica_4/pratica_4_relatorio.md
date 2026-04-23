# Questão 1. Indique as taxas de compressão obtida pelas codificações CUIF.1, CUIF.2, CUIF.3 e CUIF.4 para as imagens lena e teste (razão entre o arquivo original bmp e os arquivos cuif).

=== lena.bmp ===
Taxa CUIF.1: 1.0000
Taxa CUIF.2: 1.5000
Taxa CUIF.3: 1.0000
Taxa CUIF.4: 1.0867

=== teste.bmp ===
Taxa CUIF.1: 1.0003
Taxa CUIF.2: 1.5003
Taxa CUIF.3: 1.0003
Taxa CUIF.4: 21.4313


# Questão 2. Compare as taxas de compressão obtidas pelas codificações CUIF.1, CUIF.2, CUIF.3 e CUIF.4 para a imagem lena. Qual é a codificação gerou a maior taxa de compressão? Justifique porque.

A taxa de compressão obtida pelo CUIF.2 foi a maior para a imagem lena. Isso acontece porque o CUIF.2 descarta os 4 bits menos significativos dos canais G e B e combina os 4 bits mais significativos de cada um em um único byte. Dessa forma, em vez de armazenar 3 bytes por pixel (R, G, B), armazena-se 2 bytes por pixel (R completo e GB combinado), resultando na taxa de compressão de 1.5.

# Questão 3. Compare as taxas obtidas para as imagens lena e teste. Explique porque a taxa de compressão para o CUIF.4 da imagem teste é bem maior para a imagem lena.bmp.

As taxas de CUIF.1, CUIF.2 e CUIF.3 para ambas imagens foi bem similar. A grande diferença que acontece no CUIF.4 é decorrente de a imagem teste ter somente duas cores utilizadas repetidas vezes. Isso é muito vantajoso para a compressão RLE utilizada, pois permite reduzir significativamente o tamanho de bytes utilizados por imagens que possuem repetição de pixels.

# Questão 4. Indique o PSNR medido nas imagens lena1.bmp, lena2.bmp, lena3.bmp e lena4.bmp quando comparadas com a imagem original lena.bmp. Justifique os valores obtidos, explicando a fonte dos ruídos gerados em cada codificação.

=== lena.bmp ===
PSNR CUIF.1: Infinito
PSNR CUIF.2: 30.93921521048951
PSNR CUIF.3: 44.123361242826995
PSNR CUIF.4: 39.47975675028337

Para lena1, não houve ruído pois o CUIF.1 armazena os canais RGB sem nenhuma alteração. Para lena2, o ruído vem do descarte dos 4 bits menos significativos dos canais G e B na codificação. Para lena3, o ruído vem do truncamento das operações de ponto flutuante nas conversões RGB→YCbCr e YCbCr→RGB, que acumula pequenos erros em ambas as direções. Para lena4, o ruído tem duas fontes: o mesmo truncamento da conversão YCbCr do CUIF.3, e o shift right aplicado na compressão RLE que zera o bit menos significativo de todos os valores YCbCr, introduzindo um erro adicional na reconstrução.

# Questão 5. Indique o PSNR medido na imagem teste2.bmp quando comparada com a imagem original teste.bmp. Justifique os valor obtido.

O PSNR é infinito pois os componentes de cor são múltiplos de 16 (pois a conversão faz shifts para a direita). Nesse caso a imagem não possuí componentes de cor verde e azul, então não existe nenhum ruído quando é feita a conversão CUIF.2.
