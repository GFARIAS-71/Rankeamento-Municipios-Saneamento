# Rankeamento de Municípios Nordestinos em Saneamento

Este repositório ranqueia os 1.794 municípios do Nordeste (AL, BA, CE, MA, PB, PE, PI, RN e SE) pelo desempenho em saneamento básico usando o método multicritério PROMETHEE II, com pesos objetivos CRITIC. O resultado é comparado ao [Ranking ABES da Universalização do Saneamento 2026](https://rankingabes.abes-dn.org.br/relatorio.php), que usa a mesma base, o mesmo ano e os mesmos cinco indicadores, mas soma os indicadores com pesos iguais. Com isso, a comparação isola o efeito da regra de agregação, que no ABES é compensatória e no PROMETHEE é de compensação limitada.

O estudo será submetido como artigo ao [Rii Forum 2027](https://rii-forum.org) (Roma, 6 e 8–9 de abril de 2027), com anais publicados pela Springer.

## Situação

Em andamento. Os dados brutos já foram baixados; os scripts de preparação e de análise ainda não foram escritos.

| Etapa | Situação |
| --- | --- |
| Dados do SINISA 2025 baixados | Concluída |
| Dados do ABES 2026 para o Nordeste baixados | Concluída |
| Matriz de decisão montada | A fazer |
| PROMETHEE II com CRITIC e com pesos iguais | A fazer |
| Robustez (SMAA, AHP Gaussiano, sensibilidade a q e p) e comparação com o ABES | A fazer |
| Resumo para o Rii Forum (prazo: 15/11/2026) | A fazer |
| Artigo completo (prazo: 30/12/2026) | A fazer |

## Método

- **Alternativas:** os municípios nordestinos com dados suficientes no SINISA 2025. Entram os que têm os cinco indicadores e os que têm só um ausente, imputado pela média ponderada dos 15 municípios de mesmo porte mais parecidos nos demais indicadores (KNN, escolhido por validação cruzada). Se o IRS3002 estiver ausente, assume-se disposição inadequada (valor adaptado 0).
- **Critérios:** os cinco indicadores do Ranking ABES, todos a maximizar.

  | Código | Indicador SINISA | Descrição |
  | --- | --- | --- |
  | C1 | IAG0001 | Atendimento da população total com rede de abastecimento de água |
  | C2 | IES0001 | Atendimento da população total com rede coletora de esgoto |
  | C3 | IES2003 | Esgoto tratado referido à água consumida (limitado a 100%) |
  | C4 | IRS0001 | Cobertura da população total com coleta de resíduos sólidos domiciliares |
  | C5 | IRS3002 adaptado | Disposição final adequada de resíduos (100 − disposição inadequada) |

- **Pesos:** CRITIC no ranking principal; AHP Gaussiano, pesos iguais e SMAA (10.000 vetores) como testes de robustez.
- **Análises:** PROMETHEE II, PROMETHEE I como diagnóstico, plano GAIA e SMAA-PROMETHEE.
- **Validação externa:** associação das ordenações com a taxa de internações por DRSAI (doenças relacionadas ao saneamento ambiental inadequado) informada pelo ABES.

O detalhamento das decisões e o roteiro do artigo estão em [docs/guia_escrita.md](docs/guia_escrita.md).

## Estrutura do repositório

```text
.
├── README.md
├── docs/
│   └── guia_escrita.md              Guia de escrita do artigo e decisões metodológicas
├── jupyter notebooks/
│   ├── 01_filtragem_municipios.ipynb   Classifica os indicadores faltantes e seleciona as alternativas
│   └── 02_imputacao_faltantes.ipynb    Compara técnicas de imputação e completa a matriz de decisão
├── resultados/
│   ├── municipios_5_indicadores.csv          Saída da filtragem: só os municípios completos
│   ├── municipios_4_ou_5_indicadores.csv     Saída da filtragem: completos e com um faltante
│   └── matriz_decisao.csv           Matriz de decisão com o indicador faltante imputado
├── dados/
│   ├── SINISA/2025/                 SINISA 2025 (ano-base 2024), Ministério das Cidades; base nacional, filtrada para o Nordeste
│   │   ├── abastecimento de água/   Planilhas por município, por prestador e consolidadas; glossário
│   │   ├── esgotamento sanitário/   Idem para esgoto
│   │   └── resíduos sólidos/        Planilhas de indicadores e de formulários; glossários e relatório
│   └── ABES 2026/
│       └── relatorio ABES 2026 NE.xlsx   Ranking ABES 2026 para os 1.794 municípios do Nordeste
└── Rii2027 call for papers 2027-09-30.pdf   Chamada de trabalhos do Rii Forum 2027
```

## Fontes de dados

| Base | Órgão | Ano-base | Origem |
| --- | --- | --- | --- |
| SINISA 2025 (água, esgoto e resíduos sólidos) | Ministério das Cidades | 2024 | [gov.br/cidades, resultados SINISA 2025](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/resultados-sinisa-2025) |
| Ranking ABES da Universalização do Saneamento 2026 | ABES | 2024 | [rankingabes.abes-dn.org.br](https://rankingabes.abes-dn.org.br/relatorio.php) |

Cuidados ao usar os dados:

- Nesse arquivo, 1.289 dos 1.794 municípios aparecem como "Não habilitado", com grande variação entre estados (3% de habilitados no Piauí, 52% no Ceará). Dado ausente aparece como `0,00`, e não como célula vazia, então os zeros dos não habilitados não podem ser usados como valores.
- Os números estão gravados como texto, com vírgula decimal e ponto de milhar (por exemplo, `10.220,55` na taxa de DRSAI).
- As planilhas do SINISA são nacionais; filtre os municípios do Nordeste pela coluna `Macrorregião` (valor `Nordeste`). Nem todo município aparece em todas as planilhas: a de indicadores de água traz 1.528 dos 1.794 municípios nordestinos, e só 36 dos 224 do Piauí.
- Para o abastecimento de água, use a versão retificada da planilha (`SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`).
- As datas de extração de cada base devem ser registradas no `log_decisoes.md`, que ainda será criado.

## Como reproduzir

Os scripts ainda não existem. A estrutura prevista é:

1. `01_preparar.py`: lê as planilhas em `dados/`, filtra os municípios do Nordeste, aplica a regra de dados ausentes e gera `matriz_decisao.csv`.
2. `02_promethee.py`: calcula os pesos e o ranking PROMETHEE II.
3. `03_robustez.py`: roda SMAA, os esquemas de pesos alternativos, a sensibilidade a q e p e a comparação com o ABES.

As dependências ficarão em `requirements.txt`, com as versões fixadas.

## Autoria e licença

Guilherme de Farias ([@GFARIAS-71](https://github.com/GFARIAS-71)).

A licença do código ainda não foi definida. Os dados em `dados/` pertencem às respectivas fontes (Ministério das Cidades e ABES) e seguem as condições de uso delas.
