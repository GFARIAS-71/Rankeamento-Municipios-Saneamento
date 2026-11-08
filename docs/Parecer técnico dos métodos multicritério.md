# Parecer técnico: métodos multicritério do ranking de saneamento

Nov 8, 2026 · @Guilherme de Farias

## Objetivo e escopo

Este parecer reúne, à medida que forem calculados, todos os métodos do trabalho, separados em métodos de pesos e métodos de agregação. Até aqui ele cobre a ABES, os dois AHP e o CRITIC. Os três primeiros produzem rankings fortemente concordantes no conjunto dos municípios, mas divergem no topo. O CRITIC, que só calcula pesos, concentra 36,6% do peso em Destinação, mais que qualquer outro esquema.

| Método | Papel | Situação neste parecer | Planilha |
| --- | --- | --- | --- |
| ABES | Pesos iguais + soma simples das notas brutas | Incluído (pesos e ranking) | *relatorio ABES 2026 NE.ods* |
| AHP Clássico | Pesos (Saaty) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Classico.ods* |
| AHP Gaussiano | Pesos (coeficiente de variação) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Gaussiano.ods* |
| CRITIC | Só pesos (dispersão + conflito) | Incluído (pesos) | *CRITIC.ods* |
| Pesos iguais na escala normalizada | Só pesos | A incluir | — |
| TOPSIS | Só agregação | A incluir | — |
| VIKOR | Só agregação | A incluir | — |
| PROMETHEE II | Só agregação | A incluir | — |

A análise usa os **505 municípios do Nordeste habilitados** no Ranking ABES 2026, isto é, excluídos os "Não habilitados". Os cinco indicadores usados são:

- **Água**: IAG0001
- **Esgoto**: IES0001
- **Tratamento**: IES2003
- **Coleta**: IRS0001
- **Destinação**: IRS3002

Todos os números vêm das planilhas da pasta `planilhas/` indicadas na tabela acima.

## Os métodos: formas de pesar e formas de ranquear

Os métodos se distinguem em duas etapas: como se definem os pesos dos cinco indicadores e como esses pesos se combinam com o desempenho de cada município. Alguns métodos cobrem só a primeira etapa (CRITIC), outros só a segunda (TOPSIS, VIKOR, PROMETHEE II), e a ABES e os AHP, como aplicados aqui, cobrem as duas. Até aqui, há quatro formas de pesar e duas de ranquear.

### Formas de pesar os critérios

| Método | Como os pesos são obtidos | Natureza do peso |
| --- | --- | --- |
| ABES | Nenhum cálculo: os cinco indicadores entram com o mesmo peso | Nominal e igual: 20% para cada indicador |
| AHP Clássico | Comparação par a par dos critérios na escala de Saaty, com pesos pela média geométrica das linhas da matriz (RC = 0,0152, consistente) | Subjetiva: expressa o julgamento de importância do decisor |
| AHP Gaussiano | Coeficiente de variação de cada indicador (desvio-padrão ÷ média), normalizado para somar 1 | Objetiva: expressa quanto os municípios diferem entre si em cada indicador |
| CRITIC | Desvio-padrão de cada indicador normalizado por min-max, multiplicado pelo conflito com os demais (Σ de 1 − correlação), normalizado para somar 1 | Objetiva: expressa quanto o indicador varia e quanto traz de informação que os outros não trazem |

Os valores de cada peso estão na seção "Pesos resultantes". O CRITIC não tem forma de ranquear própria: seus pesos serão aplicados pelos métodos de agregação quando estes entrarem no parecer.

### CRITIC

O CRITIC (Diakoulaki, Mavrotas e Papayannakis, 1995) define o peso de um indicador pela quantidade de informação que ele carrega. Essa informação tem duas partes: quanto o indicador varia entre os municípios (desvio-padrão) e quanto ele discorda dos demais (conflito). Um indicador muito correlacionado com outro conta em dobro a mesma informação e, por isso, perde peso.

```math
r_{ij} = \frac{x_{ij} - \min_i x_{ij}}{\max_i x_{ij} - \min_i x_{ij}} \qquad C_j = \sigma_j \sum_{k=1}^{5} (1 - \rho_{jk}) \qquad w_j = \frac{C_j}{\sum_{k} C_k}
```

