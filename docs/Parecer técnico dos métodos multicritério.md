# Parecer técnico: métodos multicritério do ranking de saneamento

Nov 8, 2026 · @Guilherme de Farias

## Objetivo e escopo

Este parecer reúne, à medida que forem calculados, todos os métodos do trabalho, separados em métodos de pesos e métodos de agregação. Até aqui ele cobre a ABES, os dois AHP, o CRITIC e o PROMETHEE II. Os três primeiros produzem rankings fortemente concordantes no conjunto dos municípios, mas divergem no topo. O CRITIC, que só calcula pesos, concentra 36,6% do peso em Destinação, mais que qualquer outro esquema. O PROMETHEE II, que só ranqueia, foi aplicado aos quatro esquemas de pesos. Com pesos iguais, CRITIC e AHP Gaussiano ele fica muito perto da ABES (ρ de 0,95 a 0,99). Com os pesos do AHP clássico, ele se afasta dela mais que qualquer outro ranking calculado até aqui (ρ = 0,71).

| Método | Papel | Situação neste parecer | Planilha |
| --- | --- | --- | --- |
| ABES | Pesos iguais + soma simples das notas brutas | Incluído (pesos e ranking) | *relatorio ABES 2026 NE.ods* |
| AHP Clássico | Pesos (Saaty) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Classico.ods* |
| AHP Gaussiano | Pesos (coeficiente de variação) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Gaussiano.ods* |
| CRITIC | Só pesos (dispersão + conflito) | Incluído (pesos) | *CRITIC.ods* |
| Pesos iguais na escala normalizada | Só pesos | A incluir | — |
| TOPSIS | Só agregação | A incluir | — |
| VIKOR | Só agregação | A incluir | — |
| PROMETHEE II | Só agregação (comparação par a par, compensação limitada) | Incluído (ranking nos quatro esquemas de pesos) | *PROMETHEE II.ods* |

A análise usa os **505 municípios do Nordeste habilitados** no Ranking ABES 2026, isto é, excluídos os "Não habilitados". Os cinco indicadores usados são:

- **Água**: IAG0001
- **Esgoto**: IES0001
- **Tratamento**: IES2003
- **Coleta**: IRS0001
- **Destinação**: IRS3002

Todos os números vêm das planilhas da pasta `planilhas/` indicadas na tabela acima.

## Os métodos: formas de pesar e formas de ranquear

Os métodos se distinguem em duas etapas: como se definem os pesos dos cinco indicadores e como esses pesos se combinam com o desempenho de cada município. Alguns métodos cobrem só a primeira etapa (CRITIC), outros só a segunda (TOPSIS, VIKOR, PROMETHEE II), e a ABES e os AHP, como aplicados aqui, cobrem as duas. Até aqui, há quatro formas de pesar e três de ranquear.

### Formas de pesar os critérios

| Método | Como os pesos são obtidos | Natureza do peso |
| --- | --- | --- |
| ABES | Nenhum cálculo: os cinco indicadores entram com o mesmo peso | Nominal e igual: 20% para cada indicador |
| AHP Clássico | Comparação par a par dos critérios na escala de Saaty, com pesos pela média geométrica das linhas da matriz (RC = 0,0152, consistente) | Subjetiva: expressa o julgamento de importância do decisor |
| AHP Gaussiano | Coeficiente de variação de cada indicador (desvio-padrão ÷ média), normalizado para somar 1 | Objetiva: expressa quanto os municípios diferem entre si em cada indicador |
| CRITIC | Desvio-padrão de cada indicador normalizado por min-max, multiplicado pelo conflito com os demais (Σ de 1 − correlação), normalizado para somar 1 | Objetiva: expressa quanto o indicador varia e quanto traz de informação que os outros não trazem |

Os valores de cada peso estão na seção "Pesos resultantes". O CRITIC não tem forma de ranquear própria: seus pesos são aplicados pelos métodos de agregação. Até aqui, isso foi feito no PROMETHEE II.

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

**Por que min-max.** A normalização muda o desvio-padrão, mas não a correlação. Com a normalização pela soma, usada nos AHP, o desvio-padrão de cada indicador vira o coeficiente de variação dividido por 505, e o CRITIC daria praticamente os pesos do Gaussiano (8,3%, 18,8%, 34,1%, 6,4% e 32,4%; coluna O da aba PESOS CRITIC, só para comparação). O min-max é a normalização do artigo original e mantém o CRITIC como um esquema distinto. A mesma normalização será usada quando os pesos CRITIC forem aplicados na agregação.

