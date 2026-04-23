# Relatório Prática 3

Entregue via Moodle o relatório contendo as respostas das questões abaixo e o código modificado:

## Questão 1. Abra o arquivo lena.bmp no editor hexadecimal em https://hexed.it/ e, analisando o formato do cabeçalho BMP apresentado na Seção 2, indique no relatório: qual é o valor dos campos offset e tamanho do arquivo? Quais são os valores dos componentes de cor R, G e B do primeiro pixel armazenado no arquivo?
Campo offset: 54 bytes
Tamanho do arquivo: 786486 bytes 
Componentes de cor:
- B: 57
- G: 22
- R: 82

## Questão 2. Qual é o tamanho do cabeçalho do arquivo lena1.cuif para seu grupo?
26 bytes.

## Questão 3. No arquivo praticaIII.py tem um função PSNR incompleta. Implemente esta função de maneira a calcular o PSRN passando como parâmetro a imagem original e uma decodificada. Implemente o cálculo do MSE e PSNR com base nas fórmulas da seção 5 .

## Questão 4. Indique o PSNR comparando a imagem original mandril.bmp (original) com a imagem obtida a partir do arquivo CUIF.1 (lena1.bmp). Explique porque do resultado do PSNR para o caso do CUIF.1.

## Questão 5. Compacte as imagens lena.bmp e lena1.cuif com zip. Qual a taxa de compressão obtida para os dois arquivos? Qual arquivo compactou mais? Explique porque deste resultado, ou seja, indique a vantagem de organizar os pixels nesta sequência definida pelo CUIF.1 (primeiro os valores de R, depois de G e finalmente de B) para a compressão baseada em RLE ou DPCM? Dica: relembre os princípios da compressão RLE e DPCM e compare a parte de dados de imagem do arquivo lena.bmp e lena1.cuif no editor hexadecimal.

## Questão 6. Agora altere o código em PraticaIII.py para que seja gerado o arquivo lena2.cuif, que utiliza a versão CUIF.2 (usar 2 em vez de 1 para indicação da versão) e lena2.bmp. Visualiza as imagens lena1.bmp e lena2.bmp para ver se existem diferenças visíveis. Analise o código que gera o arquivo CUIF.2 (em Cuif.py) e explique o princípio da compressão adotada no CUIF.2

## Questão 7. Indique as taxas de compressão obtidas pelos CUIF.1 e CUIF.2 para a imagem lena.bmp? Para este cálculo determine a razão entre um arquivo cuif e a imagem lena.bmp. Qual versão do CUIF compactou mais? 

## Questão 8. Indique o PSNR comparando a imagem original lena.bmp (original) com a imagem obtida a partir do arquivo CUIF.2 (lena2.bmp). Justifique a resposta do PSNR indicando a fonte do ruído.