Na fórmula, rᵢⱼ é o valor normalizado por min-max (o pior município do indicador fica com 0 e o melhor com 1), σⱼ é o desvio-padrão de rᵢⱼ, ρⱼₖ é a correlação de Pearson entre os indicadores j e k, e Cⱼ é a informação do indicador.

| Indicador | Desvio-padrão (min-max) | Conflito Σ(1 − ρ) | Informação C | Peso CRITIC |
| --- | --- | --- | --- | --- |
| Água | 0,202 | 3,468 | 0,699 | 13,4% |
| Esgoto | 0,249 | 3,255 | 0,812 | 15,5% |
| Tratamento | 0,296 | 3,461 | 1,023 | 19,6% |
| Coleta | 0,232 | 3,361 | 0,781 | 14,9% |
| Destinação | 0,494 | 3,881 | 1,915 | 36,6% |

As correlações entre os indicadores são baixas: a maior é 0,33 (Água × Coleta), seguida de 0,32 (Esgoto × Tratamento). Nenhum par passa do limite de 0,8 que exigiria justificar ou excluir um critério. Por isso o conflito varia pouco (3,26 a 3,88), e quem decide o peso é sobretudo o desvio-padrão. Destinação lidera nas duas partes. É o indicador mais disperso, porque quase todos os municípios têm 0 ou 100, e o menos correlacionado com os outros (correlação negativa com Água e com Tratamento).

**Por que min-max.** A normalização muda o desvio-padrão, mas não a correlação. Com a normalização pela soma, usada nos AHP, o desvio-padrão de cada indicador vira o coeficiente de variação dividido por 505, e o CRITIC daria praticamente os pesos do Gaussiano (8,3%, 18,8%, 34,1%, 6,4% e 32,4%). O min-max é a normalização do artigo original e mantém o CRITIC como um esquema distinto. A mesma normalização será usada quando os pesos CRITIC forem aplicados na agregação.

### Formas de ranquear os municípios

| Forma | Métodos que a usam | Dados de entrada | Como a pontuação é formada |
| --- | --- | --- | --- |
| Soma simples | ABES | Notas brutas dos indicadores (0 a 100) | Soma das cinco notas; como os pesos são iguais, eles são redundantes e podem ser omitidos |
| Soma ponderada normalizada | AHP Clássico e AHP Gaussiano | Valores normalizados pela soma (cada indicador soma 1 nos 505 municípios) | Soma dos valores normalizados, cada um multiplicado pelo peso do seu critério |

```math
\text{ABES: } P_i = \sum_{j=1}^{5} x_{ij} \qquad\qquad \text{AHP: } P_i = \sum_{j=1}^{5} w_j \, r_{ij}, \quad r_{ij} = \frac{x_{ij}}{S_j}
```

Na fórmula, xᵢⱼ é a nota do município i no indicador j, Sⱼ é a soma desse indicador nos 505 municípios e wⱼ é o peso do AHP. Os dois AHP compartilham a mesma forma de ranquear e diferem apenas nos pesos.

As duas formas são aditivas e compensatórias: uma nota alta num indicador compensa uma nota baixa em outro. A diferença está na normalização, que divide cada indicador por uma constante própria. Por isso, os pesos iguais da ABES nas notas brutas equivalem, na escala normalizada, a pesos proporcionais à soma de cada indicador:

```math
\sum_j x_{ij} = \sum_j S_j \, r_{ij}, \qquad r_{ij} = \frac{x_{ij}}{S_j}
```

Por isso, para comparar os métodos na mesma base, este parecer usa o **peso equivalente da ABES na escala normalizada**: Coleta 31,3%, Água 26,7%, Destinação 18,7%, Esgoto 13,7% e Tratamento 9,5%. Aplicar 20% a cada valor normalizado não reproduziria a ABES (ρ = 0,95 com ela, e 33 posições de deslocamento médio).

## Pesos resultantes

O Clássico e o Gaussiano privilegiam dimensões opostas. O Clássico concentra 68% do peso em Água e Coleta, enquanto o Gaussiano põe 64% em Tratamento e Destinação. A ABES, com 20% nominais para cada indicador, equivale na escala normalizada a uma posição intermediária, mais perto do Clássico.