### Formas de ranquear os municípios

| Forma | Métodos que a usam | Dados de entrada | Como a pontuação é formada |
| --- | --- | --- | --- |
| Soma simples | ABES | Notas brutas dos indicadores (0 a 100) | Soma das cinco notas; como os pesos são iguais, eles são redundantes e podem ser omitidos |
| Soma ponderada normalizada | AHP Clássico e AHP Gaussiano | Valores normalizados pela soma (cada indicador soma 1 nos 505 municípios) | Soma dos valores normalizados, cada um multiplicado pelo peso do seu critério |
| Fluxo líquido de sobreclassificação | PROMETHEE II, com qualquer dos quatro esquemas de pesos | Notas brutas (0 a 100), sem normalização | Cada município é comparado com os outros 504, critério a critério; a pontuação é o saldo entre quanto ele supera os demais e quanto é superado |

```math
\text{ABES: } P_i = \sum_{j=1}^{5} x_{ij} \qquad\qquad \text{AHP: } P_i = \sum_{j=1}^{5} w_j \, r_{ij}, \quad r_{ij} = \frac{x_{ij}}{S_j}
```

Na fórmula, xᵢⱼ é a nota do município i no indicador j, Sⱼ é a soma desse indicador nos 505 municípios e wⱼ é o peso do AHP. Os dois AHP compartilham a mesma forma de ranquear e diferem apenas nos pesos.

As duas formas são aditivas e compensatórias: uma nota alta num indicador compensa uma nota baixa em outro. A diferença está na normalização, que divide cada indicador por uma constante própria. Por isso, os pesos iguais da ABES nas notas brutas equivalem, na escala normalizada, a pesos proporcionais à soma de cada indicador:

```math
\sum_j x_{ij} = \sum_j S_j \, r_{ij}, \qquad r_{ij} = \frac{x_{ij}}{S_j}
```

Por isso, para comparar os métodos na mesma base, este parecer usa o **peso equivalente da ABES na escala normalizada**: Coleta 31,3%, Água 26,7%, Destinação 18,7%, Esgoto 13,7% e Tratamento 9,5%. Aplicar 20% a cada valor normalizado não reproduziria a ABES (ρ = 0,95 com ela, e 33 posições de deslocamento médio).

### PROMETHEE II

O PROMETHEE II (Brans e Vincke, 1985; Brans e Mareschal, 2005) é um método de sobreclassificação (*outranking*). Ele não soma notas: compara os municípios dois a dois e conta quanto cada um supera os demais. Por isso é só um método de agregação. Os pesos vêm dos quatro esquemas (iguais, CRITIC, AHP Gaussiano e AHP clássico), o que dá quatro rankings PROMETHEE II.

As contas seguem seis etapas. Como os cinco indicadores já estão em % (0 a 100) e são todos a maximizar, o método trabalha direto com as notas brutas, sem normalização.

1. **Diferença em cada critério:** dⱼ(a,b) = fⱼ(a) − fⱼ(b), a vantagem de a sobre b no indicador j.
2. **Função de preferência:** Pⱼ(a,b) = Fⱼ[dⱼ(a,b)], entre 0 e 1. Diferenças pequenas (até o limiar de indiferença q) valem 0, e diferenças grandes (acima do limiar de preferência p) valem 1.
3. **Índice de preferência:** π(a,b) = Σⱼ wⱼ·Pⱼ(a,b), entre 0 e 1. Mede com que intensidade a é preferido a b em todos os critérios.
4. **Fluxos de saída e de entrada:** φ⁺(a) = Σₓ π(a,x)/(m − 1) mede a força de a, e φ⁻(a) = Σₓ π(x,a)/(m − 1) mede a sua fraqueza, com m = 505.
5. **Fluxo líquido:** φ(a) = φ⁺(a) − φ⁻(a), entre −1 e 1, com Σφ = 0.
6. **Ranking:** a fica à frente de b se φ(a) > φ(b). O resultado é uma ordem completa, sem incomparabilidades.

```math
P_j(d) = \begin{cases} 0 & d \le q_j \\ \dfrac{d - q_j}{p_j - q_j} & q_j < d \le p_j \\ 1 & d > p_j \end{cases} \qquad \varphi(a) = \frac{1}{m-1} \sum_{x \ne a} \left[ \pi(a,x) - \pi(x,a) \right]
```

