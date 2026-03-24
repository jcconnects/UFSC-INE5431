CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA
INE5431 SISTEMAS MULTIMÍDIA
PROF. ROBERTO WILLRICH ( INE/UFSC)
ROBERTO.WILLRICH@UFSC.BR
HTTPS://MOODLE.UFSC.BR
Introdução
Objetivos do Capítulo
Identificação os principais requisitos de rede de comunicação para
transmissão de áudio e vídeo
Analisar algumas tecnologias de redes locais
Conteúdo
Definição de alguns parâmetros de desempenho de redes de computadores
importantes para a comunicação multimídia
Taxa de bits, vazão, atraso, variação de atraso, taxa de perdas de pacote
Caracterização das fontes de áudio e vídeo tempo-real
Identificação dos principais requisitos de rede para a comunicação de áudio e vídeo
Análise de algumas tecnologias: Ethernet e ADSL
https://lh3.googleusercontent.com/notebooklm/ANHLwAySuAMuWBAKdIdqTgfQItxmrAhG0LrBKbPAPeq2I1sJFj2OtK2BbF6V5Oo8sN5BCKZIOCgnt3JOCz9NfuJrDIwOZxP4fwCzV4Do4x7XzcBeddaOqAFdHWMrX4mzl2fQMhVs-Gsd0w=w657-h355-v0
Parâmetros de Desempenho de Redes
Taxa de bits
Taxa de bits é o número de dígitos binários que a rede é capaz de transportar
por unidade de tempo
Expresso em bps, Kbps, Mbps, Gbps, etc
Exemplo taxa nominal de tecnologia de redes (enlace)
Ethernet 10Mbps, 100Mpbs, 1Gbps,...
Contratada pelo ISP: 10Mbps (download) / 1Mbps (upload)
https://lh3.googleusercontent.com/notebooklm/ANHLwAw0DBOsK9Ed6lk_WRQH8tqBsz69NBVcKJkjtxbuyNQcgmGw7zdPDtGCPqApY9KnUrNufOp-aEgTo01F7Cy9Y1lfMgHdaFiZeuPf0vhz0hQSoBPoGI06KhAplS3LUzZyHSbOgoPq=w257-h113-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAw7Kejl30kdQot6vieARK34y19YuHa5vqNYbRPzP6yrkV9UKtfJecK-kJjexuz9Nq1dGcIE2U81KqsuRZ_iQlWxWP7QvrwcbXdufVrqCuo6wNOqdkia2yIVJzUJrxcBz3uYasV0=w258-h113-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxW00oHi42i6KR82vepL-fY2vnPIRMwQcWjppklTY8UiBL6aUvofu-UVRwtAbWEXNzlORMexz0l7JDon59g2UhEstBQLz8wSpXZGhdu3ikMcDqAXpUsh0YXPwRoOYDquj2u5K-HDQ=w448-h428-v0
Parâmetros de Desempenho de Redes Vazão (Throughput)
Taxa de bits efetiva vista do ponto de vista do aplicativo
A taxa de bits realmente útil para as aplicações
Exemplo: tráfego HTTP
Pacotes http para ser transmitido
Sobrecarga de 20 bytes na camada de transporte (TCP) e mais 20 bytes na camada de rede (IP), ...
Vazão da maioria das redes varia com o tempo
Alguns fatores que afetam a vazão:
congestionamento (devido a sobrecarga ou gargalos)
falha de nós e ligações
controle de fluxo limita a taxa de transferência
P1 P2
Transporte
Rede
Enlace
Física
Transporte
Rede
Enlace
FísicaRede
Taxa de bit efetiva
https://lh3.googleusercontent.com/notebooklm/ANHLwAxdX5tO5jNTjjdHmCpKBBhnvSoE7IjQc1L1gGefhtF8x9_-apsqlspiNSqXvlGhjP79NTiQY4W2iFQT1xFQ7wp7RS_pIQy61qRkw-4bPJmzSrCFdsza_0s6DT_RcDymeVWoRtvE=w416-h140-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwwVCx-cVlfQthTD840bqEFS4RBjO88eiurNYE_apfopjJg6DP-efs_1O9Q95RuWz8tzd5hZkx4mg3gqOsRcQ6DtH-Xo-Q2YldjvtQs8HGni5ndFIsZym40qRXXtMfDoOLHBEQA7Q=w724-h395-v0
Parâmetros de Desempenho de Redes
Vazão (Throughput)
https://lh3.googleusercontent.com/notebooklm/ANHLwAzNJTeb8jwH6EKfKgWVU4vdA9bWQ4VjaGd3mWAAvpjskfjQisQULwUEkt51ExNwSrSaMOU-ElUcJWy6LaCS1hYJKjGL1XEPZAh2k2i3l35RBwdbzPvzg3zQ12J26j-iMlANePvT=w144-h38-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyqp2o6ejlf6tttyC7GLWQtsIaZivlVuO3Wfesus7kkahWjgA0g3MgpVbzr34a5or3Qm54yGpGs6heVALIlliXxrg8QFxwbJYLldZaeZPocxARXbd5VPI_GZw4j_vPXrdfotUC0Sg=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAw5YbIi77fliOMOop0bjnO90M5Sz5PcbkFRjmVmwbON9JrZeWL0qVabg-L48teoRz7eAbddO6FdagM7GU1u-0yq2na3krG48NkOHY1hD0lVQS0RvyI2YL-TQC1b7wukYv4GqlOzOQ=w288-h284-v0
Parâmetros de Desempenho de Redes Atraso Fim-a-Fim (usuário a usuário)
Tempo para transmitir pacote de um emissor a um receptor
Componentes:
Atraso de processamento na fonte
Atraso de transmissão: nas interfaces de rede (NIC – Network Interface Card) da fonte/dest. e na rede
Atraso de processamento no destino
CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA
Rede
Proc. Fonte Placa de Rede (NIC)
Rede Proc. Destino Placa de Rede (NIC)
https://lh3.googleusercontent.com/notebooklm/ANHLwAwXiDd_jwlZ2vKnygDN6k2QEvqIk_urx3cXQ5knxljoKvRcAZEd2xG3b_5Z7Wy0HAA8nxpbcOhJ2co-siOAfB4JTvMYIxmwWBPCZS7BckBGANZslJzAd3FOpcQiUPwUQtuvrktRRg=w144-h38-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzEIWHw-Xp03Jo7NLx7y1ogaVA9IzFH4QwqsJ02ujT-EQDCifr8tEKeUxJ6uNu5hlQRr9_lYA_y8vDqqVcL3dz6SWgc9Wc6Hr34tvmpFgJ25sluabGtSJ757vliUKl2PzMOKPgRLw=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxaeZBN50vXwesqeb0YOg6FY5qgUzEw5OMCZeYcGZj7dqNbGxW_GztvL5WTO9fZlY1uXz0wsVEZTFN283osJrpTKKsmd1xE2j1Qbk2M0uCne7LcAEIrQJYaA66fl96M64AnSPjC=w288-h284-v0
Parâmetros de Desempenho de Redes
Atraso de transmissão
Atraso na interface: tempo entre o tempo de o dado estar pronto para ser
transmitido e o tempo em que a interface transmite para a rede (pelo enlace de saída)
Atraso associado ao controle de acesso ao meio e criação da conexão (se for orientada a conexão)
Nas redes Ethernet depende do dispositivo de rede local utilizado (hub ou switch)
Hub gera atrasos e variação de atrasos (CSMA-CD)
CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA
Rede
Proc. Fonte Placa de Rede (NIC)
Rede Proc. Destino Placa de Rede (NIC)
https://lh3.googleusercontent.com/notebooklm/ANHLwAzJMVvVgJw96UhymnKacUnqi-xe7Y1kst7FGz6oTyBgyUtloA216senugVdr0U1V-zEDDaQkn6s5kFbcl3oOLM1_IBU2pu0Y2J7J9QD-wvl7wafzr2efgJpktP5duC2U3eiMmKaOA=w320-h240-v0
Ethernet: usa CSMA/CD
Se meio estiver livre então {
transmite e monitora o canal;
Se detecta outra transmissão
então {
aborta e envia sinal de “jam” (reforço de colisão);
atualiza número de colisões;
espera como exigido pelo algorit. “exponential backoff”;
vá para A
}
senão {
quadro transmitido;
zera contador de colisões
}
}
senão {espera até terminar a transmissão em curso vá para A}
https://lh3.googleusercontent.com/notebooklm/ANHLwAzNHp6QYRTbpd5ZBIQ8CmrbEikS2XQF6ScTQVFEqNfdW2UZL4-q99t8kQ0FJwFdSoy3ypqHz_Gkaq2Y5WhSa9caYQsiogr_LXf38GCpD6VI2jS4x32VW91110pCG4gdMtlzi8yz_g=w144-h38-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyTjIWw9Xim2QoxEsJ5XitKzcPV4Y7cy45s8pLVsPg7HJ2XgKTZRdcYPxHeVTt9GW485LuGHvewtxIdSkx5ZGfJFuWYr1qTfPf3zRmmU3F1dVyemzzU4jZAmw1CUzphXrqTuo2P-Q=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwnyI8tTySCeGJ-oh5P-A1iPyjgJfITrdh17-vVfq2vHT-kyjOo53X55pM8lzPnPN8XEBkPRQ8hywOoXBC35IgY1LolNgQfeXacG-LiEwxUfU0Zz_EQa2lGgeJ9-gf3Iz1CE9UO=w288-h284-v0
Parâmetros de Desempenho de Redes
Atraso de transmissão
Atraso na rede: tempo entre o tempo de o dado é enviado pelo enlace de
saída da fonte e é entregue na interface de rede do receptor.
Atraso na rede local até chegar no roteador
Atraso em cada hop (salto) da rede: atraso entre a chegada do pacote no roteador e a entrega do pacote no outro roteador
CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA
Rede
Proc. Fonte Placa de Rede (NIC)
Rede Proc. Destino Placa de Rede (NIC)
https://lh3.googleusercontent.com/notebooklm/ANHLwAxQnlamWID1YCGXHaEO60kjxiipdCiniNPle9uao_RBlJXRooXBjBaTds7RCMLYq1aEL4gTX3mBuaJGK0Nvkm-B7xGyp7_HtNMRSElpcbGLvEzpVB2qo7cuxzWxq2QALeRKoR_aBg=w985-h611-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAx3El05LYwk4azJK_N_bnvtAfma-dvQbtwuizGf3AcsIHLcqclTL3KdS3OuP0rpv2CIJdk03uHr_ihwQjNOVJ3hLQ4T8fNUP7E7PymfrlDVAmfzQdPe_WW60xOfr4RM5UOs0q5x=w451-h267-v0
Parâmetros de Desempenho de Redes
Atraso de transmissão
Atraso na rede: tempo entre o tempo de o dado é enviado pelo enlace de
saída da fonte e é entregue na interface de rede do receptor.
https://lh3.googleusercontent.com/notebooklm/ANHLwAxaharTZN_qNS2g2lOjU0f6xQNkTXNaGFg3m9z-8Gapdwuasw75snNT7ZvcmaQAmGIcVfsGBaBZwd_GNn6EPMX-3xhAxr6n82PLn2upalqvneZmvWFzokOLO3H_w3RbBGsbuO-5=w227-h227-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAz_xbfknjI3ekQzAoOhsFdkWfklf-w99nOAEiVVco3Mob8nKXKdBvFS1BqXhjH3Du_9stzFkgZbSKMoUJ6GTmD9_5QGjfVNEyR3xPJlPIZwUBOPTVveka8u2gp_h5kTdA0WhDFAAw=w227-h227-v0
Parâmetros de Desempenho de Redes
Atraso em cada hop
Atraso de processamento: verificação do quadro, identif. do enlace de saída, e
encaminhamento para porta de saída
na ordem de microssegundos
Atraso de enfileiramento: tempo de espera no enlace de saída até a transmissão
depende do nível de congestionamento do roteador
na ordem de mili ou microseg.
Atraso de serialização: tem necessário para serializar o quadro no enlace
Depende da taxa de bits do enlace
Atraso de propagação: tempo necessário para os bits se propagarem pelo enlace até o destino
A B
propagação serialização
processamento no nó enfileiramento
https://lh3.googleusercontent.com/notebooklm/ANHLwAzqeZU0d3zmZodk9V4ekoLnO1y3R9HF2r6YOFWtjH94dYJ1KIoq-a10-s2Q-95h83KLty-YD3vkbnU7izyYSjuyuX6WVtHv44PzGeRODH9_pYAiAdhVN6TWvLR1y2Beflu1IxGEYA=w227-h227-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwjLSM6OK9LX_q0sUm8af8oUDPGuagHgDNUL9tWn1JmND-GgPVK0j1Yk5-msKytAkfsxUxZmZo59rMUxUEUv5LiSP0llrZQRVPM1E14_8bKe_UXaXLlEECTa_DbhYde-2UTBfXe=w227-h227-v0
Parâmetros de Desempenho de Redes
Atraso de serialização:
R=largura de banda do enlace (bps)
L=compr. do pacote (bits)
tempo para enviar os bits no enlace = L/R
Atrasos de envio de um pacote de 8000bits
8000/64000 = 125ms em um enlace de 64kbps é de
8000/10M = 0,8ms em um enlace de 10Mbps
Atraso de propagação:
d = compr. do enlace
s = velocidade de propagação no meio (~2x108
m/seg)
Atraso de propagação = d/s
Atrasos de envio de um pacote de 8000bits
100m é de 0,5ms
100km é de 0,5ms
A B
propagação
serialização
processamento no nó enfileiramento
Atraso no nó
dproc = atraso de processamento
tipicamente de poucos microsegs ou menos
denfil = atraso de enfileiramento
depende do congestionamento
dserial = atraso de serialização
= L/R, significativo para canais de baixa velocidade
dprop = atraso de propagação
poucos microsegs a centenas de msegs
propserialenfilprocnó ddddd 
https://lh3.googleusercontent.com/notebooklm/ANHLwAw9H2ww9-RyIxR6TrrGnl2WgOVUhxLtx_UOqLwhDj3M5l0X5zQ52K3BoEO8-BjlEJGprAB784-9h-qVTm4WgM0ZFhebkUReGg4bBpU27VIaX37oZ56LLsinDb4pm8yH3m0Ilt7x=w985-h611-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAw5hEAYMt7hnaDnM7XN1SgWU4UJWkNEtnkE7uhmi2jIoJ4WUG3Gu5Sq817hHHp2034xzuC5d_O1b7Xaa3s-QaJItNX6s9LYmgWz0wDg9VUkyf2EG3LWCVne6-tmB-G4otRDk3lHKw=w451-h267-v0
Parâmetros de Desempenho de Redes
Atraso de transmissão
Atraso na rede: tempo entre o tempo de o dado é enviado pelo enlace de
saída da fonte e é entregue na interface de rede do receptor.
https://lh3.googleusercontent.com/notebooklm/ANHLwAyGV4jokjyn51X0MzIbCNB9J0ESg5MAojWsVGQZZCUnoqQAqU_Ysun5aWjEd3OOIbcIEgn8-I22f1NBlt2JCuW54LYkIApXvMW3u9XdwwV9DlXqS3Y1V7tnpx63Zu0QiL22de9d=w156-h54-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAz3BznmcPafFkW2vSjqjH6ovNuaDuJtgS7lX1fdpwobTCVWJb2fX0iyIL-PHPA9W0KB6SO4GteuZfr9OUNSvCtH9peEXwV9ZzroSy_OkTSS0apssYOLeYRHS801iE4P1h2vMnc1PA=w156-h86-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyy_E-2D-A9i6vNG6hBCMoHkfFv7R-Z4L1itjcRAobQud05JsG8LW86BDAp4x68N5WPpeF1fADZ8gEe-TXv4hFjpFiE6_3iLPnZYBc2eQTH2vAqvYPsCo4lVna3jui68Lg2m2Tn0w=w156-h94-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxh4Kyscn7nesHQKWE2YPiTn6Qp9mF3YQaKHd2jvfVA8aO0DECDAOFZemG193MPBU4GgiJ8RuVSDx_TviwSNf_wv7itkSnVxwkOBod1CZ1_ySzoMC4Pw5IZ-wCHVZp15Ij-iX-S=w55-h55-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAy5O_Oe1gnYrGncrE5TLMn3aqq5tmLNDV07TlA4NGMLltd-zOtVLED5fbTWcJf-nzqmvANdqMjAGf8DkVtuW9sDHv6Hx7leao6QkUMxZg6ix3W2fjvYWAvV84ng6KXXeSxeIZfbow=w55-h55-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzg9F6xE9I2NaCFIDmaGhnby8HT8NnbgMLeVFgQsdcOegjKTMWVZ9H7LycJ520nvIELXJPAZihHrbyo8BvK8msgJL8KB9h0UZrweWK_1qDPaISAajJzo1-KVtGo5S2uoH5NFwL0Hg=w55-h55-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwii0qYfm-kCj_bt4kmgpe0WV6e9wlVjdztJbnp9GMW87IG-FhcFeYDN2Ii34S4P4FLrzqxKXXmvh5iJamxZzhww7A7iS-uBpx03YYAibFXaAMjyiHB0pFSVp7i_w0KAIzUfHV0=w55-h55-v0
Parâmetros de Desempenho de Redes
Atraso Fim-a-Fim: Medidas
Atraso de ida-e-volta (RTT - Round-trip time)
Tempo em que o pacote leva para sair da fonte e a volta de uma resposta do destino
Mais fácil de medir: usa relógio da fonte para medir tempo entre envio e recepção da resposta
Atraso de ida (OWD - One way delay)
Tempo que o pacote leva para sair da fonte e chegar no destino
Mais difícil de medir: requer sincronização na fonte e no destino
RTT
OWD
https://lh3.googleusercontent.com/notebooklm/ANHLwAxCAdx6rzLo7__IQqy3jMf5PZZCc6GmSY93oqhIVK0-fdmeQcpIAIAoX4XyVRq7oMB5d54Qm5AhqVul3gF6aKSdbnfWYOu6k2o9Qjka0JcYHX2cK--Ts4DHCeAVcI9W8ts6-yUHfw=w723-h182-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAz6TcCJEROkTpshKlDk9X9sveW-ckT5H3oGmrjZTaoEVpyLZlnfEewCstE-QISK7g7bzkag7IpK_Z2IQ20ELcMAGbfjCbgfDFmcvijRRx-omJjwRTEZuYtKJKIOl8zWgXjBl0vZ=w416-h140-v0
Parâmetros de Desempenho de Redes
Atraso de ida-e-volta (RTT - Round-trip time)
https://lh3.googleusercontent.com/notebooklm/ANHLwAw26LJh2GfjyH_cvez8Gu5HR5hr-R3gy_WqUYYf6so7zMMPNgr1W627MN8R161i_wQFKx964O5fZA1CCpa8hu3sA8Xf9y3_BArvRWhhUF0xAiGeFer_AyOiGQ_1OV-INBYXoGTycw=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzIeUSVL0ob3JSNlCj03vnhL0Gzjen6_E-OuXNBw5qNrRpSBAfSh2rJ9IOUy3SSI0RHeNjdr2wdeej45vbbhoytqnnhbpVKmw9SFMeTu4sYmrtrSypeX092wU7tJa8ztxn1tF9zFA=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyPWsC01E8iL6fE7-p5koY1TLd5Ww61pXFb1YJqXynV5NcIUosBgMrHTLEuWpf7FHMpbRs1J0aKdMTgXfj1RMtrF_ZniJMZU931XC5hAbdk-_xaoFk8u_BZFvEqXhb9sb8BssuCfg=w529-h188-v0
Parâmetros de Desempenho de Redes
Variação de atraso (Jitter)
Fluxo de vídeo e de áudio são normalmente enviados separadamente
Em redes a pacotes, fluxos são divididos em blocos de dados e cada bloco é transmitido em sequência
Se a rede é capaz de enviar todos os blocos com uma latência uniforme, então cada bloco deveria chegar no destino após um atraso uniforme
Muitas redes hoje em dia não garantem um atraso uniforme
Variações de atrasos são comuns
Rede
Proc. Fonte Placa de Rede (NIC)
Rede Proc. Destino Placa de Rede (NIC)
https://lh3.googleusercontent.com/notebooklm/ANHLwAwtNdtjWwDtdlS-nxO_WkiSLerNhadz2auHXZK-wGe5MWcx-r38hmmON_vYZeHnry_17w-LxZ4FOsp0UqcKqjkQanyHBoFo4qtTPP7Uk8oP4tZ01uVyumJ_fT7ngBcMjFkjxV16WA=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxCC6xkCRvxuK079okPc6Lqq7nVXCNJUG6ARn22dL-dR2Lf8O1KWdwCGwLJm3bGfAn-NnpMUlOMMhuC8Fs9vZksdypcJchWes1zgtyFFFwRMBjReW5JRp6sNUGvXxjvT26A5jEzZg=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwADtqYXAqCs3_Fgn0lFhqev2hcSi4UtkuFaW-EEAZvL-hckzl_2E_UwTENeHIvyFqO-jnaVVmq5Z8hHf_OM0moXRKdTPsdvIE_WL6j7Hk8nCtkQMPZX-Lz84HKpbr0LLvQ-GumCQ=w529-h188-v0
Parâmetros de Desempenho de Redes
Variação de atraso (Jitter)
Causas da variação de atraso na transmissão:
diferenças de tempo de processamento dos pacotes, diferenças de tempo de acesso à rede e diferenças de tempo de enfileiramento
No projeto de uma rede multimídia, é importante colocar um limite superior na variação de atraso
Rede
Proc. Fonte Placa de Rede (NIC)
Rede Proc. Destino Placa de Rede (NIC)
https://lh3.googleusercontent.com/notebooklm/ANHLwAxY3mnRm0PenOIvW9jcKa32Eo6T3yqZPJIZNq-Wdu0-Cn6OpHFZinXOSLgiGrmLkaaBcY1XUozok790QHDt1urr45HSo25COT7dCa7mjQLsim2pcJeH3gOpxE8AkC-H81SSUEYvoQ=w416-h140-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwxIZpYXf6XfbhGcrDpTDNouzRq-Xl_0QXnCnAedpemTI66PBWQdURNNyDOU33WLDJQNTOsNgceZwiwn4XMND97MuH3GSFwAuMYnuCd9y2px96JVmX3C3Di8YaVvMw5kR51n5uF1A=w747-h189-v0
Parâmetros de Desempenho de Redes
Jitter
Parâmetros de Desempenho de Redes Taxa de Perda de Pacotes
Razão entre o número médio de pacotes corrompidos ou errados e
o número total de pacotes transmitidos
Erros ocorrem quando:
pacotes são perdidos ou descartados no trânsito
possivelmente devido a espaço de buffer insuficiente no receptor causado pela congestionamento na rede
pacotes são atrasados
pacotes chegam fora de ordem
Características do tráfego multimídia Tipos de Transmissão
Transmissão assíncrona (download)
Dado é transferido completamente antes da apresentação
Gera atraso inicial muito grande
Exige grande capacidade de armazenamento no receptor
Transmissão síncrona (streaming)
Fluxos de áudio e vídeo são transferidos e apresentados em tempo real
Impõe severos requisitos a nível de comunicação
Escopo do estudo
Estudo dos requisitos de rede para transmissão síncrona de áudio
e vídeo
https://lh3.googleusercontent.com/notebooklm/ANHLwAxLvp_FLOlBZ7WKAzLSf-YPF306vxO7P0EcpRzFk8cE5QyviuWE5GMUJw4ocoPqli2XuLUCuhp5zXSQ9J1LQGo6njTwM7hNfn_3gFm-8NsHwZf-dyof876xX8snr9qGypSr_C8b0w=w1280-h720-v0
Download
https://lh3.googleusercontent.com/notebooklm/ANHLwAxu0Ox-jnweHJwhycEXfwBx0NRCqoqOdcByXrUHmUXBKzEVkqxUhMmorwrf3M4fuQ1_AH1XB3ueKSJEIRLA3ZemlSHAQ7e_7afWmBpwnY2kvanlIgPFU_X6SJlpyzvBPRK9g6ytAA=w1280-h720-v0
Streaming
Características das fontes multimídia Fluxos de dados multimídia são caracterizados de acordo com:
variação de vazão com o tempo
Simetria bidirecional
dependência temporal
sincronização multimídia: intramídia e intermídia
tolerância a perda de pacotes
https://lh3.googleusercontent.com/notebooklm/ANHLwAyStitHwlwoZ1daMIKGSzuTJQfzBQI4f2ROxnEJ3mNr7wCBgPiYS1OBHon1tSIJjfAmrAhnfeLYI058hALfvC9mVbWAShf_CMh4RuTCbXdZqUVXFw0BQBc-Nq3ks0gyMbaH8MGt=w34-h224-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzv4eBCWdLStO68Q-Ldws2GbcZpZhW25fNhVo3An72OA-ybDnYbE7QZw27p6a5G63ypC_FdbHWS-jTK1wKjFBH8RNhSL-Wffx7R-6lnewS7jfpV7RzftFew13mmbu9mh1OQDq-nlg=w435-h34-v0
Características das fontes multimídia
Variação de vazão com o tempo
Tráfego multimídia pode ser caracterizado como uma taxa de bits constante (CBR)
ou taxa de bits variável (VBR)
Tráfego a taxa de bits constante (CBR)
Gerada por alguns codecs
É importante que a rede transporte estes fluxos de dado a uma taxa de bits constante
Em muitas redes tal como ISDN é natural transportar dados CBR
80kbps
t
(G.711 sem supressão de silêncio)
https://lh3.googleusercontent.com/notebooklm/ANHLwAyFdfsCzRiVW-NfAtIHTxOaQ7tDgr26ghUdzO1yO-rqJq49WSms26xvAaZ5cK1dhYOnBrPZRSG4Mt87fvgStE4-Q1x5tnDI4g2D7ebzIjDifttLZ0YgiwzzCKRLMM91B5oz9hYw9w=w34-h224-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxRupqWPV744MFShGx7I5fhIOVirXP9U8jbnf5fiiEmJWdyzPxSd7UXU88EaltRO2qYbKu8tEE67XJD6VdXuqTPSbZv7shoHEj7EZlzuUJj8NU6CkPqV1sKpBZbdbh7U5lJ90Wpww=w435-h34-v0
Características das fontes multimídia
Tráfego a taxa de bits variável (VBR)
Gerada por tecnologias de compressão de dados
Tráfego com uma taxa de bits que varia com o tempo
ocorrem em rajadas, caracterizado por períodos aleatórios de relativa inatividade
quebradas com rajadas de dados
(G.711 com supressão de silêncio)
80kbps
t
https://lh3.googleusercontent.com/notebooklm/ANHLwAwUlHo4XCMYx80SINVMfYmru1CD9byCW5Q3UVijmKWbq6yqC5LQw0UjXTfb74jwsiarlxtImscD86QZ2rtmQiFxM5XsrnV2bvMo1ih-W78l7763teMT7y0lsz_wNir-e5iQI2fgIg=w400-h500-v0
Características das fontes multimídia
Simetria Bidirecional
Existem dois tipos: Simétrica e Assimétricas
Tráfego simétrico
Taxas aproximadas nas duas direções
P.e. tráfego VoIP um-a-um
https://lh3.googleusercontent.com/notebooklm/ANHLwAxTiVzK3wDD4RkNsz38WVjFOR04ut0SxJYutKkarmTbz8S7yOInC7Omrp-Xq6YH5Ze5MrMvGMAplBFbvYWCbqlyVJpOIRaW_1T_JZeyYU1RuhOOIS6nUKjiF2PdycTCKxC_O6QYUg=w288-h284-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxxX-t85I3IatZ-00GO2WwC6dzVe19AvBtUYR1Sx5S9FMEHyIcKbM6HcO1YYwyQWXhfzaNACV5xXVyekXZnGz4OnFq9W8J6E6hbBtHCyljNrgVDvD8dyg4e4T1ZzUc_PMq6kgwsSg=w185-h155-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwjCAepUnCKm7y61IsONJvxxS361WbD77_OyjpQ2rei_jxF1nqjc8RKK09XUfF9bdZiQKDyq9DmQkFUgS_BYq2wfgDlqTEe4te4aEJbNzzzQvBacyRbObrMU_Z4UkNI5HamNAsa=w161-h91-v0
Características das fontes multimídia
Simetria Bidirecional
Existem dois tipos: Simétrica e Assimétricas
Tráfego assimétrico
Tráfego em uma direção pode ser muito maior que o tráfego em outra direção
P.e. Streaming de vídeo, Vídeo sob Demanda (VoD), TV sobre IP (IPTV), ...
RedeServidor de vídeo
Vídeo
Comandos
Características das fontes multimídia Dependência temporal
Para aplicações pessoa-a-pessoa (VoIP, videofonia e videconferência)
atraso total de transmissão das imagens e da
voz de um interlocutor da fonte para o destino deve ser pequena
senão a conversação perde em interatividade
Nas aplicações pessoa-sistema
Atraso pode ser na ordem de segundos
Ola Oi
Colisão de palavras devido ao atraso
Características das fontes multimídia Sincronização multimídia
É a apresentação temporalmente correta dos componentes multimídia que compõem uma aplicação
uma das principais problemáticas de sistemas multimídia
https://lh3.googleusercontent.com/notebooklm/ANHLwAzgWakuqjKLVG7p2MiTJFyQg1zZX_an0YQBnLhVRyhvthNoEdKyMMkh6UM5s2Yp8LJnO0YEF6A_qsQYhaMjh9lxU2uNXWwepGCMB-hexq9X0NIP9qnJillh7mydCkkOIm-Tbpp4kw=w903-h137-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwEZ7Zl80x5LCBkUn7rsO3R4O6SyL4AYqBXc4f5RncjIs6YulrUL6Yoa8db7WqXp9hu6dgL-q0DjOUY8q4iKDW4DeqyrTsZao2iW5fxlU-hxOnpOHNcnLYZsiOs_5P7gveRhHSZvA=w1018-h175-v0
Características das fontes multimídia Para mídias contínuas (vídeo e áudio)
Sincronização intramídia: apresentação temporalmente correta
significa que amostras de áudio e quadros de vídeo devem ser apresentados em intervalos regulares
senão a qualidade percebida será baixa
Exemplos:
0 1/30 2/30 3/30 4/30
Vídeo 30 fps 1 quadro a cada 33,33 ms
Áudio 8000 a/s 1 amostra a cada 0,125 ms
https://lh3.googleusercontent.com/notebooklm/ANHLwAxXFYGZCIzVjZu_1BsdWhFQzdudzatuC6bmcepI3NflL61wCXqv_6Efji_LHV3mIjRx5stGPV2vOlBcMulvh6fHMjJgIi1Z8d1bqqTNHxD2R5xdN3_tXrjHtY-8ZFa17xbzcPOtmg=w903-h137-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwaHrn97M3QHuFJtsKCBfaCiEcESnWg3p7M23mf6XKYJhyZmMBAJcKa8Nrdhq8pbeowbVvc9CeM-A5-rd3E5Go3qs3FqsGpYxzmONcPiP6mjw9fg7msEzIvrEb93vGzryTeR0KAhw=w34-h373-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyZ5YM9GeXSkMmn8kjGHAouXuo6KcHlMvNLWfJe7pQKc8pwFcuqgobBCWNfRVHmnK1txfuRwmrQKgG3cjZ35oTMj55LpWcc-zbUy3U19MWMEVl1806jHo79JnDh3YUHS0Uv3avw-w=w709-h34-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyeBb4v9hRuk2Df7-_5qn0QEaB9SOT6pSIY8VhjwoPWnME4sU_C8pe68eOSnPpDLRj1eTOahVioThVlx-H7SqMlgCLarqq_3wEmNyX1B5Ik0HSHY3w0Rj5YlyYEgiyDmKrWFybxPw=w1018-h175-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxt39yNgtKKcicqDn58NshnCXQj_OG8LJANrO7AKtRCuKEmubtbj_mHK1-gSCMBHTssmgHUSumWSQRDRAdZbriw3JiM1IzCXnBcURZzMdKOiV7terLp8xNIrRZaqijkYExmEhY0HA=w396-h225-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwemBElTw4qY7vDm-ZJpHWJlIQwA5BPaqvqEmT8FbeaSuPMPACdFslhTrpLh1BZYjwm3HPXR5NZZe6H81MNbwrqFvHD3Rbv7_aazqbzMU-gryYELIhnQUVynwADd2oS4yh3nGSbpQ=w279-h181-v0
Características das fontes multimídia
Sincronização intermídia: Apresentação temporalmente correta significa que
os relacionamentos temporais desejados entre os componentes devem ser mantidos
0 1/30 2/30 3/30 4/30
Vídeo 30 fps 1 quadro a cada 33,33 ms
Áudio 8000 a/s 1 amostra a cada 0,125 ms
266 amostras a cada quadro
Características das fontes multimídia Sincronização intermídia: Fontes de perda de sincronismos
Diferentes tempos de processamento na fonte (equipamentos com
diferentes cargas de processamento com o tempo)
Diferentes atrasos na placa de rede
Diferentes atrasos de envio do pacote até o destino
Diferentes tempos de processamento no destino
Características das fontes multimídia
Sincronização Intermídia: Distorção intermídia
Parâmetro que mede a diferença entre: tempo efetivo da apresentação de um
componente, e o tempo ideal definido na relação temporal especificada
Valor aceitável para a distorção intermídia é dependente dos tipos de mídia
relacionadas
Mídias envolvida Modo ou Aplicação Distorção intermídia permitida
Vídeo e animação correlacionados +/- 120ms
Vídeo e áudio sincronização labial +/- 80ms
Vídeo e imagem superposição +/- 240ms
Vídeo e imagem sem superposição +/- 500ms
Vídeo e texto superposição +/- 240ms
Vídeo e texto sem superposição +/- 500ms
Áudio e animação correlacionados +/- 80ms
Áudio e áudio relacionamento estrito (estéreo) +/- 11ms
Áudio e áudio relacionamento fraco +/- 120ms
Áudio e áudio relacionamento fraco (música de fundo) +/- 500ms
Áudio e imagem relacionamento forte (música com notas) +/- 5ms
Áudio e imagem relacionamento fraco (apres. de slides) +/- 500ms
Áudio e texto anotação de texto +/- 240ms
https://lh3.googleusercontent.com/notebooklm/ANHLwAzhldrn0AaW2IUpXAwuDMTcqHSBYoVxJb0nkzUvEWfu1v-b0JtlyteBbXDDOBV2s-IEtMwHd0ATlSLkjfXuR7MqS5beeH1LY9XrIFUJ5IrOfyH7yQqRS0VC9ZDayxQyuf2JYFge=w259-h76-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxuL3t-l8etnCWYgaR4IMQRVaHhnr2ZCdZ6bYLIYGnIWkQfRQxlT-khVNBMp39XPONc5cD7t5bjjlk0wBpqMsLqpswdSpth5iASD-koJiNTdVFrIyyZG40-m_fKJ8483buGqk4Cyg=w773-h301-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwOoT5PW14S_kG-dppHfceNUm8ySMZW14glTZO_PfDya3VOFLKzNzCG92jdV-qlfy8S3ikyfvbx-9LzWHCc7CXwAdgKeVDcKUnV3JzM6cqwW8C-7Eo25aCAh41dBcOmmfwE3mG0gw=w135-h76-v0
Características das fontes multimídia
Tolerância a Perda de Pacotes
Transferência livre de erro não é essencial para obter uma qualidade de
comunicação aceitável
informações multimídia toleram certa quantidade de erros
Taxa de erro tolerável é dependente do método de compressão
Pacote de voz perda
CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA Requisitos de Redes para Comunicação Multimídia
INE5431 SISTEMAS MULTIMÍDIA
PROF. ROBERTO WILLRICH ( INE/UFSC)
ROBERTO.WILLRICH@UFSC.BR
HTTPS://MOODLE.UFSC.BR
Introdução
Objetivos do Capítulo
Identificação os principais requisitos de rede de comunicação para
transmissão de áudio e vídeo
Analisar algumas tecnologias de redes locais
Conteúdo
Definição de alguns parâmetros de desempenho de redes de computadores
importantes para a comunicação multimídia
Taxa de bits, vazão, atraso, variação de atraso, taxa de perdas de pacote
Caracterização das fontes de áudio e vídeo tempo-real
Identificação dos principais requisitos de rede para a comunicação de áudio e vídeo
Análise de algumas tecnologias: Ethernet e ADSL
Requisitos de rede para áudio e vídeo Identificação dos principais requisitos para áudio e vídeo
Verificar níveis de desempenho que a rede deve oferecer para se
obter boa qualidade. Requisitos avaliados:
Eficiência de uso de recursos da rede
A tecnologia usa de maneira eficiente seus recursos para transportar os dados multimídia?
Requisitos de vazão
A rede oferece banda suficiente para transportar meus dados de áudio/vídeo?
Requisitos de atraso e variação de atraso
A rede oferece um atraso pequeno e constante para meu tráfego de mídia?
Requisitos de confiabilidade
A rede produz muita perda de pacotes que afeta a qualidade de apresentação das mídias?
Eficiência de uso de recursos da rede Comutação de Pacotes vs de Circuito
Comutação
Processo de alocação de recursos para a transmissão.
Existem dois tipos básicos de comutação
Comutação de pacotes: não são reservados recursos
Pacotes usam os recursos sob demanda e, como consequência, poderão ter de aguardar (entrar na fila) para conseguir acesso ao enlace de rede.
Comutação de circuito: reserva de recursos
Recursos necessários ao longo de um caminho (buffers, taxa de transmissão de
enlaces) para prover a comunicação entre os sistemas finais são reservados pelo período da sessão de comunicação
Eficiência de uso de recursos da rede Comutação de Pacotes vs de Circuito
Comutação de circuito não usa recursos de maneira eficiente quando dados multimídia são transmitidos em rajadas
Se usuário reserva uma largura de banda igual a seu pico de taxa de transmissão:
parte da largura de banda é desperdiçada em redes de comutação de circuitos
É baseada em reserva de recursos
Taxa de pico (garantido pelo circuito)
Desperdício de recurso
Tráfego de mídia
https://lh3.googleusercontent.com/notebooklm/ANHLwAxzU39s98nAuMUlOPU3SCFIV8ymAOkuyJUeDOK0rZVJbESzGum4GvAFBie9H98YqMI0aOayMXVDSx2y1LUuHyjf5-O_CZVqcMOXPxwkj44db3habjwgsFAFWsN_soeRr_RD04x5=w355-h242-v0
Eficiência de uso de recursos da rede Comutação de Pacotes vs de Circuito
Comutação de pacotes utiliza recursos sob demanda e o tráfego é agregado no enlace (multiplexação estatística)
Melhor técnica para uso eficiente da rede
aplicação pode usar tanta largura de banda quanto necessário sujeito a um valor máximo
quando uma aplicação não usa toda a sua largura de banda outra aplicação pode usar
p
p
p
3*p
Agregação do tráfego
Requisitos de vazão
Requisito de vazão de transmissão
Requisito dependentes da qualidade/codec escolhida para áudios e vídeos
transmitidos e da técnica de compressão utilizada
MP3 (compressão com perda com diferentes qualidades)
32 kbps – qualidade aceitável para voz
96 kbps – geralmente usada para voz ou streaming de baixa qualidade
128 ou 160 kbps – qualidade intermediária
192 kbps – qualidade média
256 kbps – taxa comumente usada para alta qualidade
320 kbps – Qualidade mais alta suportada pelo MP3
Taxas de bits geradas na codificação
Na rede há uma sobrecarga de protocolos, aumentando as taxas nominais indicadas
Requisitos de vazão
Requisito de vazão de transmissão
Requisito dependentes da qualidade/codec escolhida para áudios e vídeos
transmitidos e da técnica de compressão utilizada
VoIP (codecs ITU-T)
5.3 a 64 kbps de vazão gerados por fluxo de áudio (depende do codec)
20 a 80 kbps ao nível de rede (depende do tamanho do pacote de voz)
VoIP outros codecs
700 bps – usando codec Codec2 na mais baixa taxa, som melhor com 1,2 kbps
800 bps – taxa minima necessária para entender as palavras, usando codec de voz FS-1015
2.15 kbps – taxa minima do codec Speex
6 kbps – taxa minima do codec Opus
Taxas de bits geradas na codificação
Na rede há uma sobrecarga de protocolos, aumentando as taxas nominais indicadas
Requisitos de vazão Requisito de vazão de transmissão
Outros áudios
32–500 kbps – áudio com perda usando o Ogg Vorbis
256 kbps – MP2 Digital Audio Broadcasting (DAB) necessário para alta qualidade
400 kbps–1.411 kbps – áudio sem perda usado nos formatos como Free Lossless Audio Codec, WavPack
1.411,2 kbps – format de som PCM linear CD-DA
5.644,8 kbps – DSD, usado no Super Audio CD
Taxas de bits geradas na codificação
Na rede há uma sobrecarga de protocolos, aumentando as taxas nominais indicadas
Requisitos de vazão
Requisito de vazão de transmissão
Vídeos
16 kbps – qualidade mínima para videofonia
128–384 kbps – videoconferência orientada negócios
400 kbps YouTube 240p videos (H.264)
750 kbps YouTube 360p videos (H.264)
1 mbps YouTube 480p videos (H.264)
1.15 mbps max – qualidade VCD (MPEG-1)
2.5 mbps YouTube 720p videos (H.264)
3.5 mbps typ – SDTV (usando MPEG-2)
3.8 mbps YouTube 720p (60fps) videos (H.264)
4.5 mbps YouTube 1080p videos (H.264)
8 to 15 mbps typ – HDTV quality (MPEG-4 AVC)
19 mbps aprox. – HDV 720p (MPEG-2)
24 mbps max – AVCHD (MPEG4 AVC)
25 mbps aprox. – HDV 1080i (MPEG-2)
29.4 mbps max – HD DVD
1.4 gbps– 10-bit 4:4:4 não compactado 1080p com 24fps
https://lh3.googleusercontent.com/notebooklm/ANHLwAxYgfVNaxFKJVTeDe48E0IhvuMHhHFU7wf5vj_UyRXb_HNSsJvkE3vOBp7NPvWTEDwLvCtlL6m2SB-PArepoYvrCbF59QtAHZzUC8bE_OETIfq9N8jFX9e2bOYYnhNZf0NkTYfXYg=w884-h254-v0
Requisitos de vazão
Requisito de vazão de transmissão
Requisitos de atraso e variação de atraso
Atraso fim-a-fim
Sempre existe um atraso entre a captura/leitura de uma informação em uma
fonte e sua apresentação em um destino
gerado pelo processamento da informação na fonte, sistema de transmissão e processamento no
destino
Para videoconferência e VoIP: entre 150 e 400ms
Para aplicações baseadas em servidor: na ordem de segundos
https://lh3.googleusercontent.com/notebooklm/ANHLwAw6qngFzk1yAcjPIlNplLaEskhDozHyRU1ct6zokI7x6lLeeeGlNmzHQh-HMqr7d689VvhvnlWQ8Sz5UgpcEilO6T60ZMbHwNg0GHbTV5bCW1yYvCIbTPF-Tq0l4vjJTkykTcyORg=w701-h230-v0
Requisitos de atraso e variação de atraso
Variação de atrasos
Em redes a comutação de pacotes, os pacotes de dados não chegam ao destino em intervalos
fixos
necessário para transmissão de mídias contínuas
Para videoconferência e VoIP: deve ser limitada a um pequeno valor (inferior a 30 a 60ms)
Para aplicações baseadas em servidor: pode ser mais alta
https://lh3.googleusercontent.com/notebooklm/ANHLwAyEP_WzJj39oFLx2CTmdPHGkh8ohmIUcU2qiU9ds0bB8FMgAFa9QjoPdr17qav6s4mu_1fetLlc39u9AUkYhVVo6UxsLqwSOfrtEoUJQpE_4o-x9atwzNu2DmFzePGYIw621KDSnQ=w127-h93-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAy7uDiPXYnZrKVTVSRTTnAOKHHhoQkgIYWb_NA-9B9YXKSzjtLCYkt-YuThsseryqigGX7oooTWUESCZyPkAGdBe5b750wHvc8CceT2POwWYLgkb_7OhMjyy6-LWNfcNCSqImgCZQ=w84-h58-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzTi2cJtV0Cpd1g1pjaARkgoJloVID57wUI_uQHi7d5FkB2CVt9fZBdwD29TgacEhA7m2cKvdzNuPH4VANW1m8SPIhIT1_HEk-tRyVId39e4J1p3ZPQ47CmmN0MR7UXPnjJ2HJbMw=w151-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxdGP8ZM23XXw5nS5s3deHCtN4L3TIFbetS_VUQEKC5p2WfBmlN-t_yLdeQaTtx4cRD8EY8KbXS72JQeb_V84YSFRLz4_i2IJMWD7rg4OT-zlN6MsTt8hK295CvGT7tCR-CwrbA=w701-h230-v0
Requisitos de atraso e variação de atraso
Variação de Atraso é removida com buffer FIFO no destino
Técnica de bufferização:
pacotes que chegam são colocados no buffer em taxas variadas
dispositivo de apresentação retira amostragens em uma taxa fixa
princípio: adicionar um valor de atraso variável a cada pacote de tal forma que o atraso total de cada pacote seja o mesmo
Fonte Processamento Rede Processamento Dest.
Buffer de
uniformização
de atrasos
https://lh3.googleusercontent.com/notebooklm/ANHLwAyTG8zV5O5xKMslX9Q_RI36hUIX7dj-fWePS1EPlmDf7dJmRPFSr9GakdzTMsmgNRF3Hw9BZ8XdfVHqDpX9M46-k3-2gGNwNLhWvZRjF47o3YKNYEcfrIvuAX6iqFKld-H63avn=w82-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAy4PhPpXIbQm3vD-ZXhV_IVCFB_QBZeP-6kPiJ3HhCO45A8zcZAh6K0DBcceyZFKQjhUCb9fafVdKZTcqM95OyEV1JdeQ7k20ri4-VJlok7Se1_H0LsCfEx0YKf6mdxJI9YIibSWA=w158-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAy4vj8qtpfgV9g2IpE8s7d-YiKQTIwr5Yl1PBWXfUEG9lVr1yIIUkZbgCXPfjAPIQuuS1ErUAl3iyrxLYBE-I1CGC95TUqJqwDohvmiq12zdSLi4wFScjJnuzwW6U2o8_Sz6odENQ=w158-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAys2jnrhH73YUOObRsGSMsbqDoEH4kwRRDzTre7qEdPsRSRcVEgb4WdZRNUMCSqXZkaTd35Jn_cEkpj8e4Kq_C9Pvk-6_klrDO_fVMKXqvZGuryhmj8TUGtfko0gTfwRwbVWJ5Aug=w75-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwyGM8AvZfjTU-EMQ8VmwaXrf0Hp-gPlVhY4OriErVdz604zhpE0qOCOT6gygM8zJ-ZFHx62YTwjKqEs6c1lk_kWjHp2Xbs9CtPm54EztbqgJAfvAx22dWt1cRJB9-MHc9M5uPyxw=w82-h100-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwz9BNU08U99qg9VZ5xXEM5c1KBniellTaO8tL8J5oaIqQCRQ3zgH4rKTUsZVw1Gr6DyocZfqJTLu8G41DoaAuExsMPVR2ATrdP_I2cFsekoeqOEY-eoT6gLvDT7RszDHqHDPUT=w127-h93-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwco0SjNhYk9XoBH9UcVkpu0ccu6TqtyTBAdE6lTlLmecYn5ljPLVsXQ0oNrGO5V58xiZvLhB00vHz8BMWkRheJDKB3Mgpm2-ddy9wJ3go0_Jot1egvQnGJc1kjANq6E8gKFwFaZQ=w84-h58-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwvtquPa--IhOwOMxfXGN6Y38JAKZSces3_TtNiaS-1ipchYCV25iz347-aIaGxVDGn8C5MCW1NbNb71wXnKcAlLVYwwD0PnN_cCldRUTsXaq2uHx452WNx70ebsdfd_2zX3xx6ZQ=w151-h100-v0
Variação do Atraso:Técnica de Bufferização
Supondo:
dmin: tempo mínimo de atraso do pacote
dmax: tempo máximo de atraso
Se um pacote com atraso de d é bufferizado durante (dmax-d)
todos os pacotes terão um atraso fixo de dmax
destino partirá a apresentação dmax
cada pacote será apresentado em tempo
Tempo máximo de bufferização é dmax-dmin
maior este valor, maior é o tamanho do buffer necessário
buffer não deve sofrer sobrecarga ou subutilização
tamanho do buffer não dever ser muito grande
significa que o sistema é caro e o atraso fim-a-fim é grande
d
dmax
dmax-d
Fonte Processamento Rede Processamento Dest.
Buffer
Variação do Atraso:Técnica de Bufferização
Buffer de Apresentação
Existem duas classes de operação para os buffers de apresentação:
Tempo de bufferização fixo
Tempo de bufferização adaptável
Variação do Atraso:Técnica de Bufferização
Tempo de Bufferização fixo
Primeiro pacote do fluxo é bufferizado por um período de tempo de B
Pacote seguinte é apresentado numa taxa fixa se ele é disponível
Quando a variação de atraso não é muito grande e B é apropriadamente selecionado
variação de atraso da rede pode ser removida eficientemente.
tempo de transmissão do pacote
1 2 3 4 5 6
B
tempo de chegada do pacote
tempo de apresentação pacote
Variação do Atraso:Técnica de Bufferização
Tempo de Bufferização fixo
Mas este esquema não considera o atraso real do pacote
Mesmo se o primeiro pacote sofrer o atraso máximo da rede, ele é atrasado de B segundos
Causando atraso extra desnecessário
VoIP: em geral o tempo de bufferização é de duas vezes o tamanho do pacote de voz
Exemplo: se o pacote de voz for de 20ms, o tempo de bufferização é de 40ms
tempo de transmissão do pacote
1 2 3 4 5 6
B
tempo de chegada do pacote
tempo de apresentação pacote
Variação do Atraso:Técnica de Bufferização
Tempo de Bufferização fixo
Embora esta técnica seja fácil de implementar
Pode resultar em qualidade não satisfatória de áudio
Atrasos podem variar, e se aumentar aumenta o descarte de pacotes
Não há um atraso ótimo quando as condições de rede variam com o tempo
tempo de transmissão do pacote
1 2 3 4 5 6
B
tempo de chegada do pacote
tempo de apresentação pacote
Variação do Atraso:Técnica de Bufferização
Técnicas de bufferização adaptativas
Realizam uma estimação contínua dos atrasos de rede
Via os parâmetros dos pacotes RTP e RTCP
Permite acompanhar a situação da rede
Várias operações devem ser realizadas para o cálculo do tempo de apresentação dos dados
Compensação do desvios de relógio
Compensação do Comportamento do Emissor quando do uso de técnicas para aumentar a confiabilidade
Compensação do Jitter
Compensação da trocas de rota
Compensação da reordenação de pacotes
Definição do momento de adaptar
Variação do Atraso: Técnica de Bufferização
Análise baseada no modelo cliente/servidor
Supondo:
destino consome dados a uma taxa constante
A(t) a função dos dados que chegam e C(t) a função de consumo
C(t) aumenta com o tempo em uma taxa constante
A(t) não aumenta a taxa fixa devido a variação de atrasos
Assumindo:
0: tempo de envio do primeiro pacote
t1: tempo de chegada do primeiro pacote
t2: tempo de apresentação do primeiro pacote
Para satisfazer os requisitos de continuidade
A(t-t1) dever ser igual ou maior que C(t-t2)
a diferença é bufferizada
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
https://lh3.googleusercontent.com/notebooklm/ANHLwAx90KQ1CQWyCc3blRmd01zzjWuE5nbExuj1VNeTdzcs-lgbc6g6T7dC1FtvHvrCFC0f-UCHtI8DTrJdJTxUV2wgNnuuKUJA9ZJqgdKQA2zhu1fCOrVVrPDixvAlj287HI_9lBNY=w177-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwb988fRkoNhyKJiowDrVx2t3NORmjtpMVBGk5XPhL3JvDP_pop6FwlPkiCFB8SUtDqQ5MOUbXYNMy18EWQyhxDsQDTevNHdqf3wnlQYrkys8UjaEPWEkXnmUhRLNnuhbTjhXEPYA=w185-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAynsLidVsZ_qjz7Km3MuE3jd9bjb8QPmpPJlCvGeIE2A20u5ZMUd5RFonTmpXF92qFlRfYmml65UtxdG0PZw4aCn9MA-5hPnXzn4WJoptNp-hWPJF5N-jkptYNS-x6dW5srHiBlNA=w177-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxyBGvh-wd-wGyrukNVWi6eVkt5tSFk6KAQXjOh5FIx0ALUEE_3XwuKiillqgd6NtTHiZR25nJzcjrSfxQdDeBzLekadnMDkvXVKF4IzQ4cFLwmDnctBG6F5TeFBt61b8QR8D8Opw=w244-h161-v0
Técnica de Bufferização
Requisitos de largura de banda
Inclinação de A(t-t1) representa a taxa de chegada de dados
Valor médio da taxa de chegada deve ser igual a taxa de consumo
Se a taxa de consumo é menor
diferença A(t-t1) e C(t-t2) (ocupação do buffer) aumenta com o tempo
para o sucesso da apresentação
tamanho do buffer é infinito ou
apresentação do fluxo pode apenas se mantida durante um tempo limitado
senão correrá sobrecarga do buffer
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
https://lh3.googleusercontent.com/notebooklm/ANHLwAyyenVnf4dzuCOE5wp2iIba3PsQCpPmn4L1EVGwma_oxAyMnvlt8_by4hTHQrizOipymU0qtb6PV6VvQ07FE3HzEzrThIcl7VgsguVexwqwkfwjAYnY-I0XFiwH7kz06vZQtRzw=w177-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAz73Y0SzzH5IwWJhZrsZ4GbOoqPCoHF8sj4K272ctUNqSzSBrSntUc2fDfYiEby9Ey9msJy5UI1XKQQZlGIXI3BfNL4dLcytuBF8zAumgtSszIkuq2KnGukoYw-7uPs2tVVJQ5_Sw=w185-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyfHVsvJ5jhlmX_6-EocNPmjX-A0ik4itEM5Ca82eLTShvOG7AoEYdLDNtc5q1Nftm6IAvjt8bztgVR5aOibEC-CmvRA0LDdiEp9-yEoENHU41GwaowRDDPCzuuA2rwNdSDo14x5A=w177-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAyXy0CKFQz2DfZKL3rYlwOAArxfdQNCurg6YfVlpsTd9NTyc6aUrMzIIIVqMFOpOObjNvbWkezUnz4n50OzEWVLgfnIeV6hDLoKpglBnvcfi_Yvn57NpZU1QH61HH2Es3KsL8IgfQ=w244-h161-v0
Técnica de Bufferização
Requisitos de largura de banda
Conclusão: controle da taxa de transmissão deve ser usado para que a taxa de
transmissão seja próxima a taxa de consumo
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
https://lh3.googleusercontent.com/notebooklm/ANHLwAwryaEi97sN-o-nEpsocD-cDjzPcfFcnB1wlIdqqsod_1pm2ggArtPJ5RvuVrvMEttJ-UTlZPcju1xBhuAEV7Yo7BN2UPchZnBDLDGqah16AMfSriU-K5o5kDtYLzWJGKu6BRovQw=w177-h165-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxpB28-vT5F9_lrRVW2eJ0kASrsA71k33YRNWJK-EnRvN-4HxrySuNunZcFhx0QTPVPVbp6mAeMKHp3DZCevdYyCZl9eXh4rAZSL0D9ODiAt93Bkyqs-D5tEyBxqTwRiMz22Syhdg=w177-h165-v0
Técnica de Bufferização
Requisitos de largura de banda
Se a taxa de consumo é maior que a taxa de chegada
para satisfazer o requisito que A(t-t1)-C(t-t2) não seja menor que 0
t2 deve ser maior (atraso inicial maior)
tempo de resposta mais longo
requer tamanho de buffer maior
maior o fluxo a ser apresentado, maior é o atraso inicial e maior os requisitos do buffer
não são desejáveis nem praticáveis
Conclusão: transmissor deveria enviar na taxa de consumo, e a largura de banda de transmissão fim-a-fim deve ser ao menos igual a taxa de consumo
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
tempo
dados
t1 t2
A(t-t1)
C(t-t2)
Buffer vazio
Rebufferização
Requisitos de confiabilidade
Requisito de difícil quantificação
As aplicações multimídia são tolerantes a erros de transmissão
Devido aos limites da percepção sensorial humana
Consequência: perdas geram redução da qualidade de apresentação
Requisitos de controle de erro e de atraso fim-a-fim são contraditórios
pois muitos esquemas de controle de erro envolvem a detecção e retransmissão do pacote com erros
ou perda
implica no aumento no atraso
para transmissão tempo-real de áudio e vídeo, o atraso é mais importante que a taxa de perdas
é preferível ignorar o erro e trabalhar simplesmente com o fluxo de dado recebido
Para VoIP:
ideal é inferior a 1%, acima de 25% não é tolerável
CAP 6. REQUISITOS E SUPORTES DE REDE PARA MULTIMÍDIA Análise de Tecnologias de Rede Local
INE5431 SISTEMAS MULTIMÍDIA
PROF. ROBERTO WILLRICH ( INE/UFSC)
ROBERTO.WILLRICH@UFSC.BR
HTTPS://MOODLE.UFSC.BR
Introdução
Objetivos do Capítulo
Identificação os principais requisitos de rede de comunicação para
transmissão de áudio e vídeo
Analisar algumas tecnologias de redes locais
Conteúdo
Definição de alguns parâmetros de desempenho de redes de computadores
importantes para a comunicação multimídia
Taxa de bits, vazão, atraso, variação de atraso, taxa de perdas de pacote
Caracterização das fontes de áudio e vídeo tempo-real
Identificação dos principais requisitos de rede para a comunicação de áudio e vídeo
Análise de algumas tecnologias: Ethernet e ADSL
Ethernet e a Comunicação Multimídia
Ethernet
Protocolo Camada 2 (Enlace) de interconexão para redes locais
Bandas: 10, 100, 1000, 10000 Mbps
Dois Tipos
Ethernet com meio compartilhado CSMA/CD
Controle de acesso CSMA/CD ( Carrier Sense Multiple Access with Collision Detection)
Uso de Hubs Ethernet: repassa quadro entrante em uma porta nas outras portas
Banda é compartilhada pelos computadores ligados ao hub
Ethernet Comutada (Switches Ethernet)
Uso de Switches Ethernet: repassa quadro entrante em uma porta em uma porta destinatária
Cada computador recebe a banda nominal
https://lh3.googleusercontent.com/notebooklm/ANHLwAxtcpysmkk42lAwg_XAovl7_PO9i7SvjX0WpeoBp2ZRi4-4Mrx8hBrRqaOg4qBSQGWXytuppX-rjKh8rDH8JF-oXfHDVYrhwqAiRxoguf9NBzf3P23eC9Ju-JyP0TzFk0WB0IwsUg=w320-h240-v0
Ethernet CSMA/CD e a Multimídia
Largura de Banda
Bandas: 10, 100 Mbps
Ethernet CSMA/CD não poderiam ser mais carregadas que 70% a 80% para manter as colisões a um nível aceitável
Método de acesso CSMA/CD
Tem comportamento não determinista
não permite o controle de tempo de acesso e da largura de banda
Em redes carregadas gera atrasos e variação de atrasos consideráveis
https://lh3.googleusercontent.com/notebooklm/ANHLwAyQQ1Eh3y1QnnnxbVW1vAHzhEOOkrdhS8ojxgMLzmcCONuJl6ed-QIUUMUIyeyjDJWLLj3wZQHhF15UlgvWTD80V0jLblCTG2RKzyqdEOu3jUgXNwLGxmEOLQcEitk2QaIK0DhJ7Q=w320-h240-v0
Ethernet Comutada e a Comunicação Multimídia
Banda
Bandas: 10, 100, 1000, 10000 Mbps
Switch
Não retransmite quadro que recebe nas outras portas
Possui uma tabela de encaminhamento e retransmite o quadro apenas para a porta adequada (se conhecida)
Equipamento que aumenta a eficiência da rede
Melhora a vazão total
Reduz o atraso e variação de atraso na rede local
https://lh3.googleusercontent.com/notebooklm/ANHLwAxZ38ySGkNETDh3cKZJq1ZwwdnvgMHqJcxNtO9h8ygiPWw_8cPmBBFjHssrZXWkF_p4hANV9q7sPCmnT7Xbv8Fus_IvYe_IePoVi5BCbswCG9n1Ydp3x2ZASFVSFQm4kOQRTv9-=w320-h240-v0
Ethernet e a Comunicação Multimídia Gerenciamento de tráfego
Switches convencionais não oferecem mecanismo para assegurar uma distribuição igualitária da largura de banda nem mecanismos de prioridade
Não se pode dar um tratamento diferenciado para
tráfego tempo-real sobre dados convencionais
Utiliza fila FIFO agregando todo o tráfego na porta de saída (sem priorização)
Priorização de Tráfego com 802.1Q e 802.1p
Padrão IEEE 802.1p
Define uma metodologia para a introdução de classes de
prioridade para o tráfego
Mecanismo de indicação da prioridade do quadro baseado no campo Priority do padrão
802.1Q.
São suportadas 8 classes de tráfego (prioridades), com múltiplas filas de prioridade estabelecidas por porta
especifique um mecanismo de reordenar os pacotes nas filas
Não gerencia a latência
requerida para redes de tempo real com suporte à áudio e vídeo
https://lh3.googleusercontent.com/notebooklm/ANHLwAx6uOAdH-0X0Ckugcw47mT1hkIH5BW0tIK2qlEvWbNCGIhoJxP8DvU5pcZGYNaN0HZ1W-O1T0Ws5ROOyuwrxqYm13muF5zZYgKi-TXKDGIjIG9Zpzd_ZqsX1JgHam8Ov-682B5zcA=w356-h256-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAxgeQQ151n5rk2ITyf7E_N2bI7Iw2uGRxEuIQMg2sgb-8YDRFGTlw9zBmBnVEEvhTGW31CrEjEWSa_4GV9HheNchLNbGCDsk_rdDT6rbO_AavvkKK2bsEqV0DO7O_1KSLlaVcZ_=w392-h282-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAwAJwikksUaBsNijFNP5sdLxhLeVbWZsgcrk9lyO27eLMjyXlrik2Nti2uGGFX31rnvHVhD_r_Sy_Xxipqv6fg3bI-b0kv3raSRdAC3ZFlSrc1BEeEBy0LRmPMKFA-hmubTkBF3jg=w412-h153-v0
https://lh3.googleusercontent.com/notebooklm/ANHLwAzi1dtT1gaFd5uy2gGOexI7xCWwlzfk5Ot2-fPmEQPDrB0fIIs8UucEbaEkegRnapEZoU_cy6PycADFPEwl7O9N2ZhAWaADjm0JR74ADnDfjAay7R5TUsAq4TdyMd93_gwyWKcDlg=w800-h204-v0
ADSL e VDSL
Tecnologia de Acesso que usa a linha telefônica
Utiliza os pares de cobre das linhas telefônicas para
transportar informações digitais
Tecnologia baseada em modems que convertem linhas de telefones de par-trançado comuns existentes em caminhos de acesso para multimídia e comunicações de dados de alta velocidade.
É uma tecnologia assimétrica
Fornece maior largura de banda para downstream e outra
para upstream
Torna esta tecnologia ideal para navegar na Web e vídeo sob-demanda
Usuários destas aplicações tipicamente baixam mais dados que enviam
https://lh3.googleusercontent.com/notebooklm/ANHLwAweGnuNMU9_w7Bbmu1Lav00nLa2AOOZ-BVLSN0gIpLegq8rrYgIOyRcKAJNC6yTVuRJosTNeJjfqmcpwMNYXKmxki1dIe1jNU39zXjv6ztVJOZJrhE4q1VWrIkOncYDuVC-U89h=w698-h445-v0
ADSL e VDSL
Vazão
Taxa depende de vários fatores
comprimento da linha, categoria do cabo, presença de derivações, e interferências
Provedor não precisa garantir 100% do upload e download contratado:
Deve garantir ao usuário (Res. Anatel 574/2011):
Uma velocidade instantânea de no mínimo 40% da velocidade contratada, e;
Em média mensal, a velocidade nesse horário não pode ser inferior a 80% da velocidade contratada
ADSL/VDSL e a Multimídia
Velocidades não é uma ciência exata
Provedores de serviço fornecem um serviço “melhor esforço” cujo resultado
depende muito da distância até a central
altamente sensível a interferências, a qualidade da sua conexão pode ficar instável em diversas ocasiões — principalmente em dias de chuva
Para aplicações com tráfego simétrico (mesma taxa de upload e download, como VoIP e videoconferência)
Deve-se considerar a vazão oferecida pelo upload
DSL
Susceptíveis a interferências
Provocam perdas em rajadas
Ruim para multimídia