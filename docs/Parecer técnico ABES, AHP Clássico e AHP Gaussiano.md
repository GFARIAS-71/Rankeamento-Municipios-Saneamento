# Parecer técnico: ABES, AHP Clássico e AHP Gaussiano

Nov 8, 2026 · @Guilherme de Farias

## Objetivo e escopo

Os três métodos produzem rankings fortemente concordantes no conjunto dos municípios, mas divergem no topo, e a escolha entre eles é sobretudo uma escolha de quais dimensões do saneamento devem pesar mais.

Este parecer compara três rankings, construídos com três formas de pesar os critérios e duas de ranquear, para os **505 municípios do Nordeste habilitados** no Ranking ABES 2026, isto é, excluídos os "Não habilitados". Os cinco indicadores usados são:

- **Água**: IAG0001
- **Esgoto**: IES0001
- **Tratamento**: IES2003
- **Coleta**: IRS0001
- **Destinação**: IRS3002

Todos os números vêm das planilhas *AHP\_Classico.ods* e *AHP\_Gaussiano.ods*.

## Os métodos: três formas de pesar e duas de ranquear

Os métodos se distinguem em duas etapas: como se definem os pesos dos cinco indicadores e como esses pesos se combinam com o desempenho de cada município. Ao todo, há três formas de pesar e duas de ranquear.

### Formas de pesar os critérios

| Método | Como os pesos são obtidos | Natureza do peso |
| --- | --- | --- |
| ABES | Nenhum cálculo: os cinco indicadores entram com o mesmo peso | Nominal e igual: 20% para cada indicador |
| AHP Clássico | Comparação par a par dos critérios na escala de Saaty, com pesos pela média geométrica das linhas da matriz (RC = 0,0152, consistente) | Subjetiva: expressa o julgamento de importância do decisor |
| AHP Gaussiano | Coeficiente de variação de cada indicador (desvio-padrão ÷ média), normalizado para somar 1 | Objetiva: expressa quanto os municípios diferem entre si em cada indicador |

Os valores de cada peso estão no gráfico da seção seguinte.

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

Por isso, para comparar os três métodos na mesma base, este parecer usa o **peso equivalente da ABES na escala normalizada**: Coleta 31,3%, Água 26,7%, Destinação 18,7%, Esgoto 13,7% e Tratamento 9,5%. Aplicar 20% a cada valor normalizado não reproduziria a ABES (ρ = 0,95 com ela, e 33 posições de deslocamento médio).

## Pesos resultantes

O Clássico e o Gaussiano privilegiam dimensões opostas. O Clássico concentra 68% do peso em Água e Coleta, enquanto o Gaussiano põe 64% em Tratamento e Destinação. A ABES, com 20% nominais para cada indicador, equivale na escala normalizada a uma posição intermediária, mais perto do Clássico.

&#91;embedded content: AHP\_Classico.ods e AHP\_Gaussiano.ods · 505 municípios habilitados\]

A inversão no Gaussiano é esperada. Coleta e Água são quase universais entre os habilitados (médias de 81,6 e 69,6), então variam pouco e recebem peso baixo. Tratamento e Destinação têm muitos zeros e muitos 100, variam muito e por isso dominam.

## Concordância entre os rankings

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

Um cuidado vale para os três: os indicadores Tratamento e Destinação têm muitos zeros. Parte desses zeros pode refletir ausência de informação, e não ausência de serviço. Isso afeta sobretudo o Gaussiano, que dá a esses dois indicadores 64% do peso.

## Síntese das diferenças

Este parecer não elege um método. Ele registra em que os três diferem, para servir de base à comparação com as demais formas de ranqueamento do trabalho.

- **O que define o peso.** Na ABES, nenhuma decisão: os pesos são iguais nas notas brutas. No AHP Clássico, o julgamento declarado de importância. No AHP Gaussiano, a dispersão dos dados.
- **Onde o peso se concentra.** Na escala normalizada, a ABES e o Clássico concentram o peso em Água e Coleta (58% e 68%). O Gaussiano o concentra em Tratamento e Destinação (64%).
- **Como a pontuação é formada.** A ABES usa a soma simples das notas brutas, e os dois AHP usam a soma ponderada dos valores normalizados. As duas formas são aditivas e compensatórias.
- **Concordância com a ABES.** Os dois AHP têm correlação forte com ela (ρ de 0,87 a 0,89). No topo, porém, o Clássico mantém 9 dos 10 primeiros, e o Gaussiano, 5.
- **Concordância entre os AHP.** A correlação entre os dois (ρ = 0,76) é menor que a de qualquer deles com a ABES, porque cada um se afasta dela numa direção.
- **Núcleo estável.** Salvador, Vitória da Conquista, União dos Palmares, Jequié e Porto Seguro estão no Top 10 dos três métodos.

Uma verificação fortaleceria essa comparação, que seria testar como o ranking Clássico muda com pequenas variações nos julgamentos da matriz de Saaty.