**Funções e limiares.** Nos quatro primeiros indicadores, a função é a linear (em V com indiferença), com os limiares dados pela regra registrada no guia de escrita: q é o 1º quartil e p o 3º quartil das diferenças absolutas entre todos os pares de municípios. Em Destinação, quase binário (248 municípios com 0 e 236 com 100), a regra dos quartis daria q = 0 e p = 100. Por isso a função é a em U, com q = p = 5: diferenças de até 5 pontos são empate (98 contra 100, ou 0,2 contra 0), e qualquer diferença maior vira preferência total. Assim, os poucos municípios com valores como 96,8 ou 98,3 ficam junto dos que têm 100, em vez de perderem para eles por inteiro, como aconteceria com a função usual.

| Indicador | Função | q (pontos percentuais) | p (pontos percentuais) |
| --- | --- | --- | --- |
| Água | Linear | 8,94 | 32,90 |
| Esgoto | Linear | 11,06 | 41,65 |
| Tratamento | Linear | 7,24 | 50,10 |
| Coleta | Linear | 6,40 | 31,39 |
| Destinação | Em U | 5 | 5 |

Por exemplo, Salvador tem Tratamento 100 e Aracaju, 73,6. A diferença de 26,4 pontos fica entre q e p e vale P = (26,4 − 7,24)/(50,10 − 7,24) = 0,45. Nos demais indicadores, nenhuma das duas cidades supera a outra além do limiar de indiferença. Com pesos iguais, π(Salvador, Aracaju) = 0,2 × 0,45 = 0,089 e π(Aracaju, Salvador) = 0.

**Compensação limitada.** Uma vantagem, por maior que seja, nunca passa de P = 1, nem conta mais que o peso do seu critério. Na soma ponderada, ao contrário, um zero em Tratamento pesa tanto quanto a distância até a nota do outro município. Com pesos iguais, um município que perde para outro por 100 pontos em Esgoto e em Tratamento soma no máximo 0,4 em π contra si, o mesmo que perderia com uma diferença de 60 pontos em cada um.

**Como a planilha calcula.** A matriz π completa teria 255 mil células por esquema de pesos. Como π é uma soma ponderada das preferências por critério, os fluxos também são: φ⁺(a) = Σⱼ wⱼ·φ⁺ⱼ(a), em que φ⁺ⱼ(a) é a média de Pⱼ(a,x) sobre os outros 504 municípios. A planilha calcula esses fluxos por critério uma vez (aba FLUXOS POR CRITÉRIO) e os combina com os quatro esquemas de pesos (aba FLUXOS GLOBAIS). O resultado é idêntico ao da matriz completa, o que foi conferido com um cálculo independente em Python, com diferença máxima de 10⁻¹⁵ em φ. A aba EXEMPLO PAR A PAR mostra as etapas 1 a 3 para dois municípios escolhidos numa lista.

**Os pesos no PROMETHEE II.** O peso multiplica graus de preferência (de 0 a 1), que não dependem da escala do indicador. Por isso, aqui "pesos iguais" são 20% de fato, e não os pesos equivalentes da ABES. Os pesos CRITIC entram na versão min-max, a mesma em que foram calculados.

## Pesos resultantes

O Clássico e o Gaussiano privilegiam dimensões opostas. O Clássico concentra 68% do peso em Água e Coleta, enquanto o Gaussiano põe 64% em Tratamento e Destinação. A ABES, com 20% nominais para cada indicador, equivale na escala normalizada a uma posição intermediária, mais perto do Clássico.

| Indicador | ABES (equivalente) | AHP Clássico | AHP Gaussiano | CRITIC (min-max) | CRITIC (equivalente pela soma) |
| --- | --- | --- | --- | --- | --- |
| Água | 26,7% | 41,7% | 8,5% | 13,4% | 17,7% |
| Esgoto | 13,7% | 16,0% | 20,4% | 15,5% | 10,6% |
| Tratamento | 9,5% | 9,7% | 34,9% | 19,6% | 9,2% |
| Coleta | 31,3% | 26,3% | 6,8% | 14,9% | 28,5% |
| Destinação | 18,7% | 6,2% | 29,5% | 36,6% | 34,0% |

A coluna "CRITIC (equivalente pela soma)" não é um CRITIC calculado com outra normalização. São os mesmos pesos min-max, que dão a mesma pontuação, reescritos na escala dos AHP para comparação direta com as outras colunas. A conversão divide cada peso pela amplitude do indicador, multiplica pela soma dele nos 505 municípios e normaliza o resultado. Ela está na coluna N da aba PESOS CRITIC do *CRITIC.ods*.

