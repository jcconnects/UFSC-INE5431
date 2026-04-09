
Baixe o código python anexado à esta tarefa que apresenta a imagem peixe.png  e outras imagens. Após, altere o código praticaii.py  para realizar as operações abaixo. A implementação deve ser sobre a manipulação dos píxeis no bitmap (raster), o aluno não pode utilizar funções de bibliotecas para tais operações (não pode usar convert() para conversão automática de tipos de imagem, split() para separar canais e resize() para mudar a escala). 

1. Reduza a resolução da imagem para ficar com a 1/4 altura e da largura da imagem peixe.png e apresente esta imagem.
2. Transforme a imagem peixe.png em tons de cinza e a apresente.
3. Transforme a imagem peixe.png em imagem binária e a apresenta.
4. Simule a redução do do número de bits por pixel da imagem peixe.png para 4 bits. Dica, para isto,  faça uma operação binária para manter apenas os 4 bits mais significados de cada componente de cor. Por exemplo, um canal R de 1110 1101 deveria ser convertido em  1110 0000.
5. Conforme ilustrado na imagem mais abaixo, realizar a separação (split) dos canais RGB da imagem peixe.png, apresentando 3 imagens, R, G, B, a partir da imagem original. Conforme exemplo figura abaixo. Os pixels (i,j) da imagem R devem representar um tom de vermelho igual ao componente R do pixels (i,j) da imagem original. Da mesma forma, as imagens G e B devem conter as intensidades de verde e azul dos pixels da imagem original.

Entregue o arquivo praticaii.py com as funcionalidades acima (cada uma funcionalidade sendo implementada por funções). Coloque em comentário no código os membros da equipe e apenas um dos membros deve entregar o relatório.


