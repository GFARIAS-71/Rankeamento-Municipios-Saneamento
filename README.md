# Rankeamento de Municípios Nordestinos em Saneamento

Este repositório ranqueia os municípios do Nordeste (AL, BA, CE, MA, PB, PE, PI, RN e SE) pelo desempenho em saneamento básico e mede quanto a escolha do método multicritério altera esse ranking. Os mesmos cinco indicadores do [Ranking ABES da Universalização do Saneamento 2026](https://rankingabes.abes-dn.org.br/relatorio.php) são agregados por quatro métodos (soma ponderada, que é a regra do ABES, TOPSIS, VIKOR e PROMETHEE II), cada um com três esquemas de pesos (iguais, CRITIC e AHP Gaussiano). Os 12 rankings resultantes são comparados entre si e com a taxa de internações por DRSAI (doenças relacionadas ao saneamento ambiental inadequado), para saber qual ordenação se associa mais fortemente à saúde.

**Pergunta principal:** em que medida a escolha do método de agregação multicritério altera a ordenação dos municípios nordestinos quanto ao saneamento, e qual dessas ordenações se associa mais fortemente à taxa de internações por DRSAI, considerando diferenças entre estados e portes? O grau de compensação de cada método (quanto um indicador bom compensa um ruim) entra como pergunta secundária, para explicar as diferenças.

O estudo será submetido como artigo ao [Rii Forum 2027](https://rii-forum.org) (Roma, 6 e 8–9 de abril de 2027), com anais publicados pela Springer.

## Situação

Em andamento. Os dados brutos foram baixados e a matriz de decisão está pronta; os notebooks de ranking e de análise ainda não foram escritos.

| Etapa | Situação |
| --- | --- |
| Dados do SINISA 2025 baixados | Concluída |
| Dados do ABES 2026 para o Nordeste baixados | Concluída |
| Matriz de decisão montada (581 municípios, notebooks 01 e 02) | Concluída |
| Pesos (iguais, CRITIC e AHP Gaussiano) e os 12 rankings (soma ponderada, TOPSIS, VIKOR e PROMETHEE II) | A fazer |
| Validade externa com a DRSAI (Spearman, bootstrap das diferenças, controle por UF e porte) | A fazer |
| Robustez (SMAA, sensibilidade a q e p) e comparação com o ABES | A fazer |
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

- **Desenho métodos × pesos:** 12 rankings, sempre com os mesmos cinco critérios.

  | Método de agregação | Compensação | Pesos iguais | CRITIC | AHP Gaussiano |
  | --- | --- | --- | --- | --- |
  | Soma ponderada | Total | ✓ (reproduz a pontuação do ABES) | ✓ | ✓ (é o AHP Gaussiano da literatura) |
  | TOPSIS | Total | ✓ | ✓ | ✓ |
  | VIKOR | Parcial | ✓ | ✓ | ✓ |
  | PROMETHEE II | Limitada | ✓ | ✓ | ✓ |

  O AHP Gaussiano entra como esquema de pesos (desvio-padrão ÷ média de cada critério), seguido de soma ponderada, e não como método de agregação. Assim, o efeito da agregação fica separado do efeito dos pesos. Nenhum peso é definido pelos autores. Métodos, pesos e parâmetros (q e p do PROMETHEE, v do VIKOR) são fixados antes de olhar a DRSAI.
- **Validade externa:** correlação de Spearman entre cada ranking e a taxa de internações por DRSAI informada pelo ABES, nos 412 dos 581 municípios com taxa válida (taxa 0,00 é tratada como ausente). As diferenças entre rankings são testadas com intervalos bootstrap de Δρ. Como controle mínimo, a associação é recalculada com correlação parcial por UF e porte e dentro dos estados com amostra suficiente (BA, CE, PE, RN e PB). A DRSAI nunca entra como critério.
- **Robustez:** SMAA (10.000 vetores de pesos) e sensibilidade a q e p (±50%). Robustez e validade externa são análises separadas.
- **Leitura detalhada:** o PROMETHEE II com pesos CRITIC é o ranking de referência para o plano GAIA, o PROMETHEE I (diagnóstico) e o SMAA-PROMETHEE.
- **Fora do escopo:** o ajuste por renda, cobertura da atenção primária e acesso hospitalar exigiria novas bases (IBGE, e-Gestor AB, CNES, SIH/SUS) e fica como limitação e trabalho futuro. Os resultados são lidos como associação, e não como efeito.

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
├── resultados/                      Criada ao executar os notebooks; fora do Git
│   ├── municipios_5_indicadores.csv          505 municípios com os cinco indicadores (notebook 01)
│   └── municipios_4_ou_5_indicadores.csv     581 municípios, com o faltante imputado e a situação de cada indicador (notebook 02)
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

Execute os notebooks de `jupyter notebooks/` em ordem. A pasta `resultados/` não é versionada: ela é criada na primeira execução e recebe as planilhas geradas.

1. `01_filtragem_municipios.ipynb`: lê as planilhas em `dados/`, filtra os municípios do Nordeste, classifica os indicadores faltantes e gera `municipios_5_indicadores.csv`.
2. `02_imputacao_faltantes.ipynb`: imputa o indicador faltante e gera `municipios_4_ou_5_indicadores.csv`.

As etapas seguintes (pesos, os 12 rankings, validade externa com a DRSAI e robustez) ainda serão escritas.

As dependências ficarão em `requirements.txt`, com as versões fixadas.

## Autoria e licença

Guilherme de Farias ([@GFARIAS-71](https://github.com/GFARIAS-71)).

A licença do código ainda não foi definida. Os dados em `dados/` pertencem às respectivas fontes (Ministério das Cidades e ABES) e seguem as condições de uso delas.