A inversão no Gaussiano é esperada. Coleta e Água são quase universais entre os habilitados (médias de 81,6 e 69,6), então variam pouco e recebem peso baixo. Tratamento e Destinação têm muitos zeros e muitos 100, variam muito e por isso dominam.

O CRITIC fica entre os dois extremos na escala min-max, com Destinação muito à frente (36,6%) e os outros quatro entre 13% e 20%. Na escala pela soma, ele se parece com a ABES em Esgoto, Tratamento e Coleta e difere dela num ponto: tira peso de Água (de 26,7% para 17,7%) e o passa para Destinação (de 18,7% para 34,0%). Destinação é o único indicador que o Gaussiano e o CRITIC colocam no topo, por razões parecidas: é quase binário e não acompanha os demais.

## Concordância entre os rankings

Esta seção e a seguinte comparam primeiro a ABES e os dois AHP e, depois, os quatro rankings PROMETHEE II. Os pesos CRITIC aparecem aqui pelo PROMETHEE II, o único método de agregação calculado até agora com eles.

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

### PROMETHEE II

Com pesos iguais, CRITIC e AHP Gaussiano, o PROMETHEE II concorda com a ABES mais do que os dois AHP concordam com ela. A exceção são os pesos do AHP clássico, com a menor correlação do parecer.

| Par comparado | Spearman (ρ) | Kendall (τ-b) | Deslocamento médio (posições) |
| --- | --- | --- | --- |
| PROMETHEE II (pesos iguais) × ABES | 0,949 | 0,824 | 35,4 |
| PROMETHEE II (CRITIC) × ABES | 0,988 | 0,917 | 16,1 |
| PROMETHEE II (AHP Gaussiano) × ABES | 0,955 | 0,826 | 32,2 |
| PROMETHEE II (AHP clássico) × ABES | 0,713 | 0,535 | 88,6 |
| PROMETHEE II × soma ponderada, ambos com pesos do AHP Gaussiano | 0,973 | 0,859 | 25,7 |
| PROMETHEE II × soma ponderada, ambos com pesos do AHP clássico | 0,900 | 0,726 | 50,9 |

Todas as correlações são positivas e significativas (p < 10⁻⁷⁰, n = 505). As duas últimas linhas comparam rankings com os mesmos pesos, então a diferença entre eles vem só da forma de agregar.

- **CRITIC quase reproduz a ABES** (ρ = 0,988). Os dois dão a Destinação um papel decisivo: na ABES, porque o indicador vale 0 ou 100 e entra com toda essa amplitude na soma; no PROMETHEE II com CRITIC, porque ele tem o maior peso (36,6%) e uma função em U, que trata quase toda diferença como preferência total. Dos 50 primeiros, 47 têm Destinação 100 na ABES e 49 no PROMETHEE II com CRITIC.
- **O AHP clássico se afasta.** Com 68% do peso em Água e Coleta, e a compensação limitada, municípios com Água e Coleta acima de 90 e quase nenhum esgoto sobem muito, porque a perda em Esgoto e Tratamento está limitada aos pesos desses critérios (16,0% e 9,7%). Esplanada (BA) vai de 396º na ABES (318º na soma ponderada clássica) para 163º, e Conceição do Coité (BA), de 381º (298º) para 153º. No sentido oposto, Saloá (PE) cai de 69º para 368º, e Prata (PB), de 51º para 333º. Os dois têm Tratamento 100, mas Água abaixo de 51.
- **A forma de agregar pesa menos que os pesos.** Mantidos os pesos, a troca de soma ponderada por PROMETHEE II dá ρ de 0,90 a 0,97. Mantido o PROMETHEE II, a troca de pesos dá ρ de 0,60 (AHP Gaussiano × AHP clássico) a 0,94 (CRITIC × AHP Gaussiano).

| Spearman (ρ) entre os PROMETHEE II | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| Pesos iguais | 1 | 0,916 | 0,897 | 0,873 |
| CRITIC | 0,916 | 1 | 0,936 | 0,663 |
| AHP Gaussiano | 0,897 | 0,936 | 1 | 0,605 |
| AHP clássico | 0,873 | 0,663 | 0,605 | 1 |

