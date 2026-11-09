# Log de decisões metodológicas

Guilherme de Farias · iniciado em 9 nov. 2026

Este arquivo registra cada escolha metodológica do trabalho, com a justificativa e a data. Ele vira a seção de Metodologia do artigo e a base das respostas aos revisores. O [guia de escrita](guia_escrita.md) explica o porquê de cada regra; aqui fica só o que foi decidido.

**Congelamento antes da DRSAI.** Tudo o que está nas seções 1 a 7 foi fixado em 9 nov. 2026, antes de calcular qualquer correlação entre os rankings e a taxa de internações por DRSAI. Até essa data, a DRSAI aparece nas planilhas só como coluna copiada do arquivo do ABES, sem entrar em nenhum cálculo. Nenhum método, peso, limiar ou normalização será alterado depois do teste de validade externa. Se algum ajuste for inevitável (um erro de cálculo, por exemplo), ele entra na seção 9 com data, motivo e o resultado antes e depois da correção.

## 1. Bases de dados

| Base | Arquivo no repositório | Origem | Ano-base | Data de extração |
| --- | --- | --- | --- | --- |
| SINISA 2025: água, esgoto e resíduos sólidos | `dados/SINISA/2025/` | [gov.br/cidades, resultados SINISA 2025](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/resultados-sinisa-2025) | 2024 | 7 nov. 2026 |
| Ranking ABES 2026, Nordeste | `dados/ABES 2026/relatorio ABES 2026 NE.xlsx` | [rankingabes.abes-dn.org.br](https://rankingabes.abes-dn.org.br/relatorio.php) | 2024 | 7 nov. 2026 |

As duas bases foram baixadas em 7 nov. 2026, data informada pelo autor.

**Planilha de água retificada.** O IAG0001 vem de `SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`, a versão retificada publicada pelo Ministério das Cidades, e não da versão original.

**Filtro do Nordeste.** As planilhas do SINISA são nacionais; os municípios são filtrados pela coluna `Macrorregião` = `Nordeste` (1.794 municípios em AL, BA, CE, MA, PB, PE, PI, RN e SE).

## 2. Alternativas (amostra)

**Regra.** Entram os municípios que autodeclararam ao SINISA 2025 os quatro indicadores contabilizados (IAG0001, IES0001, IES2003 e IRS0001). Quem não tem algum deles fica fora. Município que não aparece numa planilha conta como ausente em todos os indicadores dela. "Zero declarado" é valor válido, e não ausência. Se o IRS3002 estiver ausente, assume-se disposição final inadequada (valor adaptado 0), e ele não conta como faltante.

**Resultado** (levantado com o notebook `01_filtragem_municipios.ipynb`, hoje fora de uso; a base de trabalho é `planilhas/relatorio ABES 2026 NE.ods`, com os mesmos 505 municípios):

| Indicadores faltantes (dos quatro contabilizados) | Municípios | Habilitados no ABES |
| --- | --- | --- |
| 0 | 505 | 505 |
| 1 | 76 | 0 |
| 2 | 675 | 0 |
| 3 | 420 | 0 |
| 4 | 118 | 0 |
| **Total** | **1.794** | **505** |

| Indicador | Municípios sem o indicador | Principal motivo |
| --- | --- | --- |
| IES2003 | 1.215 | Ausente da base de esgoto (641) ou sem atendimento por rede (570) |
| IES0001 | 1.212 | Idem |
| IRS0001 | 453 | Não respondeu ao formulário de resíduos |
| IAG0001 | 278 | Ausente da base de água (266) |

- Os 505 municípios completos são exatamente os 505 habilitados no ABES 2026, e a soma das notas brutas reproduz a pontuação do ABES em todos eles (diferença máxima de 0,00 ponto). A hipótese de trabalho do guia foi confirmada.
- Nenhum dos 505 tem o IRS3002 ausente, então a presunção de disposição inadequada não altera nenhum valor da amostra atual.
- Por UF: AL 22, BA 151, CE 95, MA 11, PB 65, PE 77, PI 6, RN 55 e SE 23.
- Os 1.289 de fora vão para o apêndice, com o perfil por UF e porte.
- A imputação de indicadores faltantes foi descartada. A amostra é só a dos completos.

## 3. Critérios

Os cinco indicadores do Ranking ABES, com as mesmas regras de tratamento, todos a maximizar. As notas brutas vão de 0 a 100.

| Código | Critério | Indicador SINISA | Unidade | Direção | Tratamento | Fonte |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | Água: atendimento da população total com rede de abastecimento | IAG0001 | % | max | Planilha retificada | SINISA 2025, Base Municipal de água |
| C2 | Esgoto: atendimento da população total com rede coletora | IES0001 | % | max | Nenhum | SINISA 2025, Base Municipal de esgoto |
| C3 | Tratamento: esgoto tratado referido à água consumida | IES2003 | % | max | Limitado a 100, como no ABES | SINISA 2025, Base Municipal de esgoto |
| C4 | Coleta: cobertura da população total com coleta de resíduos domiciliares | IRS0001 | % | max | Nenhum | SINISA 2025, indicadores de resíduos |
| C5 | Destinação: disposição final adequada de resíduos | IRS3002 adaptado | % | max | 100 − disposição inadequada; ausente = 0 | SINISA 2025, indicadores de resíduos |

A DRSAI não é critério. Ela só avalia os rankings depois de prontos (seção 7).

## 4. Parâmetros do PROMETHEE II

Decisão de 8 nov. 2026, confirmada em 9 nov. 2026 (planilha `planilhas/PROMETHEE II.ods`, aba PARÂMETROS).

| Critério | Função de preferência | q (indiferença) | p (preferência estrita) | Justificativa |
| --- | --- | --- | --- | --- |
| C1 Água | Linear (em V com indiferença) | 8,94 | 32,90 | Regra dos quartis: q = 1º e p = 3º quartil das diferenças absolutas entre os 254.520 pares ordenados |
| C2 Esgoto | Linear | 11,06 | 41,65 | Idem |
| C3 Tratamento | Linear | 7,24 | 50,10 | Idem |
| C4 Coleta | Linear | 6,40 | 31,39 | Idem |
| C5 Destinação | Em U | 5 | 5 | Exceção à regra dos quartis, que daria q = 0 e p = 100 (248 municípios com 0 e 236 com 100). Até 5 pontos é empate; acima disso, preferência total |

- As notas brutas entram sem normalização. Os limiares estão em pontos percentuais.
- **Função em U em Destinação, e não função nível.** A versão anterior do guia sugeria a função nível. Optou-se pela função em U porque o indicador é quase binário e só 21 municípios têm valores intermediários. Com q = p = 5, os que têm 95 a 99 (Massapê/CE com 98,3 e Saloá/PE com 96,8, por exemplo) empatam com os que têm 100, em vez de perderem para eles por inteiro, como aconteceria com a função usual. A troca da usual pela em U muda o ρ com a ABES em no máximo 0,003 e não altera nenhum Top 10.
- Os fluxos são calculados por critério e combinados com cada esquema de pesos, o que equivale à matriz π completa.
- O ranking de referência para GAIA, PROMETHEE I e SMAA-PROMETHEE é o PROMETHEE II com pesos CRITIC.

## 5. Parâmetros do VIKOR e do TOPSIS

| Método | Parâmetro | Valor adotado | Justificativa | Planilha |
| --- | --- | --- | --- | --- |
| VIKOR | v (peso da estratégia da maioria) | 0,5 | Valor usual da literatura e da apresentação da UNIFOR; S e R pesam o mesmo em Q | `VIKOR.ods`, PARÂMETROS, B22 |
| VIKOR | Ideal e anti-ideal | Melhor e pior valor observados nos 505 | Definição de Opricovic e Tzeng (2004); dᵢⱼ é o min-max invertido | `VIKOR.ods` |
| VIKOR | Condições C1 e C2 | DQ = 1/(m − 1) = 1/504 | Definição usual | `VIKOR.ods` |
| TOPSIS | Normalização | Vetorial (xᵢⱼ ÷ √Σx²ᵢⱼ) | A do TOPSIS original (Hwang e Yoon, 1981) | `TOPSIS.ods`, PARÂMETROS, B30 |
| TOPSIS | Ideais positivo e negativo | Melhor e pior valor ponderado observado | Definição usual | `TOPSIS.ods` |

Ordenação: menor Q é melhor no VIKOR; maior C* é melhor no TOPSIS.

## 6. Pesos e normalizações

### 6.1 Dicionário de pesos

Pesos na escala em que cada esquema é aplicado. As planilhas guardam os valores com todas as casas decimais; aqui eles aparecem com seis.

| Critério | Pesos iguais | CRITIC (min-max) | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| C1 Água | 0,200000 | 0,133648 | 0,084569 | 0,417419 |
| C2 Esgoto | 0,200000 | 0,155239 | 0,203834 | 0,160227 |
| C3 Tratamento | 0,200000 | 0,195575 | 0,348771 | 0,097476 |
| C4 Coleta | 0,200000 | 0,149318 | 0,067577 | 0,263374 |
| C5 Destinação | 0,200000 | 0,366220 | 0,295250 | 0,061504 |
| **Soma** | 1 | 1 | 1 | 1 |

Os mesmos quatro vetores alimentam a soma ponderada, o TOPSIS, o VIKOR e o PROMETHEE II (16 rankings).

### 6.2 Como cada esquema foi calculado

| Esquema | Natureza | Cálculo | Planilha |
| --- | --- | --- | --- |
| Pesos iguais | Neutro | 1/5 por critério | — |
| CRITIC | Objetivo (dispersão + conflito) | Desvio-padrão populacional de cada critério normalizado por min-max × Σ(1 − ρ) com os demais, dividido pela soma | `CRITIC.ods`, PESOS CRITIC |
| AHP Gaussiano | Objetivo (dispersão) | Desvio-padrão populacional ÷ média de cada critério normalizado pela soma, dividido pela soma dos fatores | `AHP Gaussiano.ods`, PESOS GAUSSIANOS |
| AHP clássico | Subjetivo (julgamento do autor) | Média geométrica das linhas da matriz de Saaty, normalizada | `AHP Classico.ods`, MATRIZ, PESOS E CONSISTÊNCIA |

O AHP clássico é o único esquema com pesos definidos por julgamento. Nenhum outro peso foi escolhido pelos autores.

### 6.3 Matriz de Saaty do AHP clássico

Preenchida pelo autor antes de qualquer correlação com a DRSAI. Não será alterada depois do teste.

| | Água | Esgoto | Tratamento | Coleta | Destinação | Peso |
| --- | --- | --- | --- | --- | --- | --- |
| **Água** | 1 | 3 | 4 | 2 | 5 | 0,4174 |
| **Esgoto** | 1/3 | 1 | 2 | 1/2 | 3 | 0,1602 |
| **Tratamento** | 1/4 | 1/2 | 1 | 1/3 | 2 | 0,0975 |
| **Coleta** | 1/2 | 2 | 3 | 1 | 4 | 0,2634 |
| **Destinação** | 1/5 | 1/3 | 1/2 | 1/4 | 1 | 0,0615 |

λ máx. = 5,0680; IC = 0,0170; IR (n = 5) = 1,12; RC = 0,0152 (consistente, abaixo de 0,10).

### 6.4 Normalização usada em cada célula

| Método | Pesos iguais | CRITIC | AHP Gaussiano | AHP clássico |
| --- | --- | --- | --- | --- |
| Soma ponderada | Notas brutas (é a regra do ABES) | Min-max | Pela soma | Pela soma |
| TOPSIS | Vetorial | Vetorial | Vetorial | Vetorial |
| VIKOR | Min-max invertido (dᵢⱼ) | Idem | Idem | Idem |
| PROMETHEE II | Nenhuma (notas brutas e limiares em pontos) | Idem | Idem | Idem |

- **Min-max no CRITIC (decisão de 8 nov. 2026).** Pior município = 0, melhor = 1, tanto no cálculo dos pesos quanto na soma ponderada. A normalização pela soma foi descartada para o CRITIC porque, com ela, o desvio-padrão de cada critério vira CV ÷ 505, o fator de conflito varia pouco (3,26 a 3,88), e o CRITIC reproduziria o AHP Gaussiano (ρ = 0,998 entre os dois rankings). O min-max é a normalização do artigo original (Diakoulaki et al., 1995) e mantém o peso na mesma escala em que ele é aplicado.
- **Pesos iguais na soma ponderada.** Aplicados às notas brutas, reproduzem exatamente a pontuação do ABES nos 505 municípios. Aplicar 20% aos valores normalizados pela soma não reproduz o ABES (ρ = 0,95), porque os 20% sobre as notas brutas equivalem, na escala pela soma, aos pesos abaixo.

### 6.5 Pesos na escala normalizada pela soma, para comparação

| Critério | ABES (equivalente) | AHP clássico | AHP Gaussiano | CRITIC convertido |
| --- | --- | --- | --- | --- |
| C1 Água | 26,7% | 41,7% | 8,5% | 17,7% |
| C2 Esgoto | 13,7% | 16,0% | 20,4% | 10,6% |
| C3 Tratamento | 9,5% | 9,7% | 34,9% | 9,2% |
| C4 Coleta | 31,3% | 26,3% | 6,8% | 28,5% |
| C5 Destinação | 18,7% | 6,2% | 29,5% | 34,0% |

Esta tabela só serve para comparar os esquemas entre si. Os pesos aplicados são os da seção 6.1.

## 7. Protocolo de validade externa com a DRSAI

Fixado em 9 nov. 2026, antes de qualquer cálculo com a DRSAI.

1. **Variável.** Taxa de internações por DRSAI informada no arquivo do ABES. Taxa 0,00 é tratada como ausente. Os números estão gravados como texto, com ponto de milhar e vírgula decimal: remove-se o ponto antes de trocar a vírgula.
2. **Amostra comum.** Os 360 dos 505 municípios com taxa válida, os mesmos para os 16 rankings.
3. **Associação.** ρ de Spearman entre a posição em cada ranking (1 = melhor) e a taxa. Espera-se ρ positivo entre posição e taxa (negativo entre pontuação e taxa).
4. **Diferença entre rankings.** Δρ entre pares de rankings, com intervalo de 95% por bootstrap percentil, reamostrando municípios com reposição 5.000 vezes, semente 20261109. O teste de Steiger (1980) para correlações dependentes entra como conferência.
5. **Controle mínimo.** ρ parcial de Spearman controlando por UF e porte. ρ dentro de BA, CE, PE, RN e PB e dentro de cada porte. AL, MA, SE e PI só entram na análise conjunta.
6. **Valores extremos.** Repetir sem os 5% de taxas mais altas.
7. **Número de rankings.** Os 16 do desenho, todos reportados. Nenhum ranking novo será acrescentado depois de ver a DRSAI.

## 8. Análises de robustez previstas

Parâmetros fixados em 9 nov. 2026. Cada variação é comparada com o ranking original pelo Kendall τ e, quando couber, pelo efeito no ρ com a DRSAI.

| Análise | Variação | Rankings afetados |
| --- | --- | --- |
| Limiares do PROMETHEE II | q e p de C1 a C4 multiplicados por 0,5 e por 1,5 | Os 4 PROMETHEE II |
| Limiar de Destinação | Função usual (q = p = 0) e função em U com q = p = 10 | Os 4 PROMETHEE II |
| v do VIKOR | 0,25 e 0,75 | Os 4 VIKOR |
| Normalização do TOPSIS | Min-max no lugar da vetorial | Os 4 TOPSIS |
| Julgamentos de Saaty | Cada julgamento acima da diagonal alterado em ±1 ponto da escala, mantendo RC < 0,10 | Os 4 rankings com pesos do AHP clássico |
| SMAA-PROMETHEE | 10.000 vetores de pesos uniformes no simplex, semente 20261109 | PROMETHEE II com CRITIC |
| Reversão de ordem | Retirar o melhor, o pior e um município aleatório (semente 20261109) | Os 16 |
| Retirada de estados | Retirar um estado de cada vez | Os 16 |

Robustez e validade externa são análises separadas. Nenhuma variação desta seção substitui os parâmetros principais das seções 4 a 6.

## 9. Alterações depois do congelamento

Nenhuma até agora.
