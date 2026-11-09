# Ranking Northeast Brazilian Municipalities on Sanitation with Multi-Criteria Methods

*[Versão em português](README.md)*

This repository ranks the municipalities of Northeast Brazil (the states of AL, BA, CE, MA, PB, PE, PI, RN and SE) by their performance in basic sanitation, and measures how much the choice of multi-criteria decision-making (MCDM) method changes that ranking. The same five indicators used by the [ABES Sanitation Universalization Ranking 2026](https://rankingabes.abes-dn.org.br/relatorio.php) are aggregated by four methods (weighted sum, which is the ABES rule, TOPSIS, VIKOR and PROMETHEE II), each with four weighting schemes (equal weights, CRITIC, Gaussian AHP and classical AHP). The 16 resulting rankings are compared with each other and with the hospitalization rate for DRSAI (*doenças relacionadas ao saneamento ambiental inadequado*, diseases related to inadequate environmental sanitation), to find which ordering is most strongly associated with health outcomes.

**Main research question:** to what extent does the choice of MCDM aggregation method (ABES weighted sum, classical AHP, Gaussian AHP, TOPSIS, VIKOR or PROMETHEE II) change the ordering of Northeast Brazilian municipalities on sanitation, and which ordering is most strongly associated with the DRSAI hospitalization rate, accounting for differences between states and municipality size? The degree of compensation of each method (how much a good indicator offsets a poor one) is a secondary question used to explain the differences.

The study is being prepared as a paper for the [Rii Forum 2027](https://rii-forum.org) (Rome, 6 and 8–9 April 2027), with proceedings published by Springer.

**Language note.** The spreadsheets, notebooks and internal documents (`docs/`) are written in Portuguese. This README and the [data dictionary](DATA_DICTIONARY.md) translate every file, sheet, column, indicator and label needed to read and reproduce the work.

## Status

Work in progress. The decision matrix, the 16 rankings, the external validity test against DRSAI (notebook 02) and the compensation and profile analysis (notebook 03) are done. All methodological choices were frozen in the decision log (`docs/Log de decisoes.md`) on 9 Nov 2026, before any correlation with DRSAI was computed. The robustness analyses (SMAA, threshold and parameter sensitivity, rank reversal, leave-one-state-out) are not yet done.

## Method

**Alternatives.** The 505 Northeast municipalities that self-reported to SINISA 2025 all four scored indicators (IAG0001, IES0001, IES2003 and IRS0001). These are exactly the 505 municipalities that ABES 2026 classifies as eligible ("habilitados"); the other 1,289 of the region's 1,794 municipalities are excluded. Missing indicators are not imputed. If IRS3002 were missing it would be set to 0 (inadequate disposal), but none of the 505 is in that situation. By state: AL 22, BA 151, CE 95, MA 11, PB 65, PE 77, PI 6, RN 55, SE 23.

**Criteria.** The five ABES indicators, all to be maximized, on a 0–100 scale (percent).

| Code | SINISA indicator | Short name (PT) | Description |
| --- | --- | --- | --- |
| C1 | IAG0001 | Água | Share of the total population served by the water supply network |
| C2 | IES0001 | Esgoto | Share of the total population served by the sewage collection network |
| C3 | IES2003 | Tratamento | Treated sewage relative to water consumed (capped at 100%, as in ABES) |
| C4 | IRS0001 | Coleta | Share of the total population covered by household solid waste collection |
| C5 | IRS3002 (adapted) | Destinação | Adequate final disposal of solid waste (100 − share disposed inadequately) |

The unweighted sum of the five raw scores reproduces the ABES total score ("Pontuação total") for all 505 municipalities.

**Design: 4 aggregation methods × 4 weighting schemes = 16 rankings.**

| Aggregation method | Compensation | Normalization | Score (better is) |
| --- | --- | --- | --- |
| Weighted sum | Full | Raw scores (equal weights, which reproduces ABES), min-max (CRITIC), sum normalization (both AHP schemes) | Higher |
| TOPSIS | Full | Vector normalization | Closeness coefficient C*, higher |
| VIKOR (v = 0.5) | Partial | Inverted min-max distance to the best observed value | Compromise index Q, lower |
| PROMETHEE II | Limited | None (raw scores; thresholds in percentage points) | Net flow φ, higher |

| Weighting scheme | Nature | How it is computed | Water | Sewage | Treatment | Collection | Disposal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Equal weights | Neutral | 1/5 each | 20.0% | 20.0% | 20.0% | 20.0% | 20.0% |
| CRITIC | Objective (dispersion and conflict) | Std. dev. of min-max-normalized criterion × Σ(1 − r) with the other criteria, normalized to sum to 1 | 13.4% | 15.5% | 19.6% | 14.9% | 36.6% |
| Gaussian AHP | Objective (dispersion) | Coefficient of variation of each sum-normalized criterion, normalized to sum to 1 | 8.5% | 20.4% | 34.9% | 6.8% | 29.5% |
| Classical AHP | Subjective (authors' judgment) | Geometric mean of the rows of a Saaty pairwise comparison matrix (CR = 0.0152) | 41.7% | 16.0% | 9.7% | 26.3% | 6.2% |

The two AHP variants enter as weighting schemes followed by a weighted sum, not as separate aggregation methods, so that the effect of aggregation is separated from the effect of the weights. In the weighted-sum row, the Gaussian AHP and classical AHP columns are the "Gaussian AHP" and "classical AHP" methods of the literature. Classical AHP is the only scheme whose weights express the authors' priorities; all others are derived from the data. Because 20% applied to sum-normalized values does not reproduce ABES (Spearman ρ = 0.95), comparisons of weights in the Portuguese documents use the ABES-equivalent weights on the sum-normalized scale (26.7%, 13.7%, 9.5%, 31.3% and 18.7%).

**Method parameters** (fixed before the DRSAI test; see section 4 and 5 of the decision log):

- **PROMETHEE II.** Linear preference function for C1–C4, with the indifference threshold q and preference threshold p set to the 1st and 3rd quartiles of all pairwise differences (q = 8.94, 11.06, 7.24, 6.40; p = 32.90, 41.65, 50.10, 31.39 percentage points). C5 is nearly binary and uses the U-shape (quasi-criterion) function with q = p = 5. Flows are computed per criterion and then weighted, which is equivalent to the full preference matrix π.
- **VIKOR.** Group utility S = Σ wⱼ·dᵢⱼ, individual regret R = max wⱼ·dᵢⱼ, compromise index Q with v = 0.5. Acceptance conditions C1 (acceptable advantage, DQ = 1/504) and C2 (acceptable stability) are checked for each weighting scheme.
- **TOPSIS.** Vector normalization, weighted matrix, positive and negative ideals from the best and worst observed weighted values, Euclidean distances D⁺ and D⁻, closeness C* = D⁻ / (D⁺ + D⁻). Min-max normalization is kept as a robustness option.

**External validity.** Spearman correlation between each ranking and the DRSAI hospitalization rate reported by ABES, on the 360 of the 505 municipalities with a valid rate (a rate of 0.00 is treated as missing). Differences between rankings (Δρ) are tested with 95% percentile bootstrap intervals (5,000 resamples of municipalities, seed 20261109) and checked with Steiger's (1980) test for dependent correlations. As a minimal control, the association is recomputed as a partial Spearman correlation controlling for state and size class, within the states with enough observations (BA, CE, PE, RN, PB), within each size class, and without the top 5% of rates. DRSAI never enters any ranking as a criterion. Results are read as associations, not causal effects.

**Planned robustness analyses** (decision log, section 8): PROMETHEE thresholds ×0.5 and ×1.5; disposal threshold variants; VIKOR v = 0.25 and 0.75; TOPSIS with min-max normalization; ±1 step changes to each Saaty judgment while keeping CR < 0.10; SMAA-PROMETHEE with 10,000 uniform weight vectors; rank reversal; leave-one-state-out.

## Repository structure

```text
.
├── README.md                     Main README (Portuguese)
├── README.en.md                  This file
├── DATA_DICTIONARY.md            English dictionary of files, sheets, columns, indicators and labels
├── requirements.txt              Pinned Python dependencies for the notebooks
├── docs/                         Internal documents (Portuguese)
│   ├── Log de decisoes.md            Decision log: data sources, sample, criteria, parameters, weights,
│   │                                 DRSAI protocol and robustness plan, frozen before the DRSAI test
│   ├── Parecer técnico dos métodos multicritério.md   Technical review comparing the weighting and
│   │                                 aggregation methods (ABES, classical and Gaussian AHP, CRITIC,
│   │                                 PROMETHEE II, VIKOR, TOPSIS)
│   └── Guia de escrita.md            Writing guide for the paper, with the methodological rationale
├── jupyter notebooks/            Python reproduction of the spreadsheets plus the statistical analyses
│   ├── 01_rankings.ipynb             Weights, the 16 rankings and agreement between them
│   ├── 02_validade_drsai.ipynb       External validity of the 16 rankings against DRSAI
│   ├── 03_compensacao_perfil.ipynb   Compensation and profile of municipalities that change position
│   └── mcda.py                       Weighting schemes and aggregation methods, with the logged parameters
├── planilhas/                    Step-by-step calculations in LibreOffice Calc (.ods)
│   ├── Relatorio ABES 2026 NE.ods    Decision matrix: the 505 eligible municipalities (input to everything)
│   ├── AHP Classico.ods              Classical AHP
│   ├── AHP Gaussiano.ods             Gaussian AHP
│   ├── CRITIC.ods                    CRITIC weights and weighted sum with CRITIC
│   ├── PROMETHEE II.ods              PROMETHEE II under the four weighting schemes
│   ├── TOPSIS.ods                    TOPSIS under the four weighting schemes
│   └── VIKOR.ods                     VIKOR under the four weighting schemes
├── dados/                        Raw data as downloaded (Portuguese file names)
│   ├── SINISA/2025/                  SINISA 2025 (reference year 2024), Ministry of Cities, national files
│   │   ├── abastecimento de água/        Water supply
│   │   ├── esgotamento sanitário/        Sewage
│   │   └── resíduos sólidos/             Solid waste
│   └── ABES 2026/
│       └── relatorio ABES 2026 NE.xlsx   ABES 2026 ranking for all 1,794 Northeast municipalities
└── Rii2027 call for papers 2027-09-30.pdf   Call for papers of the target conference
```

What each spreadsheet and notebook contains, sheet by sheet, is in the [data dictionary](DATA_DICTIONARY.md#2-spreadsheets-planilhas).

## Data sources

| Dataset | Publisher | Reference year | Downloaded | Source |
| --- | --- | --- | --- | --- |
| SINISA 2025 (National Basic Sanitation Information System): water, sewage and solid waste | Brazilian Ministry of Cities | 2024 | 7 Nov 2026 | [gov.br/cidades, SINISA 2025 results](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/resultados-sinisa-2025) |
| ABES Sanitation Universalization Ranking 2026, Northeast | ABES (Brazilian Association of Sanitary and Environmental Engineering) | 2024 | 7 Nov 2026 | [rankingabes.abes-dn.org.br](https://rankingabes.abes-dn.org.br/relatorio.php) |

Caveats when reusing the raw data:

- In the ABES file, 1,289 of the 1,794 municipalities are "Não habilitado" (not eligible), and missing values are written as `0,00` rather than left blank, so their zeros are not real values.
- Numbers in the raw ABES file are stored as text in Brazilian format: comma as decimal separator and dot as thousands separator (for example `10.220,55`). Remove the dot before replacing the comma. `planilhas/Relatorio ABES 2026 NE.ods` already holds the converted numbers.
- The SINISA spreadsheets cover all of Brazil; filter the Northeast with the column `Macrorregião` = `Nordeste`. Not every municipality appears in every spreadsheet.
- For water supply, use the rectified file `SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`.

## How to reproduce

There are two independent routes to the same numbers.

**1. Spreadsheets (`planilhas/`).** Open the `.ods` files in LibreOffice Calc (version 24.2 was used). Each method file starts with a copy of the decision matrix (sheet `PLANILHA ABES`) and then follows the method step by step, one sheet per step ("ETAPA" = step), ending with the ranking and a comparison with ABES. Calculations are live formulas within each file. The weight vectors are typed into the PROMETHEE II, TOPSIS and VIKOR files with full precision (they are copied from the CRITIC and AHP files, not linked), so a change of weights must be entered there by hand. Inputs that can be changed are on the `PARÂMETROS` sheet of the PROMETHEE II, TOPSIS and VIKOR files (cell B30 of `TOPSIS.ods` switches between vector and min-max normalization) and on the Saaty matrix in `AHP Classico.ods`.

**2. Notebooks (`jupyter notebooks/`).** The notebooks read `planilhas/Relatorio ABES 2026 NE.ods` directly, recompute everything in Python and do not write any files. The scores they produce match the spreadsheets to the 15th decimal place.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt    # Python 3.13; odfpy is needed to read .ods files
cd "jupyter notebooks"
jupyter nbconvert --to notebook --execute --inplace 01_rankings.ipynb
jupyter nbconvert --to notebook --execute --inplace 02_validade_drsai.ipynb
jupyter nbconvert --to notebook --execute --inplace 03_compensacao_perfil.ipynb
```

Or open them in Jupyter and run all cells. Each notebook locates the repository root on its own (the first parent folder that contains `dados/`), so it can be started from any folder inside the repository. On a laptop the three run in under a minute in total. Random steps (bootstrap) use the fixed seed 20261109, so the results are deterministic.

| Notebook | What it does | Main outputs |
| --- | --- | --- |
| `01_rankings.ipynb` | Recomputes the four weight vectors and the 16 rankings using `mcda.py` | Weight table and Saaty consistency ratio; scores and positions; Spearman ρ and Kendall τ-b between all 16 rankings, grouped by pair type (same aggregation, same weights, both different); how many municipalities change quartile relative to ABES |
| `02_validade_drsai.ipynb` | Applies the external validity protocol (decision log, section 7) | Spearman ρ of each ranking with the DRSAI rate and bootstrap CI (figure F1); Δρ against ABES and for all pairs, with Steiger's test; average effect of weights vs. method; partial ρ controlling for state and size; ρ within states and size classes; ρ without the top 5% of rates |
| `03_compensacao_perfil.ipynb` | Answers secondary questions PS2 (compensation) and PS4 (profile of municipalities that move), as numbered in `docs/Guia de escrita.md` | Per-municipality inequality across indicators, worst indicator and number of zeros; how much method vs. weights move each municipality; direction of movement for municipalities with zeros; whether DRSAI tracks the worst indicator more than the mean; quartile changes between the ranking most associated with DRSAI and ABES; the 20 municipalities with the widest range of positions |

`mcda.py` contains the functions for every weighting scheme (`pesos_saaty`, `pesos_gaussianos`, `pesos_critic`) and aggregation method (`soma_ponderada`, `topsis`, `vikor_q`, `fluxos_por_criterio`), the function `rankings` that returns all 16 scores, and the logged parameters (`SAATY`, `Q`, `P`, `FUNCAO`, `V_VIKOR`). Function names are in Portuguese; the [data dictionary](DATA_DICTIONARY.md#4-python-module-mcdapy) translates them.

## Authorship and license

Omitted during the double-blind review for Rii Forum 2027; it will be restored in the final version.

The license for the code has not yet been chosen. The data in `dados/` belong to their publishers (Brazilian Ministry of Cities and ABES) and are subject to their terms of use.
