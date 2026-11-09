# Parecer técnico: métodos multicritério do ranking de saneamento

Nov 8, 2026 · @Guilherme de Farias

## Objetivo e escopo

Este parecer reúne, à medida que forem calculados, todos os métodos do trabalho, separados em métodos de pesos e métodos de agregação. Até aqui ele cobre a ABES, os dois AHP, o CRITIC, o PROMETHEE II, o VIKOR e o TOPSIS. Os três primeiros produzem rankings fortemente concordantes no conjunto dos municípios, mas divergem no topo. O CRITIC, que só calcula pesos, concentra 36,6% do peso em Destinação, mais que qualquer outro esquema. O PROMETHEE II, que só ranqueia, foi aplicado aos quatro esquemas de pesos. Com pesos iguais, CRITIC e AHP Gaussiano ele fica muito perto da ABES (ρ de 0,95 a 0,99). Com os pesos do AHP clássico, ele se afasta dela (ρ = 0,71). O VIKOR, também só de agregação, foi aplicado aos mesmos quatro esquemas. Com pesos iguais, ele fica muito perto da ABES (ρ = 0,98), mais que o PROMETHEE II com os mesmos pesos; com os pesos do AHP clássico, é o ranking mais distante dela calculado até aqui (ρ = 0,70). Nos quatro esquemas, Salvador é a solução de compromisso única. O TOPSIS, o último método de agregação, também foi aplicado aos quatro esquemas. Com a normalização vetorial, os 20% nominais deixam de ser iguais em efeito: Esgoto e Tratamento, com muitos zeros, ganham influência, e o TOPSIS de pesos iguais se afasta mais da ABES (ρ = 0,91) que o PROMETHEE II e o VIKOR de pesos iguais. Com os pesos do AHP Gaussiano, ele praticamente repete a soma ponderada (ρ = 0,99), e com os do AHP clássico é o ranking mais distante da ABES (ρ = 0,69). Salvador é o primeiro nos quatro.

| Método | Papel | Situação neste parecer | Planilha |
| --- | --- | --- | --- |
| ABES | Pesos iguais + soma simples das notas brutas | Incluído (pesos e ranking) | *relatorio ABES 2026 NE.ods* |
| AHP Clássico | Pesos (Saaty) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Classico.ods* |
| AHP Gaussiano | Pesos (coeficiente de variação) + soma ponderada normalizada | Incluído (pesos e ranking) | *AHP Gaussiano.ods* |
| CRITIC | Só pesos (dispersão + conflito) | Incluído (pesos) | *CRITIC.ods* |
| Pesos iguais na escala normalizada | Só pesos | A incluir | — |
| TOPSIS | Só agregação (proximidade relativa ao ideal, compensação total) | Incluído (ranking nos quatro esquemas de pesos) | *TOPSIS.ods* |
| VIKOR | Só agregação (solução de compromisso, compensação parcial) | Incluído (ranking nos quatro esquemas de pesos) | *VIKOR.ods* |
| PROMETHEE II | Só agregação (comparação par a par, compensação limitada) | Incluído (ranking nos quatro esquemas de pesos) | *PROMETHEE II.ods* |

A análise usa os **505 municípios do Nordeste habilitados** no Ranking ABES 2026, isto é, excluídos os "Não habilitados". Os cinco indicadores usados são:

- **Água**: IAG0001
- **Esgoto**: IES0001
- **Tratamento**: IES2003
- **Coleta**: IRS0001
- **Destinação**: IRS3002

Todos os números vêm das planilhas da pasta `planilhas/` indicadas na tabela acima.

## Os métodos: formas de pesar e formas de ranquear

Os métodos se distinguem em duas etapas: como se definem os pesos dos cinco indicadores e como esses pesos se combinam com o desempenho de cada município. Alguns métodos cobrem só a primeira etapa (CRITIC), outros só a segunda (TOPSIS, VIKOR, PROMETHEE II), e a ABES e os AHP, como aplicados aqui, cobrem as duas. Até aqui, há quatro formas de pesar e cinco de ranquear.

### Formas de pesar os critérios

| Método | Como os pesos são obtidos | Natureza do peso |
| --- | --- | --- |
| ABES | Nenhum cálculo: os cinco indicadores entram com o mesmo peso | Nominal e igual: 20% para cada indicador |
| AHP Clássico | Comparação par a par dos critérios na escala de Saaty, com pesos pela média geométrica das linhas da matriz (RC = 0,0152, consistente) | Subjetiva: expressa o julgamento de importância do decisor |
| AHP Gaussiano | Coeficiente de variação de cada indicador (desvio-padrão ÷ média), normalizado para somar 1 | Objetiva: expressa quanto os municípios diferem entre si em cada indicador |
| CRITIC | Desvio-padrão de cada indicador normalizado por min-max, multiplicado pelo conflito com os demais (Σ de 1 − correlação), normalizado para somar 1 | Objetiva: expressa quanto o indicador varia e quanto traz de informação que os outros não trazem |

Os valores de cada peso estão na seção "Pesos resultantes". O CRITIC não tem forma de ranquear própria: seus pesos são aplicados pelos métodos de agregação. Até aqui, isso foi feito no PROMETHEE II, no VIKOR e no TOPSIS.

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
| Índice de compromisso | VIKOR, com qualquer dos quatro esquemas de pesos | Distâncias ao melhor valor observado, normalizadas por min-max (0 a 1) | Combina a soma das distâncias ponderadas (S) com a maior delas (R); menor índice Q, melhor posição |
| Proximidade relativa ao ideal | TOPSIS, com qualquer dos quatro esquemas de pesos | Valores normalizados pela norma vetorial (cada indicador dividido pela raiz da soma dos quadrados) | Distâncias euclidianas ao ideal positivo (D⁺) e ao negativo (D⁻); maior C* = D⁻/(D⁺ + D⁻), melhor posição |

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

