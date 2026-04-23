# Prática 3 — Representação Digital de Imagens

**Disciplina:** INE5431 - Sistemas Multimídia  
**Professor:** Roberto Willrich  
**Data:** 15 de abril de 2026

## Contexto

Desenvolvimento de padrões de representação/compressão de imagem digital usando o formato **CUIF (CUstom Image Format)**. A prática trabalha com as versões CUIF.1 e CUIF.2, usando a imagem `lena.bmp` como base, e o formato BMP como referência sem compressão.

## Arquivos

- `Cuif.py` — biblioteca com a classe Cuif (construtor, printHeader, show, save, open, saveBMP)
- `pratica_3.py` — script principal a ser modificado (contém função PSNR incompleta)
- `lena.bmp` — imagem de entrada
- `relatorio.md` — relatório com respostas às questões

## Formato BMP (resumo)

- Cabeçalho de 54 bytes (offset 0–53), dados da imagem a partir do offset indicado no campo offset (bytes 10–13)
- Pixels codificados em ordem **BGR** (não RGB)
- Cada linha deve ser múltiplo de 4 bytes (padding com zeros)
- Linhas armazenadas de baixo para cima (invertidas)
- Apenas BMPs de 3 bytes/pixel sem compressão são considerados

### Cabeçalho BMP (campos principais)

| Offset | Tamanho | Descrição |
|--------|---------|-----------|
| 0 | 2 | Assinatura: `4D42` hex |
| 2 | 4 | Tamanho do arquivo |
| 10 | 4 | Offset até os dados da imagem |
| 18 | 4 | Largura (pixels) |
| 22 | 4 | Altura (pixels) |
| 28 | 2 | Bits por pixel (24 para RGB) |

## Formato CUIF (cabeçalho)

| Offset | Tamanho | Descrição |
|--------|---------|-----------|
| 0 | 4 | Assinatura: `"CUIF"` |
| 4 | 1 | Versão do padrão CUI |
| 5 | 1 | Número de estudantes no grupo (Nestud) |
| 6 | 4 | Largura da imagem (pixels) |
| 10 | 4 | Altura da imagem (pixels) |
| 14 | 4×Nestud | Matrículas dos estudantes (4 bytes cada) |

### CUIF.1

- Representação RGB separada em canais (canal a canal, não pixel a pixel)
- Ordem: todos os valores R em raster, depois todos os G, depois todos os B
- 1 byte por canal por pixel

### CUIF.2

- Compressão com perdas
- A técnica deve ser analisada no código `Cuif.py`

## Métricas de Qualidade

**MSE (Mean Squared Error):**
```
MSE(Ori, Dec) = (1/n) * sum((ori_i - dec_i)^2)
```
onde `n = 3 * altura * largura` (3 componentes por pixel)

**PSNR (Peak Signal-to-Noise Ratio):**
```
PSNR(Ori, Dec) = 10 * log10( (2^b - 1)^2 / MSE(Ori, Dec) )
```
onde `b = 8` bits por símbolo. Quanto maior o PSNR, melhor a qualidade.

## Roteiro

1. Abrir `lena.bmp` no editor hexadecimal (hexed.it) para responder a Questão 1
2. Incluir matrículas do grupo em `pratica_3.py`
3. Executar `pratica_3.py` para converter `lena.bmp` → `lena1.cuif`
4. Fazer conversão inversa: `lena1.cuif` → `lena1.bmp`
5. Verificar matrículas exibidas no console
6. Comparar `lena.bmp` e `lena1.bmp` visualmente

## Questões do Relatório

1. Campos *offset* e *tamanho do arquivo* do BMP; valores RGB do primeiro pixel
2. Tamanho do cabeçalho de `lena1.cuif` para o grupo
3. Implementar MSE e PSNR em `pratica_3.py` (função incompleta)
4. PSNR entre `lena.bmp` e `lena1.bmp` (CUIF.1); justificar resultado
5. Compactar com zip e comparar taxas de compressão; explicar organização canal-a-canal vs RLE/DPCM
6. Gerar `lena2.cuif` (CUIF.2); comparar visualmente com `lena1.bmp`; explicar técnica de compressão
7. Taxas de compressão de CUIF.1 e CUIF.2 para `lena.bmp`; qual versão compactou mais
8. PSNR entre `lena.bmp` e `lena2.bmp`; identificar fonte do ruído
