Capítulo 10
Emulando a conversação e Trabalho Face-a-Face
Este capítulo apresenta algumas aplicações multimídia que permitem a comunicação entre pessoas ou grupos para emulação da conversação face-a-face e o trabalho colaborativo. Estas aplicações são a videofonia, videoconferência, distribuição de áudio e vídeo, e espaço de trabalho compartilhado. Note que este capítulo considera apenas aplicações utilizando redes IP.
10.1 Videofonia
A videofonia é a inclusão de vídeo na telefonia, também chamada de vídeo telefonia. O vídeo permite aumentar a transferência de informação emocional, como expressividade, via contato olho-a-olho. Mais especificamente, videofonia é permite a comunicação interpessoal, ou seja, a comunicação de no máximo duas pessoas. A comunicação de mais de duas pessoas, cada uma com seu desktop, é chamada de conferência videofônica.
10.1.1 Requisitos de Hardware
Para a videofonia é necessário um computador com módulos de entrada e saída de áudio e vídeo, além de um acesso a rede cuja banda é suficiente para a transmissão do áudio e vídeo. No caso do áudio, os requisitos são os mesmos da VoIP (placa de som, microfone e fone de ouvido). Para o vídeo é necessária uma câmera web (com entrada paralela ou USB) ou placa de captura de vídeo e uma câmera com saída de vídeo. O uso de placa de captura de vídeo é mais interessante, pois permitem obter melhor qualidade de vídeo.
10.1.2 Requisito de qualidade de áudio e vídeo
Neste tipo de aplicação, a qualidade do áudio deve ser boa devido ao alto nível de interatividade existente em aplicações interpessoais (duas pessoas se comunicando). O objetivo do vídeo é passar a informação emocional do interlocutor, sem a necessidade de alta definição, a qualidade de imagem não necessita ser alta. A taxa de quadros é mais importante que a resolução de imagem para que haja a movimentação natural das pessoas.
10.1.3 Requisitos de Rede
Em termos de taxa de bits, o canal de vídeo requer 80 a 200 Kbits/s mais 5,3 a 64 Kbits/s para o canal de áudio. Os requisitos de atraso e variação de atraso são muito similares ao da VoIP (150ms de atraso fim-a-fim, baixa variação de atraso e taxa de perda de pacote de até 1%), sendo que para o vídeo a taxa de perdas pode ser um pouco maior.
10.1.4 Requisitos de Software
Existem diversos softphone que suportam a transmissão de vídeo, como Windows Live Messenger, Skype, X-Lite e Ekiga. Alguns deles utilizam a arquitetura H.323 ou o protocolo SIP.
10.2 Videoconferência
A videoconferência ou simplesmente videoconferência, envolve vários indivíduos ou vários grupos de indivíduos engajados em diálogo. O objetivo não é manter uma simples conversação bilateral, mas suportar reuniões. Assim, a videoconferência pode ser ponto-a-ponto como na videofonia, ou ponto-a-multiponto como na distribuição de vídeo, mas sempre implica numa comunicação bidirecional (ilustrado na Figura 1).
130 Capítulo 9 Emulando a Conversação e Trabalho Face-a-Face Prof. Roberto Willrich
Videofonia
Conferência
Videofônica
Videoconferência ponto-a-ponto
Videoconferência ponto-a-multiponto
Figura 1. Videofonia e videoconferência
Sistemas de videoconferência são essencialmente projetados para aumentar o trabalho cooperativo entre parceiros remotos, especialmente quando complementado por ferramentas de espaço de trabalho compartilhado e aplicações compartilhadas. Alguns campos de aplicação da videoconferência são: comunicação entre executivos, projeto colaborativo, engenharia conjunta, debates a distância, assistência e consulta a distância, tutoria remota na educação a distância e telemedicina.
Os primeiros sistemas de videoconferência eram baseados em difusão por satélite de televisão. A comunicação era assimétrica, com um sítio origem do vídeo e múltiplas localizações receptoras. O canal de retorno era normalmente feita via chamadas telefônicas. Desde então, os serviços de videoconferência transformaram-se em simétricos, e seu desenvolvimento resultou em duas abordagens tecnológicas:
 Videoconferência baseada em circuito: este tipo apareceu no início dos anos oitenta. Estes sistemas operam sobre redes com taxas de transferência garantidas - inicialmente conexões telefônicas e agora sobre ISDN.
 Videoconferência baseada em pacotes: este tipo apareceu no início dos anos 90, principalmente com o avanço das estações de trabalho e computadores pessoais.
