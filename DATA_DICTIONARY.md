# Data Dictionary

*Companion to [README.en.md](README.en.md). The spreadsheets, notebooks and internal documents are in Portuguese; this file translates every file, sheet, column, indicator and label needed to read them.*

Number format: the `.ods` spreadsheets display numbers in the locale they were opened in; the raw ABES file (`dados/ABES 2026/relatorio ABES 2026 NE.xlsx`) stores them as text in Brazilian format (`10.220,55` = 10220.55).

## 1. Decision matrix

File: `planilhas/Relatorio ABES 2026 NE.ods`, sheet `Relatório` (report). One row per municipality, 505 rows. The same table is copied as the first sheet (`PLANILHA ABES`) of every method spreadsheet and is the only input of the notebooks.

| Column (PT) | English | Type / values |
| --- | --- | --- |
| `Município` | Municipality name | Text |
| `Capital` | State capital | `Sim` (yes, 9) / `Não` (no, 496) |
| `UF` | State (*unidade federativa*) | AL, BA, CE, MA, PB, PE, PI, RN, SE |
| `Porte` | Size class, as assigned by ABES | `Grande porte` (large, 60) / `Pequeno e médio porte` (small and medium, 445) |
| `Categoria` | ABES performance category | `Compromisso com a universalização` (commitment to universal coverage, 7), `Empenho para universalização` (effort towards universal coverage, 367), `Primeiros passos para a universalização` (first steps towards universal coverage, 131) |
| `IAG0001` | C1 Water: share of total population served by the water supply network | %, 0–100, maximize |
| `IES0001` | C2 Sewage: share of total population served by the sewage collection network | %, 0–100, maximize |
| `IES2003` | C3 Treatment: treated sewage relative to water consumed, capped at 100 | %, 0–100, maximize |
| `IRS0001` | C4 Collection: share of total population covered by household waste collection | %, 0–100, maximize |
| `IRS3002` | C5 Disposal: adequate final disposal of solid waste (100 − inadequate disposal; missing = 0) | %, 0–100, maximize |
| `Pontuação total` | ABES total score = sum of the five indicators | 0–500 |
| `Taxa de Internações por DRSAI` | Hospitalization rate for diseases related to inadequate environmental sanitation, as published by ABES (unit as defined by ABES) | Number; `0` means not reported and is treated as missing (145 of 505) |

The raw ABES file has the same columns plus `Plano de saneamento` (municipal sanitation plan), which is not used, for all 1,794 Northeast municipalities. Its extra `Categoria` value `Não habilitado` means not eligible (missing indicators); those rows are excluded.

### Indicator and criterion names

The spreadsheets label criteria as `<short name> — <SINISA code>`:

| Label in files | Criterion | English short name |
| --- | --- | --- |
| `Água — IAG0001` | C1 | Water |
| `Esgoto — IES0001` | C2 | Sewage |
| `Tratamento — IES2003` | C3 | Treatment |
| `Coleta — IRS0001` | C4 | Collection |
| `Destinação — IRS3002` | C5 | Disposal |

## 2. Spreadsheets (`planilhas/`)

Common elements: `PLANILHA ABES` is the decision matrix (section 1). `ETAPA n` = step n, `COMPARAÇÃO n` = comparison n. Columns marked `(auxiliar)` are helper columns for lookups and tie-breaking. `Linha na base` = row number in the decision matrix. `Conferência` = check column (`SIM` = passes). `Posição` = rank position (1 = best). `Posição no ABES` = rank in the ABES ranking. `Ordem (desempate)` / `Ordem única` = unique order after tie-breaking.

### `AHP Classico.ods` (classical AHP)

