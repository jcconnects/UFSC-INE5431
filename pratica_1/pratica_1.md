# Objetivo da Prática: reforçar conceitos relacionados a digitalização de áudio; entender os efeitos dos parâmetros de digitalização na qualidade do áudio.

# Procedimentos:

1) Entre no colab https://colab.research.google.com/ e abra um notebook com o código abaixo e faça o upload do arquivo audio.wav. Este arquivo tem uma taxa de amostragem de 44.1Khz, 16 bits/amostra e é mono. 

2) Estude o código python

3) Responda as questões abaixo:

# A) Vá no notebook e altere o som para manter os parâmetros próximos do original: 40kHz e 16 bits por amostra. Em seguida responda:

## i) Qual é a maior frequência de som no arquivo acima da magnitude 1?
10kHz

## ii) Indique o maior componente de frequência (em Hertz) possível quando estes parâmetros de digitalização são utilizados.
20kHz

## iii) Qual é o tamanho teórico do áudio (parte de dados);
800KB

## iv) O tamanho do arquivo em bytes (ver propriedades do arquivo, ou Linux utilize o comando "ls -l audio.wav) e indique o motivo da diferença entre este tamanho e o calculado em ii).
O tamanho do arquivo é 800044B porque 44B são referentes ao header (800000B dados + 44B header).

## v) O tamanho do arquivo em disco em bytes, observando as propriedades do arquivo, ou no linux utilize "du -s -B1 audio.wav", e indique o motivo da diferença entre este tamanho e o tamanho do arquivo em ii).
Utilizando blocos de disco de tamanho 4096 bytes, são necessários 196 blocos para armazenar os 800044 bytes do arquivo, resultando em um tamanho total em disco de 802816 bytes (196 blocos * 4096 bytes).

## vi) Indique o tamanho deste arquivo em disco se o seu HD fosse formatado para um tamanho de bloco (unidade de alocação em disco) de 2048 B.
Com blocos de tamanho 2048B, precisamos de 391 blocos para armazenar os 800044 bytes do arquivo (800044B arquivo / 2048B bloco), resultando em um tamanho do arquivo em disco de 800.768 bytes.

# B) Utilize agora o notebook para alterar a taxa de amostragem para 10kHz, e mantendo 16-bits por amostra, e responda: 

## i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?
Observou-se uma degradação do sinal (som abafado), pois a taxa de amostragem de 10kHz não permite representar frequências acima de 5kHz, fazendo com que partes de frequência mais altas do áudio original fossem perdidas.

## ii) Qual é o tamanho em bytes da parte de dados do áudio após esta conversão?
200KB

# C) Utilize agora o notebook para alterar a taxa de amostragem para 4kHz   e mantendo 4-bits por amostra, e responda: 

## i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?
Observou-se uma degradação do sinal (som abafado), pois a taxa de amostragem de 4kHz não permite representar frequências acima de 2kHz, fazendo com que partes de frequência mais altas do áudio original fossem perdidas.

## ii) Qual é o tamanho teórico em bytes da parte de dados do áudio após esta conversão?
20KB

## iii) O arquivo de áudio gerado no notebook mantém 4 bits por amostra no arquivo?
Não, pois o formato WAV utiliza, no mínimo, 8 bits por amostra como menor unidade de armazenamento. Portanto, mesmo que as amostras sejam capturadas com 4 bits, elas são armazenadas como 1 byte no arquivo.
