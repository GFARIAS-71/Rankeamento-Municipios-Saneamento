# Rankeamento de Municípios Nordestinos em Saneamento

Este repositório ranqueia os municípios do Nordeste (AL, BA, CE, MA, PB, PE, PI, RN e SE) pelo desempenho em saneamento básico e mede quanto a escolha do método multicritério altera esse ranking. Os mesmos cinco indicadores do [Ranking ABES da Universalização do Saneamento 2026](https://rankingabes.abes-dn.org.br/relatorio.php) são agregados por quatro métodos (soma ponderada, que é a regra do ABES, TOPSIS, VIKOR e PROMETHEE II), cada um com três esquemas de pesos (iguais, CRITIC e AHP Gaussiano). A esses 12 rankings soma-se o AHP clássico, com pesos definidos pela comparação par a par de Saaty. Entre os compensatórios estão, portanto, o ABES, o AHP clássico e o AHP Gaussiano. Os 13 rankings resultantes são comparados entre si e com a taxa de internações por DRSAI (doenças relacionadas ao saneamento ambiental inadequado), para saber qual ordenação se associa mais fortemente à saúde.

**Pergunta principal:** em que medida a escolha do método de agregação multicritério (soma ponderada do ABES, AHP clássico, AHP Gaussiano, TOPSIS, VIKOR ou PROMETHEE II) altera a ordenação dos municípios nordestinos quanto ao saneamento, e qual dessas ordenações se associa mais fortemente à taxa de internações por DRSAI, considerando diferenças entre estados e portes? O grau de compensação de cada método (quanto um indicador bom compensa um ruim) entra como pergunta secundária, para explicar as diferenças.

O estudo será submetido como artigo ao [Rii Forum 2027](https://rii-forum.org) (Roma, 6 e 8–9 de abril de 2027), com anais publicados pela Springer.

## Situação

Em andamento. Os dados brutos foram baixados e a matriz de decisão está pronta. O AHP clássico e o AHP Gaussiano já foram calculados em planilhas e comparados com o ABES no [parecer técnico](docs/Parecer%20técnico%20ABES,%20AHP%20Clássico%20e%20AHP%20Gaussiano.md); os notebooks de ranking e de análise ainda não foram escritos.

| Etapa | Situação |
| --- | --- |
| Dados do SINISA 2025 baixados | Concluída |
| Dados do ABES 2026 para o Nordeste baixados | Concluída |
| Matriz de decisão montada (505 municípios completos, notebook 01) | Concluída |
| AHP clássico e AHP Gaussiano em planilha, com parecer técnico comparando-os ao ABES | Concluída |
| AHP clássico e AHP Gaussiano portados para notebook | A fazer |
| Pesos (iguais, CRITIC e AHP Gaussiano) e os 13 rankings (soma ponderada, TOPSIS, VIKOR e PROMETHEE II, mais o AHP clássico) | A fazer |
| Validade externa com a DRSAI (Spearman, bootstrap das diferenças, controle por UF e porte) | A fazer |
| Robustez (SMAA, sensibilidade a q e p) e comparação com o ABES | A fazer |
| Resumo para o Rii Forum (prazo: 15/11/2026) | A fazer |
| Artigo completo (prazo: 30/12/2026) | A fazer |

## Método

- **Alternativas:** os 505 municípios nordestinos que autodeclararam ao SINISA 2025 os quatro indicadores contabilizados (IAG0001, IES0001, IES2003 e IRS0001), que coincidem com os habilitados no ABES 2026. O município a que falta qualquer um dos quatro fica de fora. Se o IRS3002 estiver ausente, assume-se disposição final inadequada (valor adaptado 0); nenhum dos 505 está nesse caso hoje.
- **Critérios:** os cinco indicadores do Ranking ABES, todos a maximizar.

  | Código | Indicador SINISA | Descrição |
  | --- | --- | --- |
  | C1 | IAG0001 | Atendimento da população total com rede de abastecimento de água |
  | C2 | IES0001 | Atendimento da população total com rede coletora de esgoto |
  | C3 | IES2003 | Esgoto tratado referido à água consumida (limitado a 100%) |
  | C4 | IRS0001 | Cobertura da população total com coleta de resíduos sólidos domiciliares |
  | C5 | IRS3002 adaptado | Disposição final adequada de resíduos (100 − disposição inadequada) |

- **Desenho métodos × pesos:** 12 rankings no desenho cruzado, mais o AHP clássico, num total de 13, sempre com os mesmos cinco critérios.

  | Método de agregação | Compensação | Pesos iguais | CRITIC | AHP Gaussiano |
  | --- | --- | --- | --- | --- |
  | Soma ponderada | Total | ✓ (reproduz a pontuação do ABES) | ✓ | ✓ (é o AHP Gaussiano da literatura) |
  | TOPSIS | Total | ✓ | ✓ | ✓ |
  | VIKOR | Parcial | ✓ | ✓ | ✓ |
  | PROMETHEE II | Limitada | ✓ | ✓ | ✓ |

  O AHP Gaussiano entra como esquema de pesos (desvio-padrão ÷ média de cada critério), seguido de soma ponderada, e não como método de agregação. Assim, o efeito da agregação fica separado do efeito dos pesos.
- **Métodos compensatórios AHP:** os dois AHP aplicam os pesos aos valores normalizados pela soma (cada indicador soma 1 nos 505 municípios) e somam os resultados.

  | Método | Como os pesos são obtidos | Água | Esgoto | Tratamento | Coleta | Destinação |
  | --- | --- | --- | --- | --- | --- | --- |
  | ABES (equivalente na escala normalizada) | Pesos iguais sobre as notas brutas | 26,7% | 13,7% | 9,5% | 31,3% | 18,7% |
  | AHP clássico | Matriz de Saaty preenchida pelo autor, média geométrica das linhas (RC = 0,0152) | 41,7% | 16,0% | 9,7% | 26,3% | 6,2% |
  | AHP Gaussiano | Coeficiente de variação de cada indicador, normalizado para somar 1 | 8,5% | 20,4% | 34,9% | 6,8% | 29,5% |

  O AHP clássico é o único com pesos definidos pelos autores. Por isso ele fica fora do desenho cruzado e entra só com soma ponderada, como contraste entre pesos subjetivos e objetivos. A normalização importa: 20% para cada valor normalizado não reproduz o ABES (ρ = 0,95), então a comparação de pesos usa os equivalentes do ABES da tabela acima. Métodos, pesos e parâmetros (q e p do PROMETHEE, v do VIKOR) são fixados antes de olhar a DRSAI.
- **Validade externa:** correlação de Spearman entre cada ranking e a taxa de internações por DRSAI informada pelo ABES, nos 360 dos 505 municípios com taxa válida (taxa 0,00 é tratada como ausente). As diferenças entre rankings são testadas com intervalos bootstrap de Δρ. Como controle mínimo, a associação é recalculada com correlação parcial por UF e porte e dentro dos estados com amostra suficiente (BA, CE, PE, RN e PB). A DRSAI nunca entra como critério.
- **Robustez:** SMAA (10.000 vetores de pesos), sensibilidade a q e p (±50%) e, no AHP clássico, a pequenas variações dos julgamentos da matriz de Saaty. Robustez e validade externa são análises separadas.
- **Leitura detalhada:** o PROMETHEE II com pesos CRITIC é o ranking de referência para o plano GAIA, o PROMETHEE I (diagnóstico) e o SMAA-PROMETHEE.
- **Fora do escopo:** o ajuste por renda, cobertura da atenção primária e acesso hospitalar exigiria novas bases (IBGE, e-Gestor AB, CNES, SIH/SUS) e fica como limitação e trabalho futuro. Os resultados são lidos como associação, e não como efeito.

O detalhamento das decisões e o roteiro do artigo estão em [docs/guia_escrita.md](docs/guia_escrita.md).

## Estrutura do repositório

```text
.
├── README.md
├── docs/
│   ├── guia_escrita.md              Guia de escrita do artigo e decisões metodológicas
│   ├── Parecer técnico ABES, AHP Clássico e AHP Gaussiano.md   Comparação dos três rankings compensatórios
│   └── imagens/                     Figuras dos documentos (pesos do ABES e dos AHP)
├── jupyter notebooks/
│   └── 01_filtragem_municipios.ipynb   Classifica os indicadores faltantes e seleciona as alternativas
├── planilhas/                       Cálculos feitos no LibreOffice Calc
│   ├── relatorio ABES 2026 NE.ods       Os 505 habilitados do ABES 2026, com os números convertidos; base dos dois AHP
│   ├── AHP Classico.ods                 Matriz de Saaty, pesos, consistência, ranking e comparação com o ABES
│   └── AHP Gaussiano.ods                Pesos gaussianos, ranking e comparação com o ABES
├── resultados/                      Criada ao executar os notebooks; fora do Git
│   └── municipios_5_indicadores.csv     Matriz de decisão: 505 municípios com os cinco indicadores e a situação de cada um
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

Os rankings do AHP clássico e do AHP Gaussiano estão, por enquanto, em `planilhas/` (abra no LibreOffice Calc). As etapas seguintes (pesos, os 13 rankings em notebook, validade externa com a DRSAI e robustez) ainda serão escritas.

As dependências ficarão em `requirements.txt`, com as versões fixadas.

## Autoria e licença

Guilherme de Farias ([@GFARIAS-71](https://github.com/GFARIAS-71)).

A licença do código ainda não foi definida. Os dados em `dados/` pertencem às respectivas fontes (Ministério das Cidades e ABES) e seguem as condições de uso delas.