| Indicador | ABES (equivalente) | AHP Clássico | AHP Gaussiano | CRITIC (min-max) | CRITIC (equivalente pela soma) |
| --- | --- | --- | --- | --- | --- |
| Água | 26,7% | 41,7% | 8,5% | 13,4% | 17,7% |
| Esgoto | 13,7% | 16,0% | 20,4% | 15,5% | 10,6% |
| Tratamento | 9,5% | 9,7% | 34,9% | 19,6% | 9,2% |
| Coleta | 31,3% | 26,3% | 6,8% | 14,9% | 28,5% |
| Destinação | 18,7% | 6,2% | 29,5% | 36,6% | 34,0% |

O gráfico ainda não inclui o CRITIC. A tabela traz os pesos CRITIC na escala min-max, em que são aplicados, e convertidos para a escala pela soma, para comparação direta com as outras colunas. A conversão divide cada peso pela amplitude do indicador, multiplica pela soma dele nos 505 municípios e normaliza o resultado.

A inversão no Gaussiano é esperada. Coleta e Água são quase universais entre os habilitados (médias de 81,6 e 69,6), então variam pouco e recebem peso baixo. Tratamento e Destinação têm muitos zeros e muitos 100, variam muito e por isso dominam.

O CRITIC fica entre os dois extremos na escala min-max, com Destinação muito à frente (36,6%) e os outros quatro entre 13% e 20%. Na escala pela soma, ele se parece com a ABES em Esgoto, Tratamento e Coleta e difere dela num ponto: tira peso de Água (de 26,7% para 17,7%) e o passa para Destinação (de 18,7% para 34,0%). Destinação é o único indicador que o Gaussiano e o CRITIC colocam no topo, por razões parecidas: é quase binário e não acompanha os demais.

## Concordância entre os rankings

Esta seção e a seguinte comparam só os métodos que já produzem ranking (ABES e os dois AHP). Os pesos CRITIC entram aqui quando forem combinados com os métodos de agregação.

Os dois AHP são fortemente correlacionados com a ABES (ρ ≈ 0,87 a 0,89), mas apenas moderadamente correlacionados entre si (ρ = 0,76). Ou seja, cada um se afasta da ABES numa direção diferente.

| Par comparado | Spearman (ρ) | Kendall (τ-b) | Deslocamento médio (posições) |
| --- | --- | --- | --- |
| ABES × AHP Clássico | 0,869 | 0,713 | 61,8 |
| ABES × AHP Gaussiano | 0,888 | 0,711 | 52,6 |
| AHP Clássico × AHP Gaussiano | 0,765 | 0,580 | 76,1 |

Todas as correlações são positivas e significativas (p < 10⁻¹⁰⁰, n = 505). Nas duas comparações com a ABES, cerca de 86% dos pares de municípios mantêm a mesma ordem relativa. Entre os dois AHP, essa proporção cai para 79%.

Os maiores deslocamentos individuais mostram o efeito dos pesos:

- **Mutuípe (BA)** é o 384º na ABES, sobe para 321º no Clássico e para 106º no Gaussiano. O município tem Tratamento de 75,5, numa base em que a maioria tem zero.
- **Viçosa (RN)** é o 41º na ABES e salta para 6º no Clássico, graças a Água, Esgoto e Coleta acima de 90. Sem Destinação (zero), fica em 28º no Gaussiano.
- **Poço Dantas (PB)** cai de 302º para 482º no Clássico, porque tem Água de apenas 10,6, o indicador de maior peso nesse método.

## Top 10

Cinco municípios estão no Top 10 dos três métodos: Salvador, Vitória da Conquista, União dos Palmares, Jequié e Porto Seguro. Fora esse núcleo, o Clássico preserva o Top 10 da ABES (9 de 10 em comum), enquanto o Gaussiano o renova pela metade (5 de 10).

| Posição | ABES | AHP Clássico | AHP Gaussiano |
| --- | --- | --- | --- |
| 1 | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** |
| 2 | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | **União dos Palmares (AL)** |
| 3 | **União dos Palmares (AL)** | **União dos Palmares (AL)** | Frei Martinho (PB) |
| 4 | **Jequié (BA)** | **Jequié (BA)** | **Porto Seguro (BA)** |
| 5 | **Porto Seguro (BA)** | Aracaju (SE) | **Jequié (BA)** |
| 6 | Campina Grande (PB) | Viçosa (RN) | Teotônio Vilela (AL) |
| 7 | Aracaju (SE) | Barra dos Coqueiros (SE) | **Vitória da Conquista (BA)** |
| 8 | Barra dos Coqueiros (SE) | Luís Eduardo Magalhães (BA) | São José do Sabugi (PB) |
| 9 | Luís Eduardo Magalhães (BA) | Campina Grande (PB) | Prata (PB) |
| 10 | Madre de Deus (BA) | **Porto Seguro (BA)** | Santa Luzia (PB) |

