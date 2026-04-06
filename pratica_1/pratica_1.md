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
800kB

## iv) O tamanho do arquivo em bytes (ver propriedades do arquivo, ou Linux utilize o comando "ls -l audio.wav) e indique o motivo da diferença entre este tamanho e o calculado em ii).
O tamanho do arquivo é 800044B porque 44B são referentes ao header.

## v) O tamanho do arquivo em disco em bytes, observando as propriedades do arquivo, ou no linux utilize "du -s -B1 audio.wav", e indique o motivo da diferença entre este tamanho e o tamanho do arquivo em ii).
Utilizando o comando du, 802.816 bytes (blocos de 4096 B no APFS). O tamanho do arquivo depende do tamanho do bloco do sistema de arquivos.

## vi) Indique o tamanho deste arquivo em disco se  o seu HD fosse formatado para um tamanho de bloco (unidade de alocação em disco) de 2048 B.
 O disco aloca espaço em blocos fixos de 2048 bytes e precisa de 391 blocos para armazenar o aquivo, desse modo ele ocupa 800.768 bytes em disco. Precisamos de um bloco extra para armazenar 1324 bytes.

# B) Utilize agora o notebook para alterar a taxa de amostragem para 10kHz,   e mantendo 16-bits por amostra, e responda: 

## i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?
O áudio ficou com o som abafado. A maior frequência é 5kHz.

## ii) Qual é o tamanho em bytes da parte de dados do áudio após esta conversão?
200kB

# C) Utilize agora o notebook para alterar a taxa de amostragem para 4kHz   e mantendo 4-bits por amostra, e responda: 

## i) Qual o efeito que ocorreu com esta alteração de taxa de amostragem? Qual é a maior frequência do som possível com estes parâmetros de digitalização?
Ficou abafado e teve vários cortes. A maior frequência é 2kHz

## ii) Qual é o tamanho teórico em bytes da parte de dados do áudio após esta conversão?
20kB

## iii) O arquivo de áudio gerado no notebook mantém 4 bits por amostra no arquivo?
No arquivo ele mantém 8 bits ao invés de 4 bits, pois o formato WAV suporta no mínimo 8 bits como menor tipo inteiro disponível.