### VIKOR

O VIKOR (Opricovic e Tzeng, 2004) busca uma **solução de compromisso**: o município mais perto do ideal, medido de duas formas ao mesmo tempo. A desvantagem agregada S soma as distâncias ponderadas ao ideal nos cinco indicadores, como uma soma ponderada. O arrependimento individual R pega só a maior dessas distâncias, isto é, o indicador em que o município está pior. O índice Q combina as duas medidas com o parâmetro v, e o ranking vai do menor para o maior Q. Como o PROMETHEE II, o VIKOR é só um método de agregação e foi aplicado aos quatro esquemas de pesos.

As contas seguem as dez etapas do mapa mental do método (apresentação da UNIFOR):

1. **Entradas:** os 505 municípios, os cinco indicadores (todos de benefício), a matriz de notas fᵢⱼ e os pesos wⱼ, que somam 1.
2. **Ideal e anti-ideal:** f*ⱼ = maior valor observado e f⁻ⱼ = menor valor observado em cada indicador. Todos chegam a 100; quatro chegam a 0, e Coleta, a 18,67.
3. **Distância normalizada:** dᵢⱼ = (f*ⱼ − fᵢⱼ)/(f*ⱼ − f⁻ⱼ), entre 0 (no ideal) e 1 (no anti-ideal). É uma normalização min-max invertida.
4. **Desvantagem ponderada:** tᵢⱼ = wⱼ·dᵢⱼ, entre 0 e wⱼ.
5. **Desvantagem agregada:** Sᵢ = Σⱼ tᵢⱼ.
6. **Arrependimento individual:** Rᵢ = maxⱼ tᵢⱼ.
7. **Índice de compromisso:** Qᵢ, entre 0 e 1, pela fórmula abaixo.
8. **Classificação:** posições crescentes por S, por R e por Q.
9. **Condições de aceitação:** C1, vantagem aceitável, exige Q(a⁽²⁾) − Q(a⁽¹⁾) ≥ DQ = 1/(m − 1); C2, estabilidade aceitável, exige que a⁽¹⁾ também seja a primeira por S ou por R.
10. **Solução:** se C1 e C2 valem, a⁽¹⁾ é a solução única; se só C2 falha, o conjunto de compromisso é {a⁽¹⁾, a⁽²⁾}; se C1 falha, ele reúne as primeiras colocadas até a última com Q(a⁽ᴹ⁾) − Q(a⁽¹⁾) < DQ.

```math
Q_i = v \, \frac{S_i - S^*}{S^- - S^*} + (1 - v) \, \frac{R_i - R^*}{R^- - R^*}, \qquad S^* = \min_i S_i, \; S^- = \max_i S_i, \; R^* = \min_i R_i, \; R^- = \max_i R_i
```

**Parâmetro v.** Usa-se v = 0,5, o valor da apresentação da UNIFOR e o mais comum na literatura: S e R pesam o mesmo em Q. Com v perto de 1, o VIKOR se aproxima de uma soma ponderada (estratégia da maioria); com v perto de 0, ele ordena pelo pior indicador de cada município. A sensibilidade a v (0,25 e 0,75, como previsto no guia de escrita) entra na análise de robustez; basta trocar a célula B22 da aba PARÂMETROS.

**Os pesos no VIKOR.** Como no PROMETHEE II, o peso multiplica valores de 0 a 1, que não dependem da escala do indicador. Por isso, "pesos iguais" são 20% de fato, e os pesos CRITIC entram na versão min-max, a mesma normalização do dᵢⱼ.

**Com pesos iguais, S é quase a ABES.** Como quatro indicadores vão de 0 a 100, a distância normalizada é (100 − nota)/100, e S é praticamente uma função linear da Pontuação total da ABES (ρ = 0,999 entre os dois; só a amplitude de Coleta, 81,33, foge da regra). O que o VIKOR acrescenta à ABES vem, portanto, de R.

**O papel de R.** Todo município com nota no anti-ideal (dᵢⱼ = 1) no indicador de maior peso tem R igual a esse peso, o máximo possível. Nesses casos, a metade de Q que vem de R vale 0,5, e o município só se diferencia dos demais por S. Com os cinco indicadores tão cheios de zeros, isso acontece com muitos municípios:

| Esquema de pesos | Indicador de maior peso | Municípios com R no máximo (R⁻) | Melhor posição entre eles no VIKOR |
| --- | --- | --- | --- |
| Pesos iguais | Todos (20%) | 340 (zero em Tratamento ou em Destinação) | 91º |
| CRITIC | Destinação (36,6%) | 248 (Destinação 0) | 253º |
| AHP Gaussiano | Tratamento (34,9%) | 154 (Tratamento 0) | 132º |
| AHP clássico | Água (41,7%) | 1 (Água no mínimo observado) | 503º |

Por exemplo, com pesos iguais, Viçosa (RN) tem Água, Esgoto, Tratamento e Coleta acima de 90, mas Destinação 0. A distância dela é 1 em Destinação e quase 0 nos outros: S = 0,233 e R = 0,2, o máximo. Dormentes (PE) tem as cinco notas entre 24 e 54, sem nenhum zero: S = 0,641, bem pior, mas R = 0,151. No índice, Viçosa fica com Q = 0,125 + 0,500 = 0,625, e Dormentes com Q = 0,381 + 0,361 = 0,742. Viçosa ainda fica à frente (93º contra 196º), mas a distância entre as duas encolhe muito em relação à ABES (41º contra 393º). Com CRITIC, o efeito é mais forte: os 248 municípios sem Destinação ocupam praticamente as 253 últimas posições, e só cinco municípios com Destinação acima de zero ficam abaixo do melhor deles.

**Compensação parcial.** S é compensatório, como a soma ponderada. R não é: uma nota muito ruim num indicador não é compensada pelos outros. Com v = 0,5, o VIKOR fica no meio do caminho e favorece municípios equilibrados, sem nenhum indicador no pior valor observado.

**Como a planilha calcula.** A aba DISTÂNCIAS NORMALIZADAS calcula dᵢⱼ (etapas 2 e 3, com f* e f⁻ na aba PARÂMETROS), a aba DESVANTAGENS PONDERADAS calcula tᵢⱼ nos quatro esquemas (etapa 4), e a aba ÍNDICES S, R E Q calcula S, R, Q e as três classificações (etapas 5 a 8). A aba CONDIÇÕES C1 E C2 testa as condições e monta a solução de compromisso (etapas 9 e 10). Os valores de S, R e Q foram conferidos com um cálculo independente em Python, com diferença máxima de 3 × 10⁻¹⁶.

**Condições de aceitação.** Salvador é a solução de compromisso única nos quatro esquemas de pesos. Ela é a primeira por S e por R (C2) e tem Q = 0, com vantagem sobre a segunda colocada de 14 a 28 vezes o limiar DQ = 1/504 ≈ 0,002 (C1).

| Esquema de pesos | 2ª colocada | Q(a⁽²⁾) − Q(a⁽¹⁾) | C1 | C2 | Resultado |
| --- | --- | --- | --- | --- | --- |
| Pesos iguais | Vitória da Conquista (BA) | 0,055 | Sim | Sim | Salvador (solução única) |
| CRITIC | Vitória da Conquista (BA) | 0,042 | Sim | Sim | Salvador (solução única) |
| AHP Gaussiano | União dos Palmares (AL) | 0,038 | Sim | Sim | Salvador (solução única) |
| AHP clássico | Vitória da Conquista (BA) | 0,027 | Sim | Sim | Salvador (solução única) |

Com 505 alternativas, DQ é muito baixo, e C1 só falharia com as duas primeiras praticamente empatadas. As condições servem para recomendar uma solução, que aqui seria o melhor município; para este trabalho, que compara ordenações inteiras, o resultado principal é o ranking por Q.

### TOPSIS

O TOPSIS (Hwang e Yoon, 1981) ordena os municípios pela **proximidade relativa à solução ideal**. Ele monta dois municípios teóricos: o ideal positivo A⁺, com o melhor valor observado em cada indicador, e o ideal negativo A⁻, com o pior. Depois mede a distância euclidiana de cada município a cada um deles. O melhor município é o que fica, ao mesmo tempo, perto de A⁺ e longe de A⁻. Como o PROMETHEE II e o VIKOR, o TOPSIS é só um método de agregação e foi aplicado aos quatro esquemas de pesos.

As contas seguem as oito etapas do mapa mental do método:

1. **Matriz de decisão:** X = [xᵢⱼ], com os 505 municípios e os cinco indicadores, todos de benefício.
2. **Normalização vetorial:** rᵢⱼ = xᵢⱼ/√Σᵢ x²ᵢⱼ. Cada indicador é dividido pela raiz da soma dos quadrados das suas notas.
3. **Ponderação:** vᵢⱼ = wⱼ·rᵢⱼ.
4. **Soluções ideais:** A⁺ⱼ = maxᵢ vᵢⱼ e A⁻ⱼ = minᵢ vᵢⱼ (o contrário para critérios de custo, que aqui não há).
5. **Distância ao ideal positivo:** D⁺ᵢ = √Σⱼ(vᵢⱼ − A⁺ⱼ)².
6. **Distância ao ideal negativo:** D⁻ᵢ = √Σⱼ(vᵢⱼ − A⁻ⱼ)².
7. **Proximidade relativa:** C*ᵢ = D⁻ᵢ/(D⁺ᵢ + D⁻ᵢ), entre 0 (no ideal negativo) e 1 (no ideal positivo).
8. **Ranking:** ordem decrescente de C*. Em empate, vale a ordem da base, como o desempate pelo identificador do mapa mental.

```math
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}} \qquad D_i^{\pm} = \sqrt{\sum_{j=1}^{5} \left( w_j r_{ij} - A_j^{\pm} \right)^2} \qquad C_i^* = \frac{D_i^-}{D_i^+ + D_i^-}
```

Nenhum município chega a C* = 1, porque nenhum tem o melhor valor nos cinco indicadores. Salvador é o primeiro nos quatro esquemas, com C* de 0,937 a 0,953.

**A normalização vetorial muda o efeito dos pesos.** A normalização é a do mapa mental e a do TOPSIS original, e o guia de escrita já a registrava. Ela preserva as proporções (um zero continua zero), mas a amplitude de rᵢⱼ depende do indicador. Nos indicadores com muitos zeros, a soma dos quadrados é menor, e a mesma diferença de pontos vale mais. Por isso o peso nominal não mede a influência do critério na distância; essa influência é proporcional a wⱼ vezes a amplitude de rᵢⱼ. A aba PARÂMETROS calcula essa influência efetiva:

| Indicador | Amplitude de rᵢⱼ | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- | --- |
| Água | 0,061 | 15,9% | 10,7% | 5,9% | 37,4% |
| Esgoto | 0,102 | 26,4% | 20,7% | 23,6% | 23,9% |
| Tratamento | 0,115 | 29,9% | 29,5% | 45,7% | 16,4% |
| Coleta | 0,043 | 11,2% | 8,4% | 3,3% | 16,6% |
| Destinação | 0,064 | 16,6% | 30,7% | 21,5% | 5,7% |

Com 20% nominais para cada indicador, Tratamento e Esgoto somam 56% da influência, e Coleta fica com 11%. É o mesmo problema dos 20% da ABES, em sentido oposto: lá, as notas altas de Água e Coleta lhes dão mais peso na escala normalizada; aqui, os zeros de Esgoto e Tratamento lhes dão mais peso na distância. O efeito empurra o TOPSIS de pesos iguais na direção do AHP Gaussiano (ρ = 0,951 entre os dois TOPSIS) e reforça o próprio Gaussiano, em que Tratamento passa de 34,9% nominais para 45,7% de influência.

**Normalização como parâmetro.** A célula B30 da aba PARÂMETROS troca a normalização vetorial pela min-max, a do CRITIC e do dᵢⱼ do VIKOR, com a qual 20% passam a ser peso igual de fato. Com min-max, o TOPSIS de pesos iguais praticamente reproduz a ABES (ρ = 0,996), e o de AHP clássico se afasta ainda mais dela (ρ = 0,642). A versão vetorial é a principal; a min-max entra na análise de robustez.

**Compensação total.** C* é uma razão entre distâncias euclidianas, e um bom valor num indicador reduz D⁺ e aumenta D⁻ tanto quanto um valor ruim em outro os piora. Não há limite por critério, como a função de preferência do PROMETHEE II, nem parcela dedicada ao pior indicador, como o R do VIKOR. Por isso o TOPSIS fica do lado compensatório, junto da soma ponderada. A diferença para a soma ponderada está no quadrado das distâncias, que pesa mais as grandes desvantagens que as pequenas.

**Como a planilha calcula.** A aba MATRIZ NORMALIZADA calcula rᵢⱼ (etapas 1 e 2, com a norma de cada indicador na aba PARÂMETROS), a aba MATRIZ PONDERADA calcula vᵢⱼ nos quatro esquemas (etapa 3), a aba SOLUÇÕES IDEAIS monta A⁺ e A⁻ (etapa 4) e a aba DISTÂNCIAS E PROXIMIDADE calcula D⁺, D⁻, C* e as posições (etapas 5 a 7). A aba RANKING ordena os municípios (etapa 8). Os valores de D⁺, D⁻ e C* foram conferidos com um cálculo independente em Python, com diferença máxima de 8 × 10⁻¹⁶, nas duas normalizações.

**Os pesos no TOPSIS.** São os mesmos do PROMETHEE II e do VIKOR (20% e CRITIC min-max), para que as comparações com mesmos pesos sejam diretas. A diferença de efeito causada pela normalização vetorial fica registrada na tabela acima, e não corrigida nos pesos.

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

Esta seção e a seguinte comparam primeiro a ABES e os dois AHP e, depois, os quatro rankings PROMETHEE II, os quatro rankings VIKOR e os quatro rankings TOPSIS. Os pesos CRITIC aparecem aqui pelo PROMETHEE II, pelo VIKOR e pelo TOPSIS, os métodos de agregação calculados até agora com eles.

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

### VIKOR

Com pesos iguais, o VIKOR fica mais perto da ABES (ρ = 0,977) que o PROMETHEE II de pesos iguais (0,949), atrás só do PROMETHEE II com CRITIC (0,988). Com os outros pesos, ele se afasta mais da ABES que o PROMETHEE II de mesmos pesos, sobretudo com CRITIC (0,920 contra 0,988). Com o AHP clássico, os dois métodos chegam ao mesmo lugar: ρ de 0,705 com a ABES no VIKOR e de 0,713 no PROMETHEE II, e ρ = 0,976 entre eles.

| Par comparado | Spearman (ρ) | Kendall (τ-b) | Deslocamento médio (posições) |
| --- | --- | --- | --- |
| VIKOR (pesos iguais) × ABES | 0,977 | 0,896 | 20,0 |
| VIKOR (CRITIC) × ABES | 0,920 | 0,803 | 37,6 |
| VIKOR (AHP Gaussiano) × ABES | 0,895 | 0,722 | 50,3 |
| VIKOR (AHP clássico) × ABES | 0,705 | 0,532 | 89,3 |
| VIKOR × soma ponderada, ambos com pesos do AHP Gaussiano | 0,970 | 0,857 | 29,7 |
| VIKOR × soma ponderada, ambos com pesos do AHP clássico | 0,897 | 0,734 | 49,9 |
| VIKOR × PROMETHEE II, ambos com pesos iguais | 0,906 | 0,759 | 45,7 |
| VIKOR × PROMETHEE II, ambos com CRITIC | 0,956 | 0,851 | 28,4 |
| VIKOR × PROMETHEE II, ambos com pesos do AHP Gaussiano | 0,944 | 0,805 | 38,3 |
| VIKOR × PROMETHEE II, ambos com pesos do AHP clássico | 0,976 | 0,866 | 24,6 |

Todas as correlações são positivas e significativas (p < 10⁻⁷⁰, n = 505). As seis últimas linhas comparam rankings com os mesmos pesos, então a diferença entre eles vem só da forma de agregar. Os fluxos do PROMETHEE II entram na planilha do VIKOR como valores copiados de *PROMETHEE II.ods*.

- **Com pesos iguais, o VIKOR é quase a ABES.** S reproduz a ABES (ρ = 0,999), e R só reordena os municípios dentro de faixas próximas. Os que mais sobem têm todas as notas medianas e nenhum zero: Dormentes (PE) vai de 393º para 196º, e Quixelô (CE), de 370º para 236º. Os que mais caem têm notas altas e um zero: Cedro de São João (SE), com Tratamento 0, cai de 34º para 91º, e Viçosa (RN), com Destinação 0, de 41º para 93º.
- **Com CRITIC, Destinação divide o ranking em dois blocos.** O R dos 248 municípios sem Destinação é o peso do indicador (36,6%), e eles ficam praticamente todos depois do 252º lugar. Viçosa (RN) vai de 41º na ABES (92º no PROMETHEE II com CRITIC) para 253º, e Acari (RN), de 61º para 254º, ambos com as outras quatro notas acima de 80. No sentido oposto, Teixeira (PB), com Água 0,01 e Tratamento 0, mas Destinação 41,7, sobe de 485º para 252º. No PROMETHEE II, a função em U também pune o zero em Destinação, mas a perda fica limitada ao peso do critério em cada comparação; no VIKOR, metade do índice passa a depender só desse indicador.
- **Com o AHP clássico, os dois métodos de compensação limitada concordam.** O peso de Água (41,7%) domina tanto R quanto os fluxos do PROMETHEE II. Guamaré (RN), com Água 27,0 e Tratamento e Destinação 100, cai de 50º na ABES para 433º (313º no PROMETHEE II), e Saloá (PE), de 69º para 409º. Abaíra (BA), com Água 89,9 e zeros em Tratamento e Destinação, sobe de 351º para 139º.
- **A forma de agregar pesa menos que os pesos, de novo.** Mantidos os pesos, trocar a soma ponderada ou o PROMETHEE II pelo VIKOR dá ρ de 0,90 a 0,98. Mantido o VIKOR, trocar os pesos dá ρ de 0,48 (CRITIC × AHP clássico) a 0,95 (pesos iguais × CRITIC), faixa mais larga que a do PROMETHEE II (0,60 a 0,94).

| Spearman (ρ) entre os VIKOR | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| Pesos iguais | 1 | 0,952 | 0,927 | 0,649 |
| CRITIC | 0,952 | 1 | 0,885 | 0,477 |
| AHP Gaussiano | 0,927 | 0,885 | 1 | 0,503 |
| AHP clássico | 0,649 | 0,477 | 0,503 | 1 |

### TOPSIS

Com pesos iguais e com CRITIC, o TOPSIS fica a uma distância parecida da ABES (ρ = 0,915 e 0,927). Com pesos iguais, é o mais longe dela entre os três métodos (0,949 no PROMETHEE II e 0,977 no VIKOR); com CRITIC, fica entre o VIKOR (0,920) e o PROMETHEE II (0,988). Com os pesos do AHP Gaussiano, ele é quase a soma ponderada com os mesmos pesos (ρ = 0,990, a maior concordância entre formas de agregar do parecer). Com os pesos do AHP clássico, é o ranking mais distante da ABES calculado até aqui (ρ = 0,695).

| Par comparado | Spearman (ρ) | Kendall (τ-b) | Deslocamento médio (posições) |
| --- | --- | --- | --- |
| TOPSIS (pesos iguais) × ABES | 0,915 | 0,764 | 44,1 |
| TOPSIS (CRITIC) × ABES | 0,927 | 0,781 | 40,8 |
| TOPSIS (AHP Gaussiano) × ABES | 0,845 | 0,663 | 61,4 |
| TOPSIS (AHP clássico) × ABES | 0,695 | 0,520 | 94,5 |
| TOPSIS × soma ponderada, ambos com pesos do AHP Gaussiano | 0,990 | 0,924 | 15,2 |
| TOPSIS × soma ponderada, ambos com pesos do AHP clássico | 0,937 | 0,787 | 39,2 |
| TOPSIS × PROMETHEE II, ambos com pesos iguais | 0,898 | 0,729 | 50,6 |
| TOPSIS × PROMETHEE II, ambos com CRITIC | 0,947 | 0,807 | 36,1 |
| TOPSIS × PROMETHEE II, ambos com pesos do AHP Gaussiano | 0,953 | 0,821 | 32,6 |
| TOPSIS × PROMETHEE II, ambos com pesos do AHP clássico | 0,949 | 0,803 | 36,9 |
| TOPSIS × VIKOR, ambos com pesos iguais | 0,882 | 0,719 | 51,5 |
| TOPSIS × VIKOR, ambos com CRITIC | 0,974 | 0,873 | 23,6 |
| TOPSIS × VIKOR, ambos com pesos do AHP Gaussiano | 0,942 | 0,800 | 40,8 |
| TOPSIS × VIKOR, ambos com pesos do AHP clássico | 0,959 | 0,834 | 29,9 |

Todas as correlações são positivas e significativas (p < 10⁻⁶⁷, n = 505). As dez últimas linhas comparam rankings com os mesmos pesos, então a diferença entre eles vem só da forma de agregar e da normalização de cada método. Os fluxos do PROMETHEE II e os índices Q do VIKOR entram na planilha do TOPSIS como valores copiados de *PROMETHEE II.ods* e *VIKOR.ods*.

- **Com pesos iguais, o TOPSIS segue a influência efetiva, e não os 20%.** Os que mais sobem têm Tratamento e Esgoto médios e Destinação 0: Mutuípe (BA) vai de 384º na ABES para 131º, e Tasso Fragoso (MA), de 283º para 115º. Os que mais caem têm Água, Coleta e Destinação no máximo, mas quase nenhum esgoto: Barra de Santo Antônio (AL), com Esgoto 5,0 e Tratamento 1,5, cai de 152º para 278º, e Campo do Brito (SE), de 143º para 260º. É o mesmo movimento da soma ponderada com os pesos do AHP Gaussiano (Mutuípe é o 106º nela), o que explica por que, com pesos iguais, o TOPSIS concorda menos com o PROMETHEE II e o VIKOR (0,90 e 0,88) do que com os outros pesos.
- **Com CRITIC, o zero em Destinação pesa, mas não divide o ranking.** O melhor dos 248 municípios sem Destinação fica em 101º, contra 92º no PROMETHEE II e 253º no VIKOR. Itapetinga (BA), com Água 100, Esgoto 98,7 e Coleta 97,0, cai de 106º na ABES para 284º. Santa Filomena (PE), com Destinação 100 e Tratamento 61,1, sobe de 271º para 66º. Mesmo assim, é com CRITIC que o TOPSIS mais se aproxima do VIKOR (ρ = 0,974).
- **Com o AHP clássico, os três métodos de agregação convergem.** Água tem 37,4% da influência, e os municípios com Água baixa caem: Guamaré (RN), com Água 27,0 e Tratamento e Destinação 100, vai de 50º na ABES para 354º, e Saloá (PE), de 69º para 336º. Brejões (BA), com Água 99,1 e zeros em Tratamento e Destinação, sobe de 345º para 110º. O TOPSIS fica a ρ = 0,95 do PROMETHEE II e a 0,96 do VIKOR com os mesmos pesos.
- **A forma de agregar pesa menos que os pesos, mais uma vez.** Mantidos os pesos, trocar a soma ponderada, o PROMETHEE II ou o VIKOR pelo TOPSIS dá ρ de 0,88 a 0,99. Mantido o TOPSIS, trocar os pesos dá ρ de 0,45 (CRITIC × AHP clássico) a 0,95 (pesos iguais × AHP Gaussiano), a faixa mais larga dos três métodos.

| Spearman (ρ) entre os TOPSIS | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| Pesos iguais | 1 | 0,854 | 0,951 | 0,712 |
| CRITIC | 0,854 | 1 | 0,861 | 0,448 |
| AHP Gaussiano | 0,951 | 0,861 | 1 | 0,527 |
| AHP clássico | 0,712 | 0,448 | 0,527 | 1 |

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

### Top 10 do VIKOR

Cinco municípios estão nos cinco Top 10 (ABES e os quatro VIKOR): Salvador, Vitória da Conquista, Jequié, Luís Eduardo Magalhães e Porto Seguro. Salvador é o primeiro em todos.

| Posição | ABES | VIKOR, pesos iguais | VIKOR, CRITIC | VIKOR, AHP Gaussiano | VIKOR, AHP clássico |
| --- | --- | --- | --- | --- | --- |
| 1 | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** |
| 2 | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | **Vitória da Conquista (BA)** | União dos Palmares (AL) | **Vitória da Conquista (BA)** |
| 3 | União dos Palmares (AL) | **Jequié (BA)** | **Jequié (BA)** | Frei Martinho (PB) | Barra dos Coqueiros (SE) |
| 4 | **Jequié (BA)** | **Luís Eduardo Magalhães (BA)** | **Porto Seguro (BA)** | **Jequié (BA)** | Aracaju (SE) |
| 5 | **Porto Seguro (BA)** | Campina Grande (PB) | **Luís Eduardo Magalhães (BA)** | Santa Luzia (PB) | Madre de Deus (BA) |
| 6 | Campina Grande (PB) | Aracaju (SE) | União dos Palmares (AL) | **Vitória da Conquista (BA)** | **Luís Eduardo Magalhães (BA)** |
| 7 | Aracaju (SE) | **Porto Seguro (BA)** | Campina Grande (PB) | **Porto Seguro (BA)** | **Jequié (BA)** |
| 8 | Barra dos Coqueiros (SE) | João Pessoa (PB) | Aracaju (SE) | **Luís Eduardo Magalhães (BA)** | Viçosa (RN) |
| 9 | **Luís Eduardo Magalhães (BA)** | União dos Palmares (AL) | João Pessoa (PB) | João Pessoa (PB) | São Francisco (SE) |
| 10 | Madre de Deus (BA) | Barra dos Coqueiros (SE) | Santa Luzia (PB) | Campina Grande (PB) | **Porto Seguro (BA)** |

Em negrito, os municípios presentes nos cinco Top 10.

O Top 10 da ABES se mantém quase inteiro com pesos iguais (9 de 10) e perde dois ou três municípios nos outros esquemas (8 com CRITIC e com o AHP clássico, 7 com o AHP Gaussiano). João Pessoa (PB), 8ª ou 9ª em três dos quatro VIKOR, não está no Top 10 da ABES e, entre os PROMETHEE II, só aparece no de CRITIC (10ª). Todas as suas notas estão entre 72 e 100, o que lhe dá um R baixo. Com o AHP clássico, o Top 10 do VIKOR repete 9 dos 10 do PROMETHEE II com os mesmos pesos, coerente com ρ = 0,976 entre os dois. Com o AHP Gaussiano, o VIKOR traz dois municípios pequenos da Paraíba que já apareciam no Top 10 da soma ponderada com esses pesos (Frei Martinho e Santa Luzia), ambos com Tratamento acima de 88 e Destinação 100.

### Top 10 do TOPSIS

Quatro municípios estão nos cinco Top 10 (ABES e os quatro TOPSIS): Salvador, Vitória da Conquista, União dos Palmares e Jequié. Salvador é o primeiro em todos.

| Posição | ABES | TOPSIS, pesos iguais | TOPSIS, CRITIC | TOPSIS, AHP Gaussiano | TOPSIS, AHP clássico |
| --- | --- | --- | --- | --- | --- |
| 1 | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** | **Salvador (BA)** |
| 2 | **Vitória da Conquista (BA)** | **União dos Palmares (AL)** | **União dos Palmares (AL)** | Frei Martinho (PB) | **Vitória da Conquista (BA)** |
| 3 | **União dos Palmares (AL)** | **Jequié (BA)** | **Jequié (BA)** | **União dos Palmares (AL)** | **Jequié (BA)** |
| 4 | **Jequié (BA)** | **Vitória da Conquista (BA)** | Frei Martinho (PB) | **Jequié (BA)** | Luís Eduardo Magalhães (BA) |
| 5 | Porto Seguro (BA) | Campina Grande (PB) | **Vitória da Conquista (BA)** | Porto Seguro (BA) | **União dos Palmares (AL)** |
| 6 | Campina Grande (PB) | Frei Martinho (PB) | Porto Seguro (BA) | Santa Luzia (PB) | Aracaju (SE) |
| 7 | Aracaju (SE) | Luís Eduardo Magalhães (BA) | Santa Luzia (PB) | **Vitória da Conquista (BA)** | Viçosa (RN) |
| 8 | Barra dos Coqueiros (SE) | Porto Seguro (BA) | Luís Eduardo Magalhães (BA) | Prata (PB) | Barra dos Coqueiros (SE) |
| 9 | Luís Eduardo Magalhães (BA) | Santa Luzia (PB) | Campina Grande (PB) | São José do Sabugi (PB) | Madre de Deus (BA) |
| 10 | Madre de Deus (BA) | Aracaju (SE) | João Pessoa (PB) | Teotônio Vilela (AL) | Campina Grande (PB) |

Em negrito, os municípios presentes nos cinco Top 10.

O Top 10 da ABES perde mais municípios no TOPSIS que no PROMETHEE II e no VIKOR: ficam 8 com pesos iguais, 7 com CRITIC, 5 com o AHP Gaussiano e 9 com o AHP clássico. Os que entram são, de novo, os municípios pequenos da Paraíba com Tratamento acima de 88 e Destinação 100 (Frei Martinho e Santa Luzia, já no Top 10 com pesos iguais), favorecidos pela influência de Tratamento. Com os pesos do AHP Gaussiano, o Top 10 do TOPSIS tem exatamente os mesmos dez municípios da soma ponderada com esses pesos, só em outra ordem, coerente com ρ = 0,990. Com o AHP clássico, ele repete 8 dos 10 do PROMETHEE II e do VIKOR com os mesmos pesos.

## Pontos fortes e limitações

Nenhum método é neutro. Cada um embute uma resposta diferente à pergunta sobre o que mais importa no saneamento.

| Método | Pontos fortes | Limitações |
| --- | --- | --- |
| ABES | Simples, transparente e oficial, com comparação direta entre edições do ranking | Os 20% nominais não geram influência igual: como as notas de Coleta e Água são mais altas, na escala normalizada elas equivalem a 31% e 27%, contra 9,5% de Tratamento |
| AHP Clássico | Pesos explícitos e justificáveis, com consistência verificada (RC = 0,015); permite discutir prioridades de política pública | Depende do julgamento de quem preenche a matriz; outro decisor pode chegar a pesos e rankings diferentes |
| AHP Gaussiano | Objetivo e reprodutível, sem julgamento humano; destaca os indicadores que de fato separam os municípios | Peso alto significa "varia muito", não "é importante"; Coleta, quase universalizada, recebe só 6,8%. Os pesos também mudam conforme a amostra de municípios |
| CRITIC | Objetivo e reprodutível; além da dispersão, desconta a informação repetida entre indicadores correlacionados | Só calcula pesos, e o ranking depende do método de agregação escolhido depois. Os pesos dependem da normalização (min-max aqui) e da amostra. Com correlações baixas como as daqui, o conflito pesa pouco, e Destinação, quase binário, recebe 36,6% |
| VIKOR | Equilibra duas visões, a do conjunto dos indicadores (S) e a do pior indicador (R), e favorece municípios sem nenhum indicador no pior valor. Tem um só parâmetro (v) e testa se a 1ª colocada é uma recomendação estável (C1 e C2) | Os valores ideal e anti-ideal são os melhores e piores observados, então mudam com a amostra, e incluir ou excluir municípios pode reordenar os demais (*rank reversal*). Com muitos zeros, R satura: todo município com o pior valor no indicador de maior peso recebe o mesmo R, e metade do índice deixa de distinguir entre eles. As condições C1 e C2 pouco informam com 505 alternativas (DQ ≈ 0,002) |
| TOPSIS | Simples e sem parâmetros além dos pesos e da normalização. Usa duas referências ao mesmo tempo (ideal positivo e negativo), e D⁺ e D⁻ mostram de onde vem a posição. Muito usado na literatura, o que facilita a comparação com outros estudos | Compensação total, como a soma ponderada: uma nota muito baixa num indicador pode ser coberta pelos outros. A normalização vetorial faz os pesos nominais perderem o sentido de influência (com 20% para cada, Tratamento e Esgoto somam 56% do efeito), e outra normalização muda o ranking. Os ideais e a norma dependem da amostra, então incluir ou excluir municípios pode reordenar os demais (*rank reversal*) |
| PROMETHEE II | Compensação limitada: uma nota muito baixa num indicador custa no máximo o peso dele. Dispensa normalização e lida bem com indicadores quase binários (função em U). Gera uma ordem completa, e os fluxos por critério mostram onde cada município ganha e perde | Exige escolher uma função e dois limiares por critério, o que acrescenta parâmetros a testar (sensibilidade a q e p). Os limiares pelos quartis dependem da amostra. Como cada município é comparado com todos os outros, incluir ou excluir municípios pode inverter a ordem de outros dois (*rank reversal*). Em Destinação, a função em U trata qualquer diferença acima de 5 pontos como preferência total, então 60 contra 100 conta tanto quanto 0 contra 100 |

Um cuidado vale para todos os métodos: os indicadores Tratamento e Destinação têm muitos zeros. Parte desses zeros pode refletir ausência de informação, e não ausência de serviço. Isso afeta sobretudo o Gaussiano e o CRITIC, que dão a esses dois indicadores 64% e 56% do peso, e também o PROMETHEE II, em que um zero em Destinação perde por inteiro para qualquer valor acima de 5, o VIKOR, em que um zero no indicador de maior peso leva R ao máximo, e o TOPSIS, em que os zeros reduzem a norma vetorial de Esgoto e Tratamento e aumentam a influência desses indicadores.

## Síntese das diferenças

Este parecer não elege um método. Ele registra em que os métodos diferem, para servir de base à comparação com as demais formas de ranqueamento do trabalho.

- **O que define o peso.** Na ABES, nenhuma decisão: os pesos são iguais nas notas brutas. No AHP Clássico, o julgamento declarado de importância. No AHP Gaussiano, a dispersão dos dados. No CRITIC, a dispersão e o conflito entre os indicadores.
- **Onde o peso se concentra.** Na escala normalizada, a ABES e o Clássico concentram o peso em Água e Coleta (58% e 68%). O Gaussiano o concentra em Tratamento e Destinação (64%). O CRITIC dá o maior peso a Destinação (36,6% em min-max, 34,0% na escala pela soma).
- **Como a pontuação é formada.** A ABES usa a soma simples das notas brutas, e os dois AHP usam a soma ponderada dos valores normalizados. As duas formas são aditivas e compensatórias. O PROMETHEE II compara os municípios dois a dois e ordena pelo fluxo líquido, com compensação limitada. O VIKOR combina a soma das distâncias ao ideal com a maior delas, com compensação parcial. O TOPSIS ordena pela proximidade relativa aos ideais positivo e negativo, com compensação total.
- **Concordância com a ABES.** Os dois AHP têm correlação forte com ela (ρ de 0,87 a 0,89). No topo, porém, o Clássico mantém 9 dos 10 primeiros, e o Gaussiano, 5.
- **Concordância entre os AHP.** A correlação entre os dois (ρ = 0,76) é menor que a de qualquer deles com a ABES, porque cada um se afasta dela numa direção.
- **Núcleo estável.** Salvador, Vitória da Conquista, União dos Palmares, Jequié e Porto Seguro estão no Top 10 dos três métodos. Salvador, Vitória da Conquista, Aracaju, Barra dos Coqueiros, Madre de Deus, Luís Eduardo Magalhães e Jequié estão no Top 10 da ABES e dos quatro PROMETHEE II. Salvador, Vitória da Conquista, Jequié, Luís Eduardo Magalhães e Porto Seguro estão no da ABES e dos quatro VIKOR. Salvador, Vitória da Conquista, União dos Palmares e Jequié estão no da ABES e dos quatro TOPSIS.
- **PROMETHEE II e ABES.** Com pesos iguais, CRITIC e AHP Gaussiano, o PROMETHEE II fica mais perto da ABES (ρ de 0,95 a 0,99) do que os dois AHP. Com os pesos do AHP clássico, fica mais longe (ρ = 0,71).
- **VIKOR e ABES.** Com pesos iguais, o VIKOR fica muito perto da ABES (ρ = 0,977), porque sua parcela S praticamente a reproduz. Com os pesos do AHP clássico, é o mais distante (ρ = 0,705). Com CRITIC, o arrependimento individual R separa os municípios sem Destinação, que caem para a segunda metade do ranking.
- **TOPSIS e ABES.** Com pesos iguais e CRITIC, o TOPSIS fica a ρ de 0,91 a 0,93 da ABES, mais longe que o PROMETHEE II de mesmos pesos (e, com pesos iguais, também que o VIKOR), porque a normalização vetorial dá mais influência a Esgoto e Tratamento. Com o AHP Gaussiano, repete a soma ponderada (ρ = 0,990 e o mesmo Top 10). Com o AHP clássico, é o mais distante da ABES (ρ = 0,695). Com normalização min-max e pesos iguais, praticamente reproduz a ABES (ρ = 0,996).
- **Salvador como solução de compromisso.** Nos quatro esquemas, Salvador satisfaz as duas condições do VIKOR (vantagem e estabilidade aceitáveis) e é a solução única.
- **Pesos contra agregação.** No PROMETHEE II, trocar os pesos muda mais o ranking (ρ de 0,60 a 0,94 entre esquemas) do que trocar a soma ponderada pelo PROMETHEE II com os mesmos pesos (ρ de 0,90 a 0,97). O VIKOR repete o padrão, com faixa ainda mais larga entre esquemas (ρ de 0,48 a 0,95) e de 0,90 a 0,98 contra a soma ponderada e o PROMETHEE II de mesmos pesos. O TOPSIS também: de 0,45 a 0,95 entre esquemas e de 0,88 a 0,99 contra os outros três métodos com os mesmos pesos.


**Cobertura do desenho métodos × pesos.** Com o TOPSIS, 15 dos 16 rankings estão calculados em planilha. Falta a soma ponderada com os pesos CRITIC (normalização min-max), que ainda não tem planilha própria.

| Método de agregação | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| Soma ponderada | Calculado (é a ABES) | A calcular | Calculado (*AHP Gaussiano.ods*) | Calculado (*AHP Classico.ods*) |
| TOPSIS | Calculado (*TOPSIS.ods*) | Calculado | Calculado | Calculado |
| VIKOR | Calculado (*VIKOR.ods*) | Calculado | Calculado | Calculado |
| PROMETHEE II | Calculado (*PROMETHEE II.ods*) | Calculado | Calculado | Calculado |

Quatro verificações fortaleceriam essa comparação: testar como o ranking Clássico muda com pequenas variações nos julgamentos da matriz de Saaty, como o PROMETHEE II muda com q e p a ±50% e com outros limiares em Destinação (basta trocar os limiares na aba PARÂMETROS da planilha), como o VIKOR muda com v = 0,25 e v = 0,75 (célula B22 da aba PARÂMETROS de *VIKOR.ods*) e como o TOPSIS muda com a normalização min-max (célula B30 da aba PARÂMETROS de *TOPSIS.ods*).