**Por que a função em U em Destinação.** Embora o indicador seja quase binário, 21 municípios têm valores intermediários, e cinco deles ficam entre 95 e 99. Com a função usual (q = p = 0), 98,3 perderia por inteiro para 100, como 0 perde, e esses municípios ficariam no meio do critério: Massapê (CE, Destinação 98,3) cairia de 237º na ABES para 384º com pesos iguais, e Saloá (PE, 96,8), de 69º para 208º. Com q = p = 5, eles empatam com os que têm 100, e Massapê e Saloá ficam em 322º e 144º com pesos iguais. As quedas que sobram vêm dos outros indicadores (Água de 37,9 em Saloá, por exemplo). A troca muda pouco as correlações (ρ com a ABES varia no máximo 0,003) e nada nos Top 10, mas evita esse efeito artificial nos casos isolados. O limiar de 5 pontos é uma escolha e entra na análise de sensibilidade a q e p.

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

### Top 10 do PROMETHEE II

Sete municípios estão nos cinco Top 10 (ABES e os quatro PROMETHEE II): Salvador, Vitória da Conquista, Aracaju, Barra dos Coqueiros, Madre de Deus, Luís Eduardo Magalhães e Jequié. Salvador é o primeiro em todos os rankings do parecer.

| Posição | ABES | PROMETHEE II, pesos iguais | PROMETHEE II, CRITIC | PROMETHEE II, AHP Gaussiano | PROMETHEE II, AHP clássico |
| --- | --- | --- | --- | --- | --- |
| 1 | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** |
| 2 | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | **Barra dos Coqueiros (SE)** |
| 3 | União dos Palmares (AL) | **Aracaju (SE)** | **Aracaju (SE)** | **Jequié (BA)** | **Aracaju (SE)** |
| 4 | **Jequié (BA)** | **Barra dos Coqueiros (SE)** | **Barra dos Coqueiros (SE)** | União dos Palmares (AL) | **Madre de Deus (BA)** |
| 5 | Porto Seguro (BA) | **Madre de Deus (BA)** | **Madre de Deus (BA)** | Campina Grande (PB) | **Vitória da Conquista (BA)** |
| 6 | Campina Grande (PB) | **Luís Eduardo Magalhães (BA)** | **Jequié (BA)** | **Luís Eduardo Magalhães (BA)** | **Luís Eduardo Magalhães (BA)** |
| 7 | **Aracaju (SE)** | **Jequié (BA)** | Campina Grande (PB) | Porto Seguro (BA) | **Jequié (BA)** |
| 8 | **Barra dos Coqueiros (SE)** | Campina Grande (PB) | **Luís Eduardo Magalhães (BA)** | **Aracaju (SE)** | Viçosa (RN) |
| 9 | **Luís Eduardo Magalhães (BA)** | Porto Seguro (BA) | Porto Seguro (BA) | **Barra dos Coqueiros (SE)** | São Francisco (SE) |
| 10 | **Madre de Deus (BA)** | Sobral (CE) | João Pessoa (PB) | **Madre de Deus (BA)** | Itabuna (BA) |

Em negrito, os municípios presentes nos cinco Top 10.

O Top 10 da ABES se mantém quase inteiro com pesos iguais e com CRITIC (9 de 10) e por inteiro com o AHP Gaussiano (10 de 10). Com o AHP clássico, ficam 7. União dos Palmares (AL), 3º na ABES, sai do Top 10 com pesos iguais, CRITIC e AHP clássico: tem Coleta de 73,9, a mais baixa entre os dez primeiros da ABES (os demais têm 88 ou mais). Na soma, as notas máximas em Água, Tratamento e Destinação cobrem essa diferença. No PROMETHEE II, a vantagem dele sobre os vizinhos de topo nesses critérios é pequena ou nula, enquanto a desvantagem em Coleta pesa contra quase todos eles. Curiosamente, o PROMETHEE II com os pesos do AHP Gaussiano tem o Top 10 da ABES, enquanto a soma ponderada com os mesmos pesos renovava metade dele.

## Pontos fortes e limitações

Nenhum método é neutro. Cada um embute uma resposta diferente à pergunta sobre o que mais importa no saneamento.

| Método | Pontos fortes | Limitações |
| --- | --- | --- |
| ABES | Simples, transparente e oficial, com comparação direta entre edições do ranking | Os 20% nominais não geram influência igual: como as notas de Coleta e Água são mais altas, na escala normalizada elas equivalem a 31% e 27%, contra 9,5% de Tratamento |
| AHP Clássico | Pesos explícitos e justificáveis, com consistência verificada (RC = 0,015); permite discutir prioridades de política pública | Depende do julgamento de quem preenche a matriz; outro decisor pode chegar a pesos e rankings diferentes |
| AHP Gaussiano | Objetivo e reprodutível, sem julgamento humano; destaca os indicadores que de fato separam os municípios | Peso alto significa "varia muito", não "é importante"; Coleta, quase universalizada, recebe só 6,8%. Os pesos também mudam conforme a amostra de municípios |
| CRITIC | Objetivo e reprodutível; além da dispersão, desconta a informação repetida entre indicadores correlacionados | Só calcula pesos, e o ranking depende do método de agregação escolhido depois. Os pesos dependem da normalização (min-max aqui) e da amostra. Com correlações baixas como as daqui, o conflito pesa pouco, e Destinação, quase binário, recebe 36,6% |
| PROMETHEE II | Compensação limitada: uma nota muito baixa num indicador custa no máximo o peso dele. Dispensa normalização e lida bem com indicadores quase binários (função em U). Gera uma ordem completa, e os fluxos por critério mostram onde cada município ganha e perde | Exige escolher uma função e dois limiares por critério, o que acrescenta parâmetros a testar (sensibilidade a q e p). Os limiares pelos quartis dependem da amostra. Como cada município é comparado com todos os outros, incluir ou excluir municípios pode inverter a ordem de outros dois (*rank reversal*). Em Destinação, a função em U trata qualquer diferença acima de 5 pontos como preferência total, então 60 contra 100 conta tanto quanto 0 contra 100 |

Um cuidado vale para todos os métodos: os indicadores Tratamento e Destinação têm muitos zeros. Parte desses zeros pode refletir ausência de informação, e não ausência de serviço. Isso afeta sobretudo o Gaussiano e o CRITIC, que dão a esses dois indicadores 64% e 56% do peso, e também o PROMETHEE II, em que um zero em Destinação perde por inteiro para qualquer valor acima de 5.

## Síntese das diferenças

Este parecer não elege um método. Ele registra em que os métodos diferem, para servir de base à comparação com as demais formas de ranqueamento do trabalho.

- **O que define o peso.** Na ABES, nenhuma decisão: os pesos são iguais nas notas brutas. No AHP Clássico, o julgamento declarado de importância. No AHP Gaussiano, a dispersão dos dados. No CRITIC, a dispersão e o conflito entre os indicadores.
- **Onde o peso se concentra.** Na escala normalizada, a ABES e o Clássico concentram o peso em Água e Coleta (58% e 68%). O Gaussiano o concentra em Tratamento e Destinação (64%). O CRITIC dá o maior peso a Destinação (36,6% em min-max, 34,0% na escala pela soma).
- **Como a pontuação é formada.** A ABES usa a soma simples das notas brutas, e os dois AHP usam a soma ponderada dos valores normalizados. As duas formas são aditivas e compensatórias. O PROMETHEE II compara os municípios dois a dois e ordena pelo fluxo líquido, com compensação limitada.
- **Concordância com a ABES.** Os dois AHP têm correlação forte com ela (ρ de 0,87 a 0,89). No topo, porém, o Clássico mantém 9 dos 10 primeiros, e o Gaussiano, 5.
- **Concordância entre os AHP.** A correlação entre os dois (ρ = 0,76) é menor que a de qualquer deles com a ABES, porque cada um se afasta dela numa direção.
- **Núcleo estável.** Salvador, Vitória da Conquista, União dos Palmares, Jequié e Porto Seguro estão no Top 10 dos três métodos. Salvador, Vitória da Conquista, Aracaju, Barra dos Coqueiros, Madre de Deus, Luís Eduardo Magalhães e Jequié estão no Top 10 da ABES e dos quatro PROMETHEE II.
- **PROMETHEE II e ABES.** Com pesos iguais, CRITIC e AHP Gaussiano, o PROMETHEE II fica mais perto da ABES (ρ de 0,95 a 0,99) do que os dois AHP. Com os pesos do AHP clássico, fica mais longe (ρ = 0,71).
- **Pesos contra agregação.** No PROMETHEE II, trocar os pesos muda mais o ranking (ρ de 0,60 a 0,94 entre esquemas) do que trocar a soma ponderada pelo PROMETHEE II com os mesmos pesos (ρ de 0,90 a 0,97).

Duas verificações fortaleceriam essa comparação: testar como o ranking Clássico muda com pequenas variações nos julgamentos da matriz de Saaty, e como o PROMETHEE II muda com q e p a ±50% e com outros limiares em Destinação (basta trocar os limiares na aba PARÂMETROS da planilha).