A emergência de sistemas de videoconferência explorando redes a pacotes não pode ser separada do desenvolvimento da videofonia a pacotes, no início dos anos noventa. Ela resultou da exploração dos dispositivos (estações de trabalho e PC) e redes de dados (LAN) já disponível nos escritórios para suportar serviços de videoconferência. A videoconferência e a videofonia são suportadas pelos mesmos produtos, que são disponíveis na forma de kits de hardware e software para estações de trabalho e computadores pessoais.
10.2.1 Requisitos de Hardware
A videoconferência necessita de vários equipamentos de suporte. É necessária uma sala especial onde estes equipamentos são instalados. Esta sala deve ter uma iluminação especial e acústica. Nesta sala são instalados, entre outros, um módulo de controle da videoconferência e dispositivos especiais de captura de vídeo e som.
Manipulando Grupos
A videoconferência envolve ao menos um grupo de pessoas em uma das localizações. Assim é necessárias uma ou várias câmeras para registrar as cenas. As várias opções de registro de vídeo são:
 uma câmera de TV fixa: a câmera registra uma vista completa do grupo. Neste caso geralmente as pessoas se sentam em uma mesa na forma de um “V” ou na forma de um semi-círculo.
 uma câmera de TV móvel: a câmera filma apenas o interlocutor atual.
 uma câmera fixa e outra móvel: este caso é a junção dos dois anteriores, sendo que a visão é chaveada por um operador.
Manipulando Documentos
Geralmente documentos devem ser transferidos para dar suporte a videoconferência. Documentos podem ser:
131 Capítulo 9 Emulando a Conversação e Trabalho Face-a-Face Prof. Roberto Willrich
 Documentos impressos: geralmente são capturados por câmeras verticais (chamadas câmeras documento). Estas câmeras geralmente produzem um vídeo cuja resolução é mais importante que a taxa de quadros a fim de permitir a visualização do documento em alta qualidade. Outra opção para captura é utilizar scanners rápidos, permitindo uma melhor resolução.
 Documentos projetados: Reuniões podem conter projeções de slides e transparências, que também exigem uma boa resolução para poderem ser lidos (implicando na necessidade de redução do número de quadros). Este tipo de apresentação deve ser evitado.
 Documentos eletrônicos: transferência de documentos digitais (documentos Word, apresentações PowerPoint, etc.), documentos scanneados antes da seção ou gerados por computador asseguram uma melhor qualidade.