Em negrito, os municípios presentes nos três Top 10.

No Gaussiano, todos os cinco que entram têm Tratamento entre 88 e 100 e Destinação 100. Quatro deles são municípios pequenos da Paraíba, alguns com Água de apenas 51 a 56. Os cinco que saem também têm Destinação 100, mas Tratamento entre 67 e 79. Como o Tratamento é o indicador de maior peso no Gaussiano, essa diferença basta para tirá-los do Top 10, mesmo tendo Água e Coleta próximas de 100.

## Pontos fortes e limitações

Nenhum método é neutro. Cada um embute uma resposta diferente à pergunta sobre o que mais importa no saneamento.

| Método | Pontos fortes | Limitações |
| --- | --- | --- |
| ABES | Simples, transparente e oficial, com comparação direta entre edições do ranking | Os 20% nominais não geram influência igual: como as notas de Coleta e Água são mais altas, na escala normalizada elas equivalem a 31% e 27%, contra 9,5% de Tratamento |
| AHP Clássico | Pesos explícitos e justificáveis, com consistência verificada (RC = 0,015); permite discutir prioridades de política pública | Depende do julgamento de quem preenche a matriz; outro decisor pode chegar a pesos e rankings diferentes |
| AHP Gaussiano | Objetivo e reprodutível, sem julgamento humano; destaca os indicadores que de fato separam os municípios | Peso alto significa "varia muito", não "é importante"; Coleta, quase universalizada, recebe só 6,8%. Os pesos também mudam conforme a amostra de municípios |
| CRITIC | Objetivo e reprodutível; além da dispersão, desconta a informação repetida entre indicadores correlacionados | Só calcula pesos, e o ranking depende do método de agregação escolhido depois. Os pesos dependem da normalização (min-max aqui) e da amostra. Com correlações baixas como as daqui, o conflito pesa pouco, e Destinação, quase binário, recebe 36,6% |

Um cuidado vale para todos os métodos: os indicadores Tratamento e Destinação têm muitos zeros. Parte desses zeros pode refletir ausência de informação, e não ausência de serviço. Isso afeta sobretudo o Gaussiano e o CRITIC, que dão a esses dois indicadores 64% e 56% do peso.

## Síntese das diferenças

Este parecer não elege um método. Ele registra em que os métodos diferem, para servir de base à comparação com as demais formas de ranqueamento do trabalho.

- **O que define o peso.** Na ABES, nenhuma decisão: os pesos são iguais nas notas brutas. No AHP Clássico, o julgamento declarado de importância. No AHP Gaussiano, a dispersão dos dados. No CRITIC, a dispersão e o conflito entre os indicadores.
- **Onde o peso se concentra.** Na escala normalizada, a ABES e o Clássico concentram o peso em Água e Coleta (58% e 68%). O Gaussiano o concentra em Tratamento e Destinação (64%). O CRITIC dá o maior peso a Destinação (36,6% em min-max, 34,0% na escala pela soma).
- **Como a pontuação é formada.** A ABES usa a soma simples das notas brutas, e os dois AHP usam a soma ponderada dos valores normalizados. As duas formas são aditivas e compensatórias.
- **Concordância com a ABES.** Os dois AHP têm correlação forte com ela (ρ de 0,87 a 0,89). No topo, porém, o Clássico mantém 9 dos 10 primeiros, e o Gaussiano, 5.
- **Concordância entre os AHP.** A correlação entre os dois (ρ = 0,76) é menor que a de qualquer deles com a ABES, porque cada um se afasta dela numa direção.
- **Núcleo estável.** Salvador, Vitória da Conquista, União dos Palmares, Jequié e Porto Seguro estão no Top 10 dos três métodos.

Uma verificação fortaleceria essa comparação, que seria testar como o ranking Clássico muda com pequenas variações nos julgamentos da matriz de Saaty.
