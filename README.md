# Rankeamento de Municípios Cearenses em Saneamento

O saneamento básico no Brasil, que reúne abastecimento de água, esgotamento sanitário, manejo de resíduos sólidos e drenagem urbana, avançou de forma desigual: o Planasa, nos anos 1970, priorizou a água nas cidades, e só a Lei 11.445/2007 deu ao setor diretrizes nacionais. A Lei 14.026/2020, o novo marco legal, fixou a meta de atender 99% da população com água potável e 90% com coleta e tratamento de esgoto até 2033, além de prazos para o fim dos lixões. O Ceará está longe dessas metas: em 2024, 72,2% da população tinha rede de água e só 32,6% tinha rede coletora de esgoto, contra 84,1% e 62,3% no Brasil (SINISA 2025). Os rankings públicos que acompanham essa distância, como o da ABES, somam indicadores com pesos iguais, de modo que um bom resultado em água pode esconder um déficit grave em esgoto ou em resíduos. Este projeto propõe um rankeamento parcialmente compensatório dos municípios cearenses, com métodos de apoio multicritério à decisão (MCDM) do estado da arte acadêmico (PROMETHEE II, pesos objetivos CRITIC e análise de robustez SMAA), para mostrar como a regra de agregação muda quem deve ser priorizado.

Na prática, este repositório ranqueia os 184 municípios do Ceará pelo desempenho em saneamento básico usando o método multicritério PROMETHEE II, com pesos objetivos CRITIC. O resultado é comparado ao [Ranking ABES da Universalização do Saneamento 2026](https://rankingabes.abes-dn.org.br/relatorio.php), que usa a mesma base, o mesmo ano e os mesmos cinco indicadores, mas soma os indicadores com pesos iguais. Com isso, a comparação isola o efeito da regra de agregação, que no ABES é compensatória e no PROMETHEE é de compensação limitada.

O estudo será submetido como artigo ao [Rii Forum 2027](https://rii-forum.org) (Roma, 6 e 8–9 de abril de 2027), com anais publicados pela Springer.

## Situação

Em andamento. Os dados brutos já foram baixados; os scripts de preparação e de análise ainda não foram escritos.

| Etapa | Situação |
| --- | --- |
| Dados do SINISA 2025 e do ABES 2026 baixados | Concluída |
| Matriz de decisão montada | A fazer |
| PROMETHEE II com CRITIC e com pesos iguais | A fazer |
| Robustez (SMAA, AHP Gaussiano, sensibilidade a q e p) e comparação com o ABES | A fazer |
| Resumo para o Rii Forum (prazo: 15/11/2026) | A fazer |
| Artigo completo (prazo: 30/12/2026) | A fazer |

## Método

- **Alternativas:** os municípios cearenses com dados suficientes no SINISA 2025. Entram os que têm os cinco indicadores e os que têm só um ausente, imputado pela mediana dos municípios de mesmo porte na região de saúde.
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
├── dados/
│   ├── SINISA/2025/                 SINISA 2025 (ano-base 2024), Ministério das Cidades
│   │   ├── abastecimento de água/   Planilhas por município, por prestador e consolidadas; glossário
│   │   ├── esgotamento sanitário/   Idem para esgoto
│   │   └── resíduos sólidos/        Planilhas de indicadores e de formulários; glossários e relatório
│   └── ABES 2026/
│       └── relatorio ABES 2026 CE.xlsx   Ranking ABES 2026 para os 184 municípios do Ceará
└── Rii2027 call for papers 2027-09-30.pdf   Chamada de trabalhos do Rii Forum 2027
```

## Fontes de dados

| Base | Órgão | Ano-base | Origem |
| --- | --- | --- | --- |
| SINISA 2025 (água, esgoto e resíduos sólidos) | Ministério das Cidades | 2024 | [gov.br/cidades, resultados SINISA 2025](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/resultados-sinisa-2025) |
| Ranking ABES da Universalização do Saneamento 2026 | ABES | 2024 | [rankingabes.abes-dn.org.br](https://rankingabes.abes-dn.org.br/relatorio.php) |

Cuidados ao usar os dados:

- No arquivo do ABES, 89 dos 184 municípios aparecem como "Não habilitado". Nesse arquivo, dado ausente aparece como `0,00`, e não como célula vazia, então os zeros dos não habilitados não podem ser usados como valores. Os números estão gravados como texto.
- Para o abastecimento de água, use a versão retificada da planilha (`SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`).
- As datas de extração de cada base devem ser registradas no `log_decisoes.md`, que ainda será criado.

## Como reproduzir

Os scripts ainda não existem. A estrutura prevista é:

1. `01_preparar.py`: lê as planilhas em `dados/`, aplica a regra de dados ausentes e gera `matriz_decisao.csv`.
2. `02_promethee.py`: calcula os pesos e o ranking PROMETHEE II.
3. `03_robustez.py`: roda SMAA, os esquemas de pesos alternativos, a sensibilidade a q e p e a comparação com o ABES.

As dependências ficarão em `requirements.txt`, com as versões fixadas.

## Autoria e licença

Guilherme de Farias ([@GFARIAS-71](https://github.com/GFARIAS-71)).

A licença do código ainda não foi definida. Os dados em `dados/` pertencem às respectivas fontes (Ministério das Cidades e ABES) e seguem as condições de uso delas.