| Sheet | English | Contents |
| --- | --- | --- |
| `PLANILHA ABES` | ABES sheet | Decision matrix |
| `MATRIZ, PESOS E CONSISTÊNCIA` | Matrix, weights and consistency | Step 1: Saaty pairwise comparison matrix (filled in by the authors), row geometric means (`Média geométrica`), weights (`Peso`), A × w, individual λ, λmax, consistency index (CI), random index (RI = 1.12) and consistency ratio (CR = 0.0152) |
| `NORMALIZAÇÃO PELA SOMA` | Sum normalization | Step 2: each indicator divided by its column sum over the 505 municipalities |
| `PONTUAÇÃO E RANKING` | Score and ranking | Step 3: weighted normalized values, `Pontuação AHP` (AHP score = Σ normalized value × weight), position |
| `CORRELAÇÃO AHP × ABES` | Correlation AHP × ABES | Step 4: Spearman ρ, t statistic, p-value, Kendall τ-b, concordant − discordant pairs (S), z, p-value, with a verbal interpretation (`Interpretação`) |
| `TOP 10 AHP × ABES` | Top 10 AHP × ABES | Step 5: the ten best-ranked municipalities in each ranking |

### `AHP Gaussiano.ods` (Gaussian AHP)

| Sheet | English | Contents |
| --- | --- | --- |
| `ESTATÍSTICAS` | Statistics | Step 1: sum, mean, population standard deviation (`Desvio-padrão (pop.)`), min, max and coefficient of variation (`Coef. variação`) of each indicator |
| `NORMALIZAÇÃO PELA SOMA` | Sum normalization | Step 2 |
| `PESOS GAUSSIANOS` | Gaussian weights | Step 3: normalized mean and std. dev., Gaussian factor (std. dev. / mean), weight |
| `PONTUAÇÃO E RANKING` | Score and ranking | Step 4: `norm. × peso` (normalized value × weight) per criterion, `Pontuação AHP Gaussiano`, position, ABES position |
| `TOP 10 GAUSSIANO × ABES` | Top 10 | Step 5 |
| `CORRELAÇÃO GAUSSIANO × ABES` | Correlation | Step 6: as in the classical AHP file |

### `CRITIC.ods`

| Sheet | English | Contents |
| --- | --- | --- |
| `ESTATÍSTICAS` | Statistics | Step 1: descriptive statistics and range (`Amplitude`) |
| `NORMALIZAÇÃO MIN-MAX` | Min-max normalization | Step 2: worst municipality = 0, best = 1 |
| `NORMALIZAÇÃO PELA SOMA` | Sum normalization | Step 3: only for comparison with the AHP weights |
| `CORRELAÇÃO ENTRE CRITÉRIOS` | Correlation between criteria | Step 4: Pearson correlation matrix of the five criteria |
| `PESOS CRITIC` | CRITIC weights | Step 5: std. dev. of normalized criterion, conflict Σ(1 − r) (`Conflito`), information content C = std. dev. × conflict (`Informação C`), weight; side table comparing all weighting schemes on a common scale |
| `PONTUAÇÃO E RANKING` | Score and ranking | Step 6: weighted sum with CRITIC weights on min-max values (`min-max × peso`), position, ABES position |

### `PROMETHEE II.ods`

| Sheet | English | Contents |
| --- | --- | --- |
| `PARÂMETROS` | Parameters | The four weight vectors (`Pesos iguais`, `CRITIC`, `AHP Gaussiano`, `AHP clássico`) with their source (`Origem dos pesos`), preference function per criterion and thresholds q (indifference) and p (preference) |
| `FLUXOS POR CRITÉRIO` | Flows per criterion | Steps 1, 2, 4: for each municipality and criterion, leaving flow φ⁺ⱼ (`fluxo de saída`), entering flow φ⁻ⱼ (`fluxo de entrada`) and net flow φⱼ (`fluxo líquido`) |
| `EXEMPLO PAR A PAR` | Pairwise example | Steps 1–3 for two municipalities chosen in the yellow cells: difference d(a,b), preference P(a,b), aggregated preference π |
| `FLUXOS GLOBAIS` | Global flows | Steps 4, 5: φ⁺, φ⁻, φ and position under each weighting scheme; checks that Σφ = 0 and −1 ≤ φ ≤ 1 |
| `RANKING` | Ranking | Step 6: ranking by net flow φ under each weighting scheme, with ABES position |
| `CORRELAÇÃO` | Correlation | Comparison 1: each PROMETHEE II ranking vs. ABES and vs. the weighted sum with the same weights: n, Spearman ρ, t, p, Kendall τ-b, S, z, p, mean displacement in positions (`Deslocamento médio`); ρ matrix between the four PROMETHEE II rankings |
| `TOP 10` | Top 10 | Comparison 2 |