10.2.2 Requisitos de qualidade de áudio e vídeo
Exceto quando documentos estão envolvidos, os requisitos da videoconferência são similares aqueles da videofonia: é importante reduzir o salto de movimento e uma limitada resolução pode ser tolerada. Isto pois a baixa taxa de quadros altera a transmissão da informação emocional, essencial para emular a comunicação face-a-face. Quando a videoconferência envolve a apresentação de documentos, ela necessita de uma resolução de média qualidade para que o documento seja legível.
Como apresentado anteriormente, usuários são mais tolerantes a distorções quando assistem passivamente. Assim uma pequena perda da semântica é aceitável, devendo o som ter uma qualidade suficiente para ser amplificado por alto-falantes.
10.2.3 Requisitos de Rede
Os requisitos de taxa de bits da videoconferência baseada em pacotes são similares aqueles da videofonia, no caso, para cada vídeo e áudio da conferência. Uma resolução de ¼ da VCR e 30 fps requer 200 kbps, sendo que 5.3 a 64 kbps devem ser adicionados para canal de áudio. A videoconferência é sensível a atrasos, sendo que os limites são os mesmos da videofonia.
Videoconferências ponto-a-multiponto não trabalham muito bem sem multicasting a pacotes. Portanto, o uso de um suporte de rede suportando multicast é interessante para um uso mais eficiente de recursos de rede. Caso a rede não tiver suporte a multicast, que é o caso geral da Internet, a fonte deve enviar uma cópia dos dados para cada um dos participantes. Caso a rede oferece recursos multicast é enviada apenas uma cópia dos dados para todos os destinos, sendo que os roteadores multicast se encarregam de duplicar o pacote quando necessário. Neste caso, o uso de recursos da rede é otimizado. Por exemplo, na Figura 78, caso não houvesse suporte a multicast, a fonte deveria enviar 3 cópias do fluxo de vídeo e de áudio, uma por cada destino. Caso os roteadores suportassem multicast, que é o caso ilustrado na Figura 78, a fonte encaminha apenas uma cópia do fluxo de áudio e vídeo, e os roteadores são responsáveis por encaminhar estes fluxos aos diversos destinos.
10.2.4 Requisitos de Software
Existem vários fabricantes de componentes ou soluções integradas completas para videoconferência. Alguns softwares para videofonia permitem a conferência de grupo, como cloudMeeting (www.cloudmeeting.com), Ekiga, Skype, palbee, (www.palbee.com), Asterisk (www.asterisk.org) e Yate (yate.null.ro).
Estação Vconf.
Estação
Estação
R R
Estação Vconf.
Estação Vconf.
Estação Vconf.R
R
R
R
R
WAN
Replicadores de pacotes multicast
Figura 78. Videoconferência Multicast
https://lh3.googleusercontent.com/notebooklm/ANHLwAw3LVXPSJ-61-Ahccmkbexp4bPseE-lX-6X0mrUKjmeHunOuXTtLjeH4_T0-rqf4QrOsIh_4l7LPym0WX7N7TqsvXsWKtMHWVf13m1D8-jVZiukocgrJQMXloG76CB-Yb_0asB3Rw=w337-h153-v0
132 Capítulo 9 Emulando a Conversação e Trabalho Face-a-Face Prof. Roberto Willrich
10.3 Espaço de Trabalho Compartilhado
Espaço de trabalho compartilhado refere-se ao compartilhamento do monitor de vídeo do computador por todos os participantes envolvidos em uma tarefa comum e que colaboram sem deixar seus espaços de trabalho. As várias aplicações de espaço de trabalho compartilhado apresentadas aqui são dedicadas a ambientes profissionais CSCW (Computer-Supported Cooperative Work). CSCW é o campo interessado no projeto de sistemas baseados em computador para suportar e aumentar o trabalho de grupos de usuários engajados em tarefas ou objetivos comuns, e o entendimento dos efeitos de usar tais sistemas. O sistema suportando espaço compartilhado é chamado de Groupware.
A idéia de compartilhar espaço de trabalho é criar um compartilhamento a distância mediado por computador de informações efêmeras tão bem quanto compartilhar o produto real sobre a qual os indivíduos participantes estão trabalhando. Por informações efêmeras entende-se aquelas informações que dão suporte a apresentação de idéias, tipo rabiscar algo em uma folha em branco para demonstrar cálculos, ou um quadro branco para esboçar um conceito.
10.3.1 Ferramentas de Quadro Branco Compartilhado
As ferramentas de quadro branco compartilhado (Figura 79) emulam, na tela do computador, o quadro branco físico. Com esta ferramenta cada participante pode desenhar no quadro branco usando ferramentas de desenho para criar objetos geométricos e desenho a mão, ou digitar textos usando editores rudimentares. Tanto textos como objetos podem ser apagados, movidos, alterados os tamanhos, etc. Além disso, o quadro pode ser armazenado para uso posterior. Convenções simples, tipo uso de um código de cor para cada participante, podem identificar quem fez o que. Muitas ferramentas de quadro branco permitem que ao invés de se ter um fundo padrão branco, seja compartilhado uma imagem como fundo.
Figura 79. Princípios de quadro branco compartilhado
Controle de Acesso (Floor Control)
Quadro branco compartilhado emula o quadro branco físico: quando duas pessoas num escritório estão trabalhando no mesmo projeto em um quadro branco físico, regras sociais e protocolos sociais governam o acesso ao quadro, assim eles não escrevem ao mesmo tempo, nem sobrescrevem ou apagam o que o outro fez. Tais regras de comportamento são difíceis de se produzir remotamente. A definição e implementação de políticas que regulam o acesso aos objetos compartilhados é um problema importante no espaço de trabalho compartilhado. Elas são chamadas políticas de controle de acesso.
Existem quatro abordagens básicas para controle de acesso:
 Sem controle. Neste caso o sistema deixa todo mundo acessar livremente a superfície compartilhada. Este esquema trabalha razoavelmente bem com duas pessoas, mas é impraticável quando o número de participantes aumenta.
 Bloqueio implícito. Cada vez que um participante entra com uma informação, este participante implicitamente toma o controle. O acesso ao quadro é automaticamente liberado num certo tempo (poucos segundos) após que a pessoa com o controle acabar sua entrada.
 Bloqueio explícito. É similar ao anterior, exceto que o usuário deve pedir e liberar explicitamente o acesso ao quadro via um botão.
133 Capítulo 9 Emulando a Conversação e Trabalho Face-a-Face Prof. Roberto Willrich
 Controle do moderador. Um dos participantes é designado como moderador para a seção colaborativa. O moderador pode tomar o controle do quadro a qualquer instante. O moderador necessita de ferramentas para monitorar a lista de pedidos pendentes.
