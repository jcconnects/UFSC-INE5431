## Questão 1.  Abra o arquivo lena.bmp no editor hexadecimal em https://hexed.it/ e, analisando o formato do cabeçalho BMP apresentado na Seção 2, indique no relatório: qual é o valor dos campos offset e tamanho do arquivo? Quais são os valores dos componentes de cor R, G e B do primeiro pixel armazenado no arquivo?
O valor do campo offset é 54 bytes e o valor do campo de tamanho do arquivo é 786486 bytes.
Já os valores dos componentes de cor do primeiro pixel são:
    R: 82
    G: 22
    B: 57

## Questão 2. Qual é o tamanho do cabeçalho do arquivo lena1.cuif para seu grupo?
26 bytes (três números de matrícula).

## Questão 3. No arquivo praticaIII.py tem um função PSNR incompleta. Implemente esta função de maneira a calcular o PSRN passando como parâmetro a imagem original e uma decodificada. Implemente o cálculo do MSE e PSNR com base nas fórmulas da seção 5.
função implementada no arquivo 'PraticaIII.py'.

## Questão 4. Indique o PSNR comparando a imagem original mandril.bmp (original) com a imagem obtida a partir do arquivo CUIF.1 (lena1.bmp). Explique porque do resultado do PSNR para o caso do CUIF.1.
A comparação resultou em um PSNR tendendo ao infinito, ou seja, nenhum ruído entre as imagens. Esse comportamento do PSNR ocorre devido ao valor do MSE (Erro médio quadrático) obtido estar próximo de zero.

## Questão 5. Compacte as imagens lena.bmp e lena1.cuif com zip. Qual a taxa de compressão obtida para os dois arquivos? Qual arquivo compactou mais? Explique porque deste resultado, ou seja, indique a vantagem de organizar os pixels nesta sequência definida pelo CUIF.1 (primeiro os valores de R, depois de G e finalmente de B) para a compressão baseada em RLE ou DPCM? Dica: relembre os princípios da compressão RLE e DPCM e compare a parte de dados de imagem do arquivo lena.bmp e lena1.cuif no editor hexadecimal
Tamanho do arquivo lena.bmp antes e após compactação:
    lena.bmp = 786486 bytes
    lena.bmp.zip = 735145 bytes

Calculando a taxa de compressão (tam. original / tam. comprimido), temos:
    taxa compressão = 786486 bytes / 735145 bytes ~= 1.0698

Tamanho do arquivo lena1.cuif antes e após compactação:
    lena1.cuif = 786458 bytes
    lena1.cuif.zip = 639299 bytes

Calculando a taxa de compressão (tam. original / tam. comprimido), temos:
    taxa compressão = 786458 bytes / 639299 bytes ~= 1.2301

Logo, podemos observar que o arquivo lena1.cuif obteve uma taxa de compressão maior que o lena.bmp. Isso ocorre pois, ao contrário do bitmap, o CUIF armazena os componentes de cor de forma sequencial, inserindo todos os componentes R seguidos de todos os G e, por fim, os componentes B. Essa organização torna as técnicas de compressão RLE e DPCM eficientes, uma vez que a variação entre valores próximos tende a ser menor. 

## Questão 6. Agora altere o código em PraticaIII.py para que seja gerado o arquivo lena2.cuif, que utiliza a versão CUIF.2 (usar 2 em vez de 1 para indicação da versão) e lena2.bmp. Visualiza as imagens lena1.bmp e lena2.bmp para ver se existem diferenças visíveis. Analise o código que gera o arquivo CUIF.2 (em Cuif.py) e explique o princípio da compressão adotada no CUIF.2
É possível observar ruídos na imagem do lena2.bmp. Isso ocorre porque o CUIF.2 aplica compressão
com perda, reduzindo a precisão dos componentes de cor verde e azul de 8 bits para 4 bits cada. Essa técnica baseia-se em quantização (redução de precisão) e empacotamento de canais, o que explica a perda de qualidade visual observada na imagem.

## Questão 7. Indique as taxas de compressão obtidas pelos CUIF.1 e CUIF.2 para a imagem lena.bmp? Para este cálculo determine a razão entre um arquivo cuif e a imagem lena.bmp. Qual versão do CUIF compactou mais?
Tamanho dos arquivos:
    lena.bmp = 786486 bytes 
    lena1.cuif = 786458 bytes
    lena2.cuif = 524314 bytes

Taxas de compressão (tam. bitmap / tam. cuifx):
    CUIF.1 = 786486 / 786458 ~= 1
    CUIF.2 = 786486 / 524314 ~= 1.5

A versão CUIF.2 compactou mais, pois reduziu a quantidade de dados por pixel de 3 bytes para 2 bytes, armazenando o componente R com 8 bits (1 byte) e empacotando os componentes G e B em um único byte (4 bits cada), resultando em uma redução de 33% do tamanho do conteúdo do arquivo.

## Questão 8. Indique o PSNR comparando a imagem original lena.bmp (original) com a imagem obtida a partir do arquivo CUIF.2 (lena2.bmp). Justifique a resposta do PSNR indicando a fonte do ruído.
A comparação resultou em um PSNR de aproximadamente 30.93 dB, indicando a presença de ruído. Esse ruído é causado pela compressão com perda do CUIF.2, que reduz a precisão dos componentes de cor
verde e azul de 8 bits para 4 bits.