### `TOPSIS.ods`

| Sheet | English | Contents |
| --- | --- | --- |
| `PARÂMETROS` | Parameters | Weight vectors, criterion direction, normalization switch (cell B30: vector or min-max) |
| `MATRIZ NORMALIZADA` | Normalized matrix | Step 2: rᵢⱼ = xᵢⱼ / √Σxᵢⱼ² (`notas brutas` = raw scores) |
| `MATRIZ PONDERADA` | Weighted matrix | Step 3: vᵢⱼ = wⱼ · rᵢⱼ for each weighting scheme |
| `SOLUÇÕES IDEAIS` | Ideal solutions | Step 4: positive ideal A⁺ (best vᵢⱼ) and negative ideal A⁻ (worst vᵢⱼ) |
| `DISTÂNCIAS E PROXIMIDADE` | Distances and closeness | Steps 5–7: D⁺ (`distância ao ideal positivo`), D⁻ (`distância ao ideal negativo`), C* (`proximidade relativa`, relative closeness) and position |
| `RANKING` | Ranking | Step 8: ranking by C* under each weighting scheme |
| `CORRELAÇÃO` | Correlation | As in PROMETHEE II, also against PROMETHEE II and VIKOR |
| `TOP 10` | Top 10 | Comparison 2 |

### `VIKOR.ods`

| Sheet | English | Contents |
| --- | --- | --- |
| `PARÂMETROS` | Parameters | Weight vectors, v = 0.5, best and worst observed values |
| `DISTÂNCIAS NORMALIZADAS` | Normalized distances | Step 3: dᵢⱼ = distance to the best value, 0 = best, 1 = worst |
| `DESVANTAGENS PONDERADAS` | Weighted disadvantages | Step 4: tᵢⱼ = wⱼ · dᵢⱼ for each weighting scheme |
| `ÍNDICES S, R E Q` | S, R and Q indices | Steps 5–7: S (`desvantagem agregada`, group utility), R (`arrependimento individual`, individual regret), Q (`compromisso`, compromise index) and positions by each |
| `RANKING` | Ranking | Step 8: ranking by Q (lower is better) under each weighting scheme |
| `CONDIÇÕES C1 E C2` | Conditions C1 and C2 | Steps 9, 10: acceptable advantage (Q(a²) − Q(a¹) ≥ DQ = 1/(m − 1)) and acceptable stability |
| `CORRELAÇÃO` | Correlation | As in PROMETHEE II |
| `TOP 10` | Top 10 | Comparison 2 |

## 3. Notebook labels

The notebooks print tables with Portuguese labels. Ranking names follow the pattern `<method> | <weighting scheme>`, for example `VIKOR | Pesos iguais`. `Soma ponderada | Pesos iguais` is the ABES ranking.