Requisitos de Rede
As ferramentas de quadro branco compartilhado não exigem muito da rede. A taxa de transferência necessária é pequena, exceto quando imagens de fundo necessitam ser enviadas com freqüência que em prática é uma distorção do espírito do quadro branco compartilhado. Quando imagens não são transmitidas, os serviços de quadro branco compartilhado são mais sensíveis a atrasos do que a taxa de bits. O atraso máximo de transito deve estar na faixa de meio a um segundo. Como este tipo de aplicação exige multicast, se uma rede a comutação de circuitos tal como ISDN for utilizada, múltiplas conexões devem ser realizadas entre os participantes.
Usando quadro branco compartilhado com outras ferramentas de conversação
Quando se usa quadro branco compartilhado, os participantes necessitam de canais diretos de comunicação. Isto ajuda a criar uma presença social útil no controle do quadro branco. Mas mais importante este canal direto de comunicação é necessário em muitos casos para complementar o trabalho cooperativo feito com o quadro branco. Estes canais podem transportar chamadas telefônicas ordinárias, troca de mensagens textuais, telefonia assistida por computador, ou videofonia.
Requisitos de Sotware
Existem muitas implementações de quadro branco compartilhado. Algumas são componentes de ferramentas completas, incluindo suporte a áudio e vídeo. Outras implementações são stand-alone. Exemplos de implementações stand-alone incluem WSCRAWL e wb (domínio público), e VENUE (DEC). Alguns produtos com ferramentas de áudio e vídeo, como diversas ferramentas H.323. As mais conhecidas são o Microsoft NetMeeting e Ekiga (que implementa também o protocolo SIP).
10.3.2 Ferramentas de compartilhamento de aplicações
As ferramentas de compartilhamento de aplicações, também chamadas de agentes de gestão de colaboração, permitem que múltiplos participantes compartilhem a apresentação e o controle de qualquer aplicação interativa ordinária. Por exemplo, um editor de texto ou gráfico. Se a aplicação é um editor de texto, qualquer participante pode rolar o texto apresentado ou entrar caracteres. Isto é chamado de edição colaborativa. Há duas idéias importantes nesta definição: a aplicação que é compartilhada não necessita ser projetada para suportar múltiplos usuários simultâneos e a ferramenta de compartilhamento torna possível o modo multiusuário; além do compartilhamento da apresentação, há o seu controle.
Existem várias aplicações para este tipo de ferramenta, entre elas nós temos: revisão simultânea por muitos colaboradores, controle compartilhado de planilhas eletrônicas, desenvolvimento colaborativo de software ou assistência remota de software.
Problemas envolvidos
As ferramentas de aplicação compartilhadas, são softwares que implementam o algoritmo necessário ao controle de acesso e o ordenamento de acesso aos recursos compartilhados, além disso protegendo recursos privados. Em geral, o controle de acesso do tipo bloqueio implícito é o mais utilizado.
Outra função necessária é a gestão de entrada e saída de participantes. Alguns sistemas permitem que usuários se juntem no início de uma sessão, sem controle adicional ou após a admissão por parte de um responsável. O sistema pode informar a todos a lista de participantes.
Requisitos de Rede
Os requisitos de rede são um pouco mais severos que as ferramentas de quadro branco compartilhado. O nível de interação é maior e o serviço resultante é mais sensível a atrasos de transito na rede: o controle de acesso pode se tornar impraticável em redes que geram grandes atrasos. Muitas implementações atuais operam sobre o IP.
134 Capítulo 9 Emulando a Conversação e Trabalho Face-a-Face Prof. Roberto Willrich
Requisitos de Software
Existem várias ferramentas de aplicação compartilhadas de domínio público e alguns produtos comerciais. Elas são geralmente baseadas no X-Windows e rodam sobre o IP.
Shared X é um produto comercial da Hewlett-Packard que usa um algoritmo de controle de acesso do tipo bloqueio implícito. Nele, apenas o iniciador necessita explicitamente lançar a aplicação, os outros participantes são requisitados a se juntarem. O iniciador pode incluir novas aplicações.
XTV (X Teleconferencing Viewing) é uma implementação de domínio público onde o controle de acesso baseado em mediador. Todos devem lançar explicitamente a ferramenta XTV. Ela permite o compartilhamento de várias aplicações simultaneamente, sendo que o chairperson é quem pode incluir novas aplicações.
O Microsoft NetMeeting também permite o compartilhamento de qualquer aplicação Windows.