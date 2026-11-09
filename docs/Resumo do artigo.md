# Resumo do artigo: roteiro para o Rii Forum 2027

Guilherme de Farias · 9 nov. 2026

Roteiro para você escrever o resumo do formulário do Rii Forum 2027 (prazo: 15/11/2026). Segue a estrutura do [Guia de escrita](Guia%20de%20escrita.md): sete movimentos, uma ou duas frases cada, sem citações. Os números vêm do [parecer técnico](Parecer%20técnico%20dos%20métodos%20multicritério.md).

## O que o formulário pede

- **Resumo:** no máximo 300 palavras, em inglês ([formulário](https://rii-forum.org/abstract-submission-form/)). Mire em 230 a 270, para ter folga.
- **Título** e **palavras-chave** (o formulário não diz quantas; o guia sugere 5 a 6, sem repetir palavras do título).
- **Trilha:** *Politics, Public Policy, Democracy and Regulation* (recomendada) ou *Research Methods and Research Design*.

## Estrutura

| # | Movimento | Palavras | Pergunta que a frase responde |
| --- | --- | --- | --- |
| 1 | Contexto | 35–45 | Por que rankings de saneamento importam, e de que escolhas eles dependem? |
| 2 | Lacuna | 20–30 | O que não se sabe sobre essas escolhas? |
| 3 | Objetivo | 35–45 | Qual é a pergunta do estudo? |
| 4 | Método | 60–80 | Quem, com quais dados, quais métodos, como foi validado? |
| 5 | Resultados | 60–80 | O que mudou no ranking, e o que aconteceu com a DRSAI? |
| 6 | Implicação | 15–25 | O que um gestor ou quem faz o ranking deve tirar disso? |
| 7 | Contribuição | 15–25 | O que o estudo oferece de método para outros pesquisadores? |

### 1. Contexto

- Diga que rankings municipais de saneamento, como o Ranking ABES, orientam atenção pública e investimento.
- Diga que eles dependem de escolhas de pesos, normalização e regra de agregação.
- Se quiser um número: 505 municípios do Nordeste habilitados no ABES 2026, ou o prazo de universalização da Lei 14.026/2020 (2033).

### 2. Lacuna

- Uma frase só: não se sabe quanto essas escolhas mudam a ordenação, nem se alguma gera um ranking mais coerente com a saúde.

### 3. Objetivo

- Reescreva a pergunta principal do README numa frase: em que medida o método multicritério altera a ordenação, e qual ordenação se associa mais fortemente às internações por DRSAI.
- Defina DRSAI por extenso na primeira vez (*diseases related to inadequate environmental sanitation*).

### 4. Método

Inclua, nesta ordem:

- **Alternativas e dados:** 505 municípios do Nordeste, cinco indicadores do ABES, SINISA 2025.
- **Desenho 4 × 4:** quatro esquemas de pesos (iguais, CRITIC, AHP gaussiano, AHP clássico) × quatro métodos (soma ponderada, TOPSIS, VIKOR, PROMETHEE II) = 16 rankings.
- **Validação:** Spearman com a taxa de DRSAI em 360 municípios, intervalos bootstrap para as diferenças entre rankings, controle por estado e porte.
- **Rigor:** parâmetros fixados antes do teste com a DRSAI. É curto e diferencia o trabalho.

### 5. Resultados

Escolha dois ou três destes. Comece pelo que responde à pergunta.

| Achado | Número |
| --- | --- |
| Os pesos mudam o ranking mais que o método | ρ médio de 0,78 entre esquemas de pesos e de 0,95 entre métodos |
| O mesmo achado, por município | Trocar os pesos move em média 132 posições; trocar o método, 62 |
| Mudança em relação ao ranking oficial | De 50 a 300 municípios mudam de quartil, conforme o ranking |
| O topo é estável | Salvador é o 1º nos 16 rankings |
| Associação com a DRSAI é fraca | ρ de −0,11 a −0,23 nos 16 rankings |
| Nenhum supera o oficial | Nenhum ranking se associa significativamente mais que o ABES; sete se associam significativamente menos |
| O controle reduz a associação | ρ parcial de −0,04 a −0,14 com controle por estado e porte |
| Compensação não explica | O grau de compensação não ordena a associação; o pior indicador não se associa mais que a média |

### 6. Implicação

- Uma frase para quem faz ou usa rankings. Por exemplo, que a definição dos pesos merece mais escrutínio que a escolha do método.

### 7. Contribuição

- Uma frase sobre o desenho: separar o efeito dos pesos do da agregação e testar os rankings contra um desfecho externo.

## Cuidados

- **Associação, não efeito.** Escreva "se associa", "é mais coerente com"; nunca "o melhor método" ou "reduz internações".
- **Resultado com número.** Todo resultado leva um número; nenhum fica só como "difere" ou "é fraco".
- **Sem robustez por enquanto.** Ela ainda não rodou. Se rodar antes de 15/11, cabe uma frase no fim dos resultados.
- **Sem unidade da taxa de DRSAI.** O resumo não precisa dela, então não depende da resposta da ABES.
- **Teste final do guia:** dê título e resumo a alguém da área e peça o achado em uma frase. Se a pessoa descrever o método, reescreva os resultados.

## Título

O guia sugere 12 a 16 palavras, com a fórmula *[o que o método faz] + [objeto] + [contexto] + [sinal metodológico]*. Decida se o título anuncia o achado ("os pesos importam mais que o método") ou a pergunta ("o método de agregação importa para a saúde?"). Com o achado já em mãos, um título que o anuncia tende a funcionar melhor.

## Proposta escrita a partir do roteiro

### Títulos

| | Inglês | Português |
| --- | --- | --- |
| **A (achado, recomendado)** | *Weights matter more than methods: multicriteria rankings of municipal sanitation and sanitation-related hospitalisations in Northeast Brazil* | *Os pesos importam mais que o método: rankings multicritério de saneamento municipal e internações por DRSAI no Nordeste brasileiro* |
| **B (pergunta)** | *Does the aggregation method matter for health? Comparing multicriteria rankings of sanitation against sanitation-related hospitalisations in Northeast Brazil* | *O método de agregação importa para a saúde? Rankings multicritério de saneamento comparados às internações por DRSAI no Nordeste brasileiro* |
| **C (política pública)** | *Same data, different priorities: how weighting and aggregation shape a public sanitation ranking in Northeast Brazil* | *Mesmos dados, prioridades diferentes: como pesos e agregação moldam um ranking público de saneamento no Nordeste brasileiro* |

O título A anuncia o achado principal. O B é o que estava no guia e funciona se você preferir não adiantar o resultado. O C combina com a trilha de políticas públicas, mas não menciona a saúde.

### Resumo em inglês (270 palavras)

As Brazil approaches its 2033 legal deadline for universal sanitation, municipal rankings such as the ABES Sanitation Universalisation Ranking steer public attention and investment, yet the choice of multicriteria method behind them (weights, normalisation and aggregation) is seldom treated as a factor that shapes the result. It is unclear how much this choice changes the ordering, or whether any alternative yields rankings more consistent with health outcomes. This study asks to what extent the multicriteria method changes the ranking of municipalities in Northeast Brazil, and which ranking is most strongly associated with hospitalisations for diseases related to inadequate environmental sanitation (DRSAI). The 505 municipalities eligible for the 2026 ABES ranking were ranked on its five indicators (SINISA 2025) by crossing four weighting schemes (equal, CRITIC, Gaussian AHP and classic AHP) with four aggregation methods (weighted sum, TOPSIS, VIKOR and PROMETHEE II). With all parameters fixed in advance, the 16 rankings were correlated (Spearman) with the DRSAI rate in 360 municipalities, using bootstrap intervals for the differences. Weights changed the ordering more than aggregation did (mean ρ of 0.78 across weighting schemes and 0.95 across methods), and up to 300 municipalities changed quartile relative to the official ranking. The association with DRSAI was weak in every ranking (ρ from −0.11 to −0.23) and shrank after controlling for state and municipality size. No ranking was significantly more associated than the official one, and seven were significantly less. For public policy, the choice of weights deserves more scrutiny than the choice of method. Methodologically, the study offers a design that separates weighting from aggregation effects and tests rankings against an external health outcome.


**Keywords:** decision aid; PROMETHEE; TOPSIS; VIKOR; AHP; external validity

### Resumo em português (287 palavras)

Com o prazo legal de universalização do saneamento fixado em 2033, rankings municipais como o Ranking ABES da Universalização do Saneamento orientam a atenção pública e o investimento, mas a escolha do método multicritério que os produz (pesos, normalização e agregação) raramente é tratada como um fator que altera o resultado. Não se sabe quanto essa escolha altera a ordenação nem se alguma alternativa gera rankings mais coerentes com a saúde. Este estudo pergunta em que medida o método multicritério altera a ordenação dos municípios do Nordeste brasileiro e qual ordenação se associa mais fortemente às internações por doenças relacionadas ao saneamento ambiental inadequado (DRSAI). Os 505 municípios habilitados no Ranking ABES 2026 foram ordenados pelos seus cinco indicadores (SINISA 2025), cruzando quatro esquemas de pesos (iguais, CRITIC, AHP gaussiano e AHP clássico) com quatro métodos de agregação (soma ponderada, TOPSIS, VIKOR e PROMETHEE II). Com os parâmetros fixados antes, os 16 rankings foram correlacionados (Spearman) com a taxa de DRSAI em 360 municípios, com intervalos bootstrap para as diferenças. Os pesos alteraram a ordenação mais que a agregação (ρ médio de 0,78 entre esquemas de pesos e de 0,95 entre métodos), e até 300 municípios mudaram de quartil em relação ao ranking oficial. A associação com a DRSAI foi fraca em todos os rankings (ρ de −0,11 a −0,23) e diminuiu com o controle por estado e porte. Nenhum ranking se associou significativamente mais que o oficial, e sete se associaram significativamente menos. Para a política pública, a definição dos pesos merece mais escrutínio que a escolha do método. Como contribuição metodológica, o estudo propõe um desenho que separa o efeito dos pesos do efeito da agregação e avalia rankings contra um desfecho de saúde externo.


**Palavras-chave:** apoio à decisão; PROMETHEE; TOPSIS; VIKOR; AHP; validade externa

### Correspondência com o roteiro

| Movimento | Começa em (inglês) |
| --- | --- |
| 1. Contexto | "As Brazil approaches..." |
| 2. Lacuna | "It is unclear..." |
| 3. Objetivo | "This study asks..." |
| 4. Método | "The 505 municipalities..." e "With all parameters fixed..." |
| 5. Resultados | "Weights changed..." até "...seven were significantly less." |
| 6. Implicação | "For public policy..." |
| 7. Contribuição | "Methodologically..." |

As palavras-chave não repetem palavras dos títulos A e B, como pede o guia. Com o título C, troque *decision aid* por *sanitation-related diseases*.