| Portuguese | English |
| --- | --- |
| `Soma ponderada` | Weighted sum |
| `Pesos iguais` | Equal weights |
| `AHP clássico` / `AHP Gaussiano` | Classical AHP / Gaussian AHP |
| `Método` / `Pesos` / `Ranking` | Method / Weights / Ranking |
| `Compensação`: `Total`, `Parcial`, `Limitada` | Compensation: full, partial, limited |
| `Pontuação` / `Posição` | Score / Rank position |
| `Melhor` / `Pior` | Best / Worst |
| `Mesma agregação, pesos diferentes` | Same aggregation, different weights |
| `Mesmos pesos, agregação diferente` | Same weights, different aggregation |
| `Pesos e agregação diferentes` | Different weights and aggregation |
| `ρ com o ABES` / `τ com o ABES` | ρ / τ with ABES |
| `Spearman ρ com a taxa de DRSAI` | Spearman ρ with the DRSAI rate |
| `IC 2,5%` / `IC 97,5%` / `IC exclui 0` | 2.5% / 97.5% bootstrap CI bounds / CI excludes zero |
| `Δρ` | Difference in ρ between two rankings (ρ(A) − ρ(B); negative means A is more strongly associated with DRSAI) |
| `ρ entre A e B` | ρ between rankings A and B (used in Steiger's test) |
| `Steiger z` / `Steiger p` | Steiger's test statistic and p-value |
| `Média do método` / `Média dos pesos` | Mean over methods / mean over weighting schemes |
| `Δρ contra os demais` | Δρ against the mean of the others |
| `Parcial UF + porte` | Partial ρ controlling for state and size class |
| `Todos` | All municipalities |
| `ρ sem os 5% mais altos` | ρ without the top 5% of DRSAI rates |
| `Desigualdade (DP)` | Inequality: standard deviation of the five indicators |
| `Pior indicador` | Worst indicator (minimum of the five) |
| `Zeros` | Number of indicators equal to 0 |
| `Amplitude: método` / `Amplitude: pesos` / `Amplitude: 16 rankings` | Range of positions across methods (same weights) / across weighting schemes (same method) / across all 16 rankings |
| `Δ médio, sem zeros` / `Δ médio, 0 em Tratamento` / `Δ médio, 0 em Destinação` | Mean change in position vs. the weighted sum with the same weights, for municipalities with no zeros / zero Treatment / zero Disposal (positive = falls) |
| `ρ(Δ, zeros)` / `ρ(Δ, desigualdade)` | Spearman ρ between position change and number of zeros / inequality |
| `Quartil ABES` / `Quartil VIKOR` / `Δ quartil` | Quartile (1 = best 25%) in ABES / in VIKOR, and the change |
| `Sobe` / `Desce` / `Mantém` | Moves up / moves down / stays |
| `Indicador decisivo` | Decisive indicator: the one defining the municipality's VIKOR regret R |
| `Melhor posição` / `Pior posição` / `Melhor ranking` / `Pior ranking` | Best / worst position and the ranking where it occurs |

## 4. Python module `mcda.py`

| Name | English |
| --- | --- |
| `CRITERIOS`, `NOMES` | Criterion codes and Portuguese short names |
| `ESQUEMAS`, `METODOS` | Weighting schemes and aggregation methods, in the order used throughout |
| `SAATY`, `IR` | Saaty matrix of the classical AHP and random index table |
| `Q`, `P`, `FUNCAO` | PROMETHEE II indifference and preference thresholds, and preference function per criterion (`linear` or `U`) |
| `V_VIKOR` | VIKOR v parameter (0.5) |
| `ler_base(raiz)` | Read the decision matrix from the repository root |
| `minmax(X)` | Min-max normalization |
| `pesos_saaty`, `pesos_gaussianos`, `pesos_critic`, `pesos` | Classical AHP weights and CR; Gaussian AHP weights; CRITIC weights; all four weight vectors |
| `soma_ponderada`, `topsis`, `vikor_q`, `fluxos_por_criterio` | Weighted sum; TOPSIS closeness; VIKOR Q; PROMETHEE per-criterion flows |
| `rankings(X, ...)` | Scores of all 16 rankings (always "higher is better"; VIKOR is returned as −Q) |
| `posicoes(pontuacao)` | Convert scores to positions (1 = best; tied municipalities share the better position) |

## 5. Raw data folders (`dados/`)

| Portuguese | English |
| --- | --- |
| `abastecimento de água` / `Água` / `AGUA` | Water supply |
| `esgotamento sanitário` / `Esgoto` / `ESGOTO` | Sewage |
| `resíduos sólidos` / `RESIDUOS` | Solid waste |
| `Base Municipal` | Municipal-level data (used here) |
| `Locais e Regionais` | By local and regional service provider |
| `Consolidado UF_MR_BR` | Aggregated by state, macro-region and Brazil |
| `Indicadores` / `Informações` | Indicators / raw reported data |
| `Gestão Técnica` / `Gestão Administrativa e Financeira` | Technical management / administrative and financial management |
| `Retificação` | Rectified (corrected) release |
| `Glossário de Indicadores` / `Glossário de Informações` | Official glossaries of indicators and of raw data items (PDF, Portuguese) |
| `Relatório` | Official report |
| `Atestado de Adimplência` | Link to the compliance certificate page |
| `Macrorregião` | Macro-region column; filter on `Nordeste` (Northeast) |
