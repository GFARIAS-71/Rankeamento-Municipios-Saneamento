# Guia de Escrita — Artigo Aplicado com PROMETHEE

Guilherme de Farias · 5 out. 2026 · revisado em 24 out. 2026 (escopo ampliado do Ceará para o Nordeste)

## Como usar este guia

Este guia cobre as sete seções do artigo na ordem em que serão lidas (Introdução, Pergunta e escopo, Revisão, Metodologia, Resultados e discussão, Limitações, Conclusão), mais as Referências, com o que cada uma precisa conter, parágrafos-modelo e os erros que mais levam à rejeição. O exemplo condutor é o projeto deste repositório: o desempenho em saneamento dos municípios do Nordeste com a base SINISA 2025 (ano-base 2024), ordenado por PROMETHEE II com pesos CRITIC e comparado ao Ranking ABES da Universalização do Saneamento 2026.

**Tamanho-alvo** para os anais do Rii Forum 2027, publicados pela Springer e indexados na Scopus, escritos em inglês. A chamada (`Rii2027 call for papers 2027-09-30.pdf`, na raiz do repositório) não informa a série dos anais nem o limite de páginas; o planejamento abaixo assume 12 a 15 páginas no modelo Springer, cerca de 4.500 a 5.500 palavras com referências. Confirme o limite com info@rii-forum.org antes de começar a cortar.

| Seção | Palavras | Figuras/tabelas típicas |
| --- | --- | --- |
| Introdução ao problema | 500–650 | nenhuma |
| Pergunta de pesquisa e escopo | 150–250 | nenhuma |
| Revisão de literatura | 700–900 | 1 tabela-síntese de estudos anteriores |
| Metodologia | 900–1.200 | tabela de critérios, tabela de pesos |
| Resultados e discussão | 1.200–1.500 | ranking, GAIA, SMAA, comparação com o ABES (4 a 5 exibições no total) |
| Limitações e trabalhos futuros | 250–350 | nenhuma |
| Conclusão | 150–250 | nenhuma |
| Referências (fora da contagem de seções) | 25–40 itens | — |

**Convenções adotadas ao longo do guia:**

- Cada seção começa pelo seu ponto principal. O leitor (e o revisor) deve conseguir ler só a primeira frase de cada seção e entender o argumento.
- Parágrafos de 3 a 5 frases. Frases com menos de 25 palavras sempre que possível.
- Toda afirmação sobre o estado da arte leva citação. Toda afirmação sobre dado leva fonte, ano-base e data de extração.
- Escreva os Resultados antes da Introdução. A introdução promete o que os resultados entregam, então ela só pode ser finalizada depois.
- Mantenha um arquivo `log_decisoes.md` com cada escolha metodológica e sua justificativa. Ele vira a seção de Metodologia e as respostas aos revisores.

## Antes de escrever: o que precisa estar fechado

Não comece a redigir antes de fechar as sete decisões abaixo. Cada uma aparece em pelo menos três seções do artigo, e mudá-la depois obriga a reescrever tudo.

| Decisão | Situação | Escolha | Onde aparece no artigo |
| --- | --- | --- | --- |
| Unidade de análise (alternativas) | Fechada | Os 1.794 municípios dos nove estados do Nordeste (AL, BA, CE, MA, PB, PE, PI, RN, SE) como universo; entram no ranking os que têm dados suficientes (regra abaixo) | Escopo, Metodologia, Resultados |
| Recorte temporal e base | Fechada | SINISA 2025 (ano-base 2024); SINISA 2024 (ano-base 2023) só como contexto, ainda não baixado para `dados/SINISA/2024/` | Escopo, Dados, Limitações |
| Conjunto de critérios | Fechada | Os cinco indicadores do Ranking ABES: IAG0001, IES0001, IES2003, IRS0001 e IRS3002 (adaptado) | Revisão, Metodologia, Resultados |
| Pesos | Fechada | CRITIC (principal); AHP Gaussiano e pesos iguais (robustez); SMAA com 10.000 vetores | Metodologia, Resultados, Limitações |
| Variante PROMETHEE | Fechada | PROMETHEE II + GAIA + SMAA; PROMETHEE I só como diagnóstico; FlowSort opcional | Revisão, Metodologia, Resultados |
| Benchmark externo | Fechada | Ranking ABES da Universalização do Saneamento 2026 (mesma base, ano e critérios; soma com pesos iguais; 4 categorias nacionais, das quais 3 aparecem entre os habilitados do Nordeste, uma delas com só 7 municípios) | Introdução, Resultados, Discussão |
| Veículo | Fechada | Rii Forum 2027 (Roma; anais pela Springer, Scopus); texto em inglês | Todo o texto |

**Decisão derivada: municípios sem dados completos.** O arquivo do ABES para o Nordeste (`dados/ABES 2026/relatorio ABES 2026 NE.xlsx`) traz os 1.794 municípios dos nove estados. Deles, 1.289 aparecem como "Não habilitado" e 505 (28%) como habilitados: 367 em "Empenho para universalização", 131 em "Primeiros passos para a universalização" e 7 em "Compromisso com a universalização" (Salvador, Vitória da Conquista, Jequié e Porto Seguro/BA, União dos Palmares/AL, Campina Grande/PB e Aracaju/SE); a categoria mais alta não aparece na região. A habilitação varia muito entre estados:

| UF | Municípios | Habilitados | % |
| --- | --- | --- | --- |
| AL | 102 | 22 | 22% |
| BA | 417 | 151 | 36% |
| CE | 184 | 95 | 52% |
| MA | 217 | 11 | 5% |
| PB | 223 | 65 | 29% |
| PE | 185 | 77 | 42% |
| PI | 224 | 6 | 3% |
| RN | 167 | 55 | 33% |
| SE | 75 | 23 | 31% |

Usar só os completos excluiria mais de dois terços da região e quase todo o Maranhão e o Piauí, provavelmente os pequenos municípios do interior com pior saneamento, o que enviesaria o ranking. A desigualdade de cobertura entre estados também é um achado: registre-a e teste se o ranking muda quando cada estado é retirado.

**Armadilha do arquivo do ABES:** nele, dado ausente aparece como "0,00", e não como célula vazia. Não é possível distinguir ausência de zero verdadeiro: entre os 505 habilitados, 248 têm 0 em IRS3002, 154 em IES2003 e 1 em IES0001 e em IAG0001. Nunca use os zeros dos 1.289 não habilitados como valores no PROMETHEE, porque eles contariam como o pior desempenho possível. A taxa de DRSAI também vale 0,00 em 789 municípios, 145 deles habilitados; trate esses casos como ausentes na validação. Os números estão gravados como texto, com vírgula decimal e ponto de milhar (100 taxas de DRSAI passam de 1.000, como `10.220,55`), e precisam ser convertidos removendo o ponto antes de trocar a vírgula (no Calc: Dados → Texto para colunas, idioma Português do Brasil).

**Regra adotada:**

1. Extrair os cinco indicadores das planilhas da Base Municipal do SINISA 2025 em `dados/SINISA/2025/` para os 1.794 municípios do Nordeste (filtro pela coluna `Macrorregião` = `Nordeste`), onde o ausente aparece como vazio. Para o IAG0001, usar a versão retificada (`SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`) e registrar isso no `log_decisoes.md`. Município que não aparece na planilha conta como ausente em todos os indicadores dela: a de indicadores de água traz 1.528 dos 1.794 municípios nordestinos (BA 406, PB 214, CE 182, PE 180, MA 175, RN 163, AL 97, SE 75 e só 36 do PI).
2. Classificar cada município: completo (5 de 5), falta 1 indicador, faltam 2 ou mais.
3. **Amostra principal:** completos + os que têm só 1 indicador ausente, imputado pela mediana dos municípios de mesmo porte na região de saúde. Os que têm 2 ou mais ausentes ficam fora e são listados em apêndice.
4. **Testes:** (a) só os completos; (b) imputação de todos os ausentes. Reporte o Kendall τ entre os rankings.
5. Registrar no `log_decisoes.md` quantos municípios caem em cada classe e quais indicadores faltam com mais frequência.
6. **Verificar** se os completos no SINISA coincidem com os 505 habilitados no ABES. É a hipótese de trabalho, mas a habilitação do ABES pode ter outras exigências e o arquivo do ABES grava ausência como 0,00. A subamostra de comparação com o ABES é sempre a dos habilitados; se as duas listas divergirem, registre quais municípios diferem e por quê.

Daqui em diante, "amostra principal" designa os [c + k] municípios com dados suficientes (c completos e k com um único indicador ausente, imputado), e não os 1.794: quem tem 2 ou mais indicadores ausentes não entra no ranking. A diferença de cobertura entre o ABES (505 municípios) e o seu estudo é um achado em si: o PROMETHEE ordena municípios que o ranking oficial descarta. Vale uma frase na Introdução e outra na Discussão.

**Consequência de usar os mesmos critérios do ABES.** Com base, ano e critérios idênticos, a comparação com pesos iguais isola completamente o efeito do método de agregação. Esse é o argumento central do artigo. Como o ABES traz a taxa de internações por DRSAI de cada município, ela pode servir de validação externa, sem entrar como critério: qual ordenação se associa mais fortemente à saúde, a do ABES ou a do PROMETHEE?

### Cronograma até o Rii Forum 2027

| Data | Marco | Tipo |
| --- | --- | --- |
| 1 nov. 2026 | Fim da inscrição com desconto (on-line 300 EUR, depois 350 EUR; presencial 550 EUR, depois 650 EUR) | Prazo do evento |
| até 2 nov. 2026 | Dados do SINISA 2025 e do apêndice do ABES extraídos e matriz montada | Interno |
| até 12 nov. 2026 | PROMETHEE II com CRITIC e com pesos iguais rodando; primeiros números para o resumo | Interno |
| 15 nov. 2026 | Envio do resumo pelo formulário do site (limite de palavras a confirmar no formulário) | Prazo do evento |
| até 30 nov. 2026 | SMAA, AHP Gaussiano, sensibilidade a q/p e comparação com o ABES concluídos | Interno |
| até 20 dez. 2026 | Versão completa revisada, no modelo Springer | Interno |
| 30 dez. 2026 | Envio do artigo completo | Prazo do evento |
| 6 abr. 2027 | Apresentações on-line | Evento |
| 8–9 abr. 2027 | Apresentações presenciais em Roma | Evento |

**Trilha sugerida no formulário:** *Artificial Intelligence, Algorithms and Data-Driven Governance*, com o enquadramento de que rankings públicos são instrumentos algorítmicos de priorização e a regra de agregação muda quem é priorizado. Alternativas: *Complexity Management and Decision Support Systems*, a trilha mais próxima do método, e *Politics, Public Policy, Democracy and Regulation*, a mais conservadora.

**Checklist de reprodutibilidade** (o que precisa existir antes do primeiro parágrafo):

- [x] Dados brutos baixados em `dados/` (SINISA 2025 e ABES 2026), com a URL de origem nos arquivos `.url`
- [ ] Data de extração de cada base registrada no `log_decisoes.md`
- [ ] Conjunto de scripts numerados (`01_preparar.py`, `02_promethee.py`, `03_robustez.py`) que gera todas as tabelas e figuras a partir dos dados brutos, com as versões das bibliotecas em `requirements.txt`
- [ ] Matriz de decisão final salva como `matriz_decisao.csv` (alternativas nas linhas, critérios nas colunas)
- [ ] Tabela de critérios com nome, unidade, direção (max/min), fonte, função de preferência, limiares q e p
- [ ] Dicionário de pesos para cada esquema, com o cálculo documentado
- [x] Repositório no GitHub criado
- [ ] Repositório ligado ao Zenodo para receber o DOI antes da submissão
- [ ] `log_decisoes.md` iniciado

Se algum item não puder ser cumprido (por exemplo, a base não permite redistribuição), registre isso agora: será uma frase na seção de Dados e outra em Limitações.

## Seção 1 — Introdução ao problema a ser resolvido

A introdução tem um único objetivo: convencer o revisor, em cinco parágrafos, de que existe um problema real, que a forma atual de medi-lo é inadequada, e que o artigo entrega algo que não existia. Estrutura em funil, do geral ao específico.

**Parágrafo 1 — O problema no mundo.** Comece pelo fato, não pelo método. Uma frase de abertura com número e fonte oficial. Exemplo:

> *No Brasil, a Lei 14.026/2020 fixou metas de universalização de 99% de cobertura de água e 90% de coleta e tratamento de esgoto até 2033; para o ano de 2024, apenas 45,9% dos municípios brasileiros enviaram ao SINISA os dados necessários para calcular os cinco indicadores básicos de saneamento (ABES, 2026).*

Siga com duas ou três frases sobre as consequências (saúde, desigualdade regional, custo fiscal) e sobre a situação do Nordeste. Fonte em cada número.

**Parágrafo 2 — Como o problema é medido hoje e por que isso é insuficiente.** Apresente o índice ou a prática corrente (no seu caso, o Ranking ABES da Universalização do Saneamento, que soma cinco indicadores com pesos iguais e classifica os municípios em quatro categorias) e sua limitação estrutural. No caso do ABES, a limitação é a agregação compensatória (soma com pesos iguais) e a exclusão dos municípios não habilitados; a cobertura parcial dos 100 maiores municípios é limitação de outro índice, o do Trata Brasil. Não critique o índice; mostre que ele responde a outra pergunta.

**Parágrafo 3 — O que a literatura já fez e o que falta.** Dois ou três estudos que aplicaram MCDM ao mesmo domínio, uma frase para cada, e a lacuna que eles deixam. A lacuna precisa ser verificável: base nova ainda não explorada, ausência de análise de robustez, ausência de comparação com o índice oficial, ausência de dimensão temporal. Cite as revisões (Behzadian et al., 2010; Yu et al., 2023; Tarnanidis et al., 2026) só aqui, uma vez.

**Parágrafo 4 — O que este artigo faz.** Uma frase de propósito e, em seguida, três bullets de contribuição. Os bullets são o que o editor lê para decidir se envia a revisores. Modelo:

- Avaliação de compensação limitada (PROMETHEE) do desempenho de saneamento dos municípios nordestinos com a base SINISA 2025 (ano-base 2024), cobrindo [c + k] dos 1.794 municípios, inclusive municípios que o ranking oficial descarta.
- Pesos objetivos CRITIC, que descontam a redundância entre indicadores correlacionados, testados contra AHP Gaussiano, pesos iguais e 10.000 cenários SMAA, o que elimina a arbitrariedade dos pesos apontada como falha recorrente na literatura PROMETHEE (Tarnanidis et al., 2026).
- Comparação controlada com o Ranking ABES da Universalização do Saneamento 2026: mesma base, mesmo ano, mesmos cinco indicadores e, no cenário de pesos iguais, mesmos pesos. Toda diferença de posição decorre apenas da regra de agregação, o que mostra como a escolha do algoritmo de um ranking público muda quem é priorizado.

**Parágrafo 5 — Organização do artigo.** Uma frase por seção. Alguns periódicos dispensam este parágrafo; verifique o guia de autores.

**O que não fazer:**

- Não abra com a definição de MCDM ou com a história do PROMETHEE. Isso pertence à revisão.
- Não use "inovador" ou "pioneiro" sobre o próprio trabalho. Mostre a lacuna e deixe o leitor concluir.
- Não prometa o que os resultados não entregam. Escreva a introdução por último.
- Não cite mais de 12 a 15 referências na introdução. O excesso sinaliza que a revisão foi mal separada.

## Seção 2 — Pergunta de pesquisa e escopo do projeto

A pergunta de pesquisa é uma frase interrogativa que o artigo responde com um sim, um não, um ranking ou um número. Se a resposta couber em uma frase da conclusão, a pergunta está bem formulada.

**Fórmula da pergunta principal (PP):** *Como [alternativas] se ordenam em [dimensão] quando [compensação limitada / incerteza], e em que medida essa ordem difere de [benchmark oficial]?*

Exemplo (Ideia 1):

> **PP:** Como os municípios nordestinos se ordenam quanto ao desempenho em saneamento quando a compensação entre componentes é limitada, de modo que déficits graves em um componente não são neutralizados por bons resultados nos demais, e quanto essa ordem difere da classificação plenamente compensatória do Ranking ABES da Universalização do Saneamento 2026?

**Perguntas secundárias (até quatro):** cada uma corresponde a uma subseção dos Resultados.

- **PS1:** Quais dos cinco indicadores mais discriminam os municípios e quais estão em conflito (análise GAIA e pesos CRITIC)?
- **PS2:** Quão estável é o ranking frente à incerteza nos pesos (índices de aceitabilidade SMAA) e frente à retirada de alternativas (reversão de ordem)?
- **PS3:** Entre os habilitados no ABES, quais municípios mudam de quartil ou de categoria entre a agregação compensatória do ABES e a de compensação limitada do PROMETHEE, e qual perfil de desempenho explica a mudança?
- **PS4 (validação externa):** Qual das duas ordenações se associa mais fortemente às internações por DRSAI?

**Escopo** é o que delimita a resposta. Escreva-o em quatro frases, uma por dimensão:

| Dimensão | Como redigir | Exemplo (Ideia 1) |
| --- | --- | --- |
| Espacial | Nomeie a unidade e o universo | Os 1.794 municípios do Nordeste; amostra principal = completos + os que têm 1 indicador ausente (imputado); subamostra de comparação com o ABES = os 505 habilitados |
| Temporal | Ano-base e, se houver, série | Ano-base 2024 (SINISA 2025); SINISA 2024 (ano-base 2023) citado apenas na discussão de tendência |
| Temática | Quais dimensões do problema entram | Os cinco indicadores do ABES, que cobrem três dos quatro componentes do saneamento: abastecimento de água, esgotamento sanitário (coleta e tratamento) e resíduos sólidos (coleta e disposição final); drenagem fora; DRSAI só como validação |
| Metodológica | Família de métodos e o que não se compara | PROMETHEE II com pesos CRITIC, GAIA e SMAA; AHP Gaussiano e pesos iguais como testes |

**O que fica fora, dito explicitamente.** Uma frase para cada exclusão relevante e o motivo: *"Drenagem urbana não foi incluída porque o módulo correspondente do SINISA 2025 cobriu apenas [x]% dos municípios nordestinos."* (O módulo de drenagem não está em `dados/`; baixe-o se for usar esse número.) Exclusões não justificadas viram perguntas de revisor.

**Erro comum:** confundir objetivo com pergunta. *"Avaliar o desempenho dos municípios"* é um objetivo e não pode ser respondido. *"Quais municípios estão mais distantes da meta de 2033 quando..."* é uma pergunta.

## Seção 3 — Revisão de literatura

A revisão não é um inventário; é um argumento em três blocos que termina na lacuna que o artigo preenche. Cada bloco tem de 200 a 300 palavras e fecha com uma frase que aponta para o próximo.

**Bloco 3.1 — O problema no domínio de aplicação.** Como o desempenho em [saneamento] é medido e avaliado na literatura e nos instrumentos oficiais. Cubra: (a) os índices oficiais e sua construção (Ranking ABES da Universalização: cinco indicadores SINISA somados com pesos iguais, quatro categorias fixas, das quais três aparecem no Nordeste; Ranking do Trata Brasil, restrito aos 100 municípios mais populosos, só [n] deles nordestinos); (b) estudos acadêmicos que avaliaram o mesmo objeto com qualquer método (DEA, regressão, índices compostos); (c) o que esses estudos concordam que importa (os critérios que você vai usar nascem aqui). Fecho: *"Esses trabalhos convergem sobre quais dimensões importam, mas as agregam de forma compensatória e sem avaliar a robustez dos resultados."*

**Bloco 3.2 — PROMETHEE e MCDA aplicados ao domínio.** Apresente a família PROMETHEE em um parágrafo (Brans & Vincke, 1985; Brans & Mareschal, 2005), as variantes que você usa em outro (SMAA-PROMETHEE, Corrente et al., 2014; GAIA), e então os estudos que aplicaram PROMETHEE ou outros MCDA ao domínio, no Brasil e fora. Para cada estudo citado, uma frase com: objeto, alternativas, número de critérios, forma de definir pesos, se fez análise de sensibilidade. Esses cinco atributos alimentam a tabela-síntese.

**Bloco 3.3 — Lacunas e posicionamento.** Nomeie as lacunas com base nas revisões (Behzadian et al., 2010; Yu et al., 2023; Tarnanidis et al., 2026) e no que a tabela-síntese mostra. Fecho obrigatório: um parágrafo que diz exatamente o que este artigo faz que os anteriores não fizeram, em diálogo direto com a tabela.

**Tabela-síntese (obrigatória).** É a figura mais lida da revisão e a prova da lacuna. Uma linha por estudo, 8 a 15 estudos, o seu artigo na última linha.

| Estudo | Objeto/alternativas | Método | Critérios (n) | Pesos | Análise de sensibilidade | Comparação com índice oficial |
| --- | --- | --- | --- | --- | --- | --- |
| Autor (ano) | 92 municípios do RJ | PROMETHEE II | 7 | Especialistas | Não | Não |
| ABES (2026) | 2.558 municípios habilitados | Soma de indicadores | 5 | Iguais | Não | — |
| Autor (ano) | 27 UFs | DEA | 5 | — | Parcial | Não |
| **Este artigo** | [c + k] municípios do Nordeste | PROMETHEE II + GAIA + SMAA | 5 | CRITIC (+ AHP Gaussiano, iguais, SMAA) | Sim (SMAA, intervalos, p/q, reversão) | Sim (Ranking ABES 2026) |

**Estratégia de busca (um parágrafo ou uma nota de rodapé).** Bases (Scopus, Web of Science, SciELO, Google Scholar para literatura cinzenta brasileira), string de busca (ex.: `PROMETHEE AND (sanitation OR "water supply" OR sewage) AND (municipal* OR Brazil*)`), período (2010–2026), critérios de inclusão e exclusão, número final de estudos. Isso não é uma revisão sistemática completa, mas mostra ao revisor que a amostra de estudos não foi escolhida por conveniência.

**Erros comuns:**

- Listar métodos MCDA (AHP, TOPSIS, ELECTRE...) sem relação com o problema. Cite só o que compara com sua escolha.
- Resumir cada estudo em um parágrafo. Uma frase por estudo; o detalhe vai para a tabela.
- Fechar a revisão sem a frase de lacuna. O revisor precisa ler, em uma frase, por que o artigo existe.
- Citar só artigos brasileiros ou só internacionais. Periódicos internacionais esperam que o caso brasileiro dialogue com a literatura global de economias emergentes.

## Seção 4 — Metodologia

A metodologia precisa permitir que outro pesquisador reproduza o ranking a partir dos mesmos dados. Organize-a em sete subseções, na ordem do fluxo de trabalho, e abra com um parágrafo que resume as etapas.

1. Fonte e preparação dos dados
2. Alternativas
3. Critérios
4. Funções de preferência e limiares
5. Pesos
6. Método multicritério (PROMETHEE I/II, GAIA, SMAA)
7. Análise de robustez e comparação com o benchmark

### 4.1 Dados

Para cada base, informe em uma tabela: órgão, nome do sistema, ano-base, data de extração, URL, variáveis extraídas, cobertura (quantos municípios reportaram) e tratamento de ausentes. Exemplo:

| Base | Órgão | Ano-base | Extração | Variáveis | Cobertura no Nordeste | Ausentes |
| --- | --- | --- | --- | --- | --- | --- |
| SINISA 2025 — Água | Ministério das Cidades | 2024 | [data] | IAG0001 (planilha retificada) | [n de 1.794] | Regra definida em "Antes de escrever" |
| SINISA 2025 — Esgoto | Ministério das Cidades | 2024 | [data] | IES0001, IES2003 | [n de 1.794] | Idem; IES2003 acima de 100% limitado a 100, como no ABES |
| SINISA 2025 — Resíduos | Ministério das Cidades | 2024 | [data] | IRS0001, IRS3002 (invertido: 100 − disposição inadequada) | [n de 1.794] | Idem |
| Ranking ABES 2026 | ABES | 2024 | [data] | Nota 0–500, categoria, taxa de DRSAI | 505 habilitados | Comparação e validação restritas aos habilitados |

**Tratamento de ausentes é decisão metodológica, não nota de rodapé.** Diga o que fez e mostre, em Resultados, que a escolha não altera o ranking de forma relevante (rode com e sem imputação, reporte o Kendall τ).

### 4.2 Alternativas

Uma frase com o universo e o critério de inclusão, seguindo a regra de dados ausentes definida em "Antes de escrever". Liste os excluídos em apêndice. Exemplo: *"Dos 1.794 municípios nordestinos, [c] dispunham dos cinco indicadores no SINISA 2025 e [k] tinham apenas um indicador ausente, imputado pela mediana de seu porte na região de saúde; esses [c + k] compõem a amostra principal. Os 505 municípios habilitados no Ranking ABES 2026 formam a subamostra de comparação."* Se a verificação da etapa 6 da regra mostrar que completos e habilitados não coincidem, ajuste a frase.

### 4.3 Critérios

A tabela de critérios é a peça central da metodologia. Os critérios são exatamente os cinco indicadores do Ranking ABES, com as mesmas regras de tratamento (limite de 100% no IES2003 e inversão do indicador de disposição inadequada). Justifique a escolha em duas frases: são os indicadores que representam os componentes do saneamento ligados às metas da Lei 14.026/2020, e usá-los torna a comparação com o ABES controlada.

| Código | Critério | Indicador SINISA | Unidade | Direção | Justificativa |
| --- | --- | --- | --- | --- | --- |
| C1 | Atendimento da população total com rede de abastecimento de água | IAG0001 | % | max | Meta 99% (Lei 14.026/2020) |
| C2 | Atendimento da população total com rede coletora de esgoto | IES0001 | % | max | Meta 90% (Lei 14.026/2020) |
| C3 | Esgoto tratado referido à água consumida | IES2003 (limitado a 100) | % | max | Meta 90% (Lei 14.026/2020) |
| C4 | Cobertura da população total com coleta de resíduos sólidos domiciliares | IRS0001 | % | max | Componente de resíduos da Lei 11.445/2007 |
| C5 | Disposição final adequada de resíduos sólidos urbanos | IRS3002 adaptado (100 − inadequada) | % | max | Fim dos lixões (Lei 14.026/2020) |

**Atenção ao C5.** No ABES, esse indicador é quase binário: muitos municípios aparecem com 0 ou 100. O CRITIC tende a dar peso alto a critérios com essa dispersão, e o C5 pode dominar o ranking. Reporte os pesos, mostre o efeito no GAIA e compare com o cenário de pesos iguais. Para o C5, uma função de preferência do tipo nível (*level*) ou usual é mais coerente que a linear. A regra dos quartis da subseção 4.4 confirma isso: aplicada ao IRS3002 dos 505 habilitados no ABES, ela dá q = 0 e p = 100 (só 23 valores distintos; 248 zeros e 236 valores 100), e a função linear vira, na prática, uma V-shape.

Regras: entre 5 e 10 critérios; verifique a correlação entre eles (matriz de Spearman em apêndice; pares com |ρ| > 0,8 exigem justificativa ou exclusão); mantenha critérios de resultado (saúde) separados dos de insumo (investimento) e diga isso no texto.

### 4.4 Funções de preferência e limiares

Esta é a subseção que os revisores mais cobram e que a maioria dos artigos omite. Para cada critério, informe a função (usual, U-shape, V-shape, nível, linear, gaussiana) e os limiares q (indiferença) e p (preferência). Nunca use a função "usual" para todos os critérios sem justificar.

Regra de derivação empírica, reproduzível e defensável: para o critério j, calcule as diferenças absolutas entre todos os pares de alternativas; q = 1º quartil dessas diferenças e p = 3º quartil. Reporte os valores na tabela de critérios (acrescente duas colunas). Exceção: no C5, use a função nível e justifique os limiares escolhidos. Em Resultados, teste q e p nos limites ±50% e mostre o efeito.

A fórmula da função linear (tipo V com indiferença) fica em destaque uma única vez:

```math
P_j(d) = \begin{cases} 0 & d \le q_j \\ \dfrac{d - q_j}{p_j - q_j} & q_j < d \le p_j \\ 1 & d > p_j \end{cases}
```

### 4.5 Pesos

O ranking principal usa pesos CRITIC; os demais esquemas são testes de robustez. A justificativa da escolha vai em duas frases: o CRITIC combina dispersão e conflito entre critérios, de modo que indicadores redundantes (coleta e tratamento de esgoto, por exemplo) não contam em dobro; e é menos sensível que o coeficiente de variação a critérios com muitos valores próximos de zero, comuns no esgotamento sanitário do interior nordestino.

| Esquema | Natureza | Como calcular | Papel no artigo |
| --- | --- | --- | --- |
| CRITIC | Objetivo (dispersão + conflito) | Desvio-padrão dos dados normalizados × Σ(1 − correlação com os demais), normalizado | Ranking principal |
| AHP Gaussiano | Objetivo (dispersão) | Fator gaussiano = desvio-padrão ÷ média de cada critério normalizado, normalizado para somar 1 | Robustez; diálogo com a literatura brasileira |
| Pesos iguais | Neutro | 1/n por critério | Isola o efeito da compensação limitada frente ao ABES, que também usa pesos iguais |
| SMAA | Estocástico | 10.000 vetores de pesos sorteados (uniformes no simplex, ou em torno dos pesos CRITIC) | Índices de aceitabilidade de posição |

Diga explicitamente que nenhum peso foi definido pelos autores. Essa frase desarma a objeção mais comum.

### 4.6 Método multicritério

Um parágrafo por etapa do PROMETHEE: grau de preferência agregado π(a,b), fluxos positivo φ⁺, negativo φ⁻ e líquido φ; PROMETHEE I (pré-ordem parcial; aqui só como diagnóstico, reportando o número de pares incomparáveis e 3 ou 4 casos emblemáticos, pois o diagrama com mais de uma centena de alternativas é ilegível) e PROMETHEE II (pré-ordem total); GAIA (projeção PCA da matriz de fluxos unicritério, com o percentual de variância explicada); SMAA-PROMETHEE (para cada vetor de pesos sorteado, calcule o ranking; o índice de aceitabilidade $b_i^r$ é a fração de sorteios em que a alternativa i fica na posição r). Cite Brans & Mareschal (2005) para o núcleo e Corrente et al. (2014) para o SMAA. Fórmulas só para φ e para $b_i^r$; o resto é referência.

```math
\phi(a) = \phi^{+}(a) - \phi^{-}(a) = \frac{1}{n-1}\sum_{b \ne a}\left[\pi(a,b) - \pi(b,a)\right]
```

### 4.7 Robustez e benchmark

Liste os testes que serão reportados em Resultados, cada um com sua métrica:

- Intervalos de estabilidade dos pesos (Visual PROMETHEE ou cálculo próprio): faixa em que cada peso pode variar sem alterar as k primeiras posições.
- Sensibilidade a q e p: ±50%, Kendall τ entre rankings.
- Reversão de ordem: retirar a melhor, a pior e uma alternativa aleatória; contar quantos pares trocam de ordem.
- Concordância entre esquemas de pesos e entre métodos (TOPSIS, VIKOR): Kendall τ e Spearman ρ.
- Comparação com o Ranking ABES 2026: Spearman ρ entre φ e a nota ABES para os municípios habilitados; matriz de transição das categorias ABES para os quartis (ou classes FlowSort) do PROMETHEE; mesmo teste com pesos iguais no PROMETHEE, para isolar o efeito da agregação.

**Software.** Nomeie biblioteca e versão exatas, tiradas do `requirements.txt` (por exemplo, pyDecision ou pymcdm para PROMETHEE e pesos); código próprio para SMAA (semente fixa); GAIA e intervalos de estabilidade também em Python, para que os scripts gerem todas as figuras. O Visual PROMETHEE (só Windows, não scriptável) serve apenas para conferir os resultados. Link para o repositório. Sem isso, revisores de MCDA costumam pedir os dados e o código.

## Seção 5 — Resultados e discussão

Os resultados respondem às perguntas de pesquisa na ordem em que foram feitas: PP, PS1, PS2, PS3, PS4. Cada subseção abre com a resposta em uma frase e só depois mostra a evidência. Separe o que o dado mostra (resultado) do que isso significa (discussão); muitos periódicos aceitam as duas coisas na mesma seção, mas o revisor precisa distinguir uma da outra.

**Sequência recomendada de exibições** (quatro a cinco exibições no corpo; o excedente vai para material suplementar):

| # | Exibição | Responde a | O que mostrar |
| --- | --- | --- | --- |
| T1 | Estatística descritiva da matriz de decisão | contexto | média, mediana, mín., máx. por critério; n válido |
| T2 | Pesos por esquema (CRITIC, AHP Gaussiano, iguais, SMAA médio) | 4.5 | uma coluna por esquema; destaque o critério mais e o menos ponderado |
| F1 | Ranking PROMETHEE II (φ) — top 20 e bottom 20 | PP | barras horizontais; não liste todos os municípios no corpo do texto |
| F2 | Pré-ordem parcial PROMETHEE I | PP | número de pares incomparáveis e 3 ou 4 casos emblemáticos (não o diagrama completo) |
| F3 | Plano GAIA | PS1 | alternativas, eixos de critérios e o bastão de decisão; variância explicada (δ) no rodapé |
| F4 | Índices de aceitabilidade SMAA | PS2 | mapa de calor alternativa × posição (ou faixa de posições com 90% de aceitabilidade) |
| T3 | Testes de robustez | PS2 | intervalos de estabilidade, Kendall τ por variação de q/p, reversões de ordem |
| F5/T4 | Comparação com o benchmark | PS3 | dispersão φ × nota ABES; matriz de transição categoria ABES (3 categorias no Nordeste, uma com só 7 municípios) × quartil PROMETHEE; tabela dos municípios que mais mudam |
| F6 | Validação externa | PS4 | dispersão da taxa de DRSAI × φ e × nota ABES, com os Spearman ρ; em suplemento se faltar espaço |

**Como escrever cada subseção:**

*5.1 Ranking principal (PP).* Abra com os três primeiros e os três últimos, com os valores de φ. Em seguida, descreva o padrão geográfico ou estrutural (estado × estado, litoral × sertão, capital × interior, prestador regional × local). Não narre a tabela; interprete-a. Use PROMETHEE I para apontar as incomparabilidades mais informativas: *"Município A domina em água e perde em esgoto; Município B, o inverso. O PROMETHEE II os aproxima, mas o PROMETHEE I mostra que essa aproximação esconde perfis opostos."*

*5.2 Critérios discriminantes (PS1).* Leia o GAIA: critérios com vetores longos discriminam; vetores opostos indicam conflito (trade-off); o bastão de decisão aponta o compromisso sob os pesos adotados. Cruze com os pesos CRITIC. Afirme explicitamente quando o resultado é intuitivo ("tratamento de esgoto é o critério mais discriminante, como esperado") e quando não é.

*5.3 Robustez (PS2).* É a subseção que converte um estudo de caso em contribuição. Reporte: (a) quantas alternativas têm a mesma posição em mais de 90% dos sorteios SMAA; (b) a faixa de variação de cada peso que preserva o top 10; (c) o Kendall τ entre os rankings com q/p ±50% (acima de 0,9 é estável); (d) o número de pares que trocam de ordem ao retirar alternativas. Conclua com uma frase de julgamento: *"O ranking é robusto nas posições extremas e instável no terço central, onde pequenas variações de peso trocam posições vizinhas."*

*5.4 Comparação com o Ranking ABES (PS3).* Reporte o Spearman ρ entre φ e a nota ABES para os municípios habilitados, primeiro com pesos CRITIC e depois com pesos iguais. A versão com pesos iguais é o experimento central: como os dois métodos usam a mesma base, o mesmo ano e os mesmos pesos, toda diferença vem da regra de agregação (compensatória no ABES, de compensação limitada no PROMETHEE). Como só três categorias do ABES aparecem entre os habilitados do Nordeste, e uma delas tem apenas 7 municípios, a matriz de transição é pouco informativa; a comparação por quartis da nota ABES é mais útil. Em seguida, concentre-se nas divergências. Para cada município que muda de quartil ou de categoria, uma linha explicando o porquê. Quase sempre é desempenho muito desigual entre critérios, como um zero em disposição de resíduos ou em tratamento de esgoto compensado por bons índices nos demais. Esta é a parte que interessa ao gestor e ao editor de política pública.

*5.5 Validação externa com DRSAI (PS4).* Calcule a correlação de Spearman entre a taxa de internações por DRSAI e, de um lado, a nota ABES, do outro, o fluxo líquido φ. Se o φ se associar mais fortemente à saúde, há um argumento de validade a favor da compensação limitada. Se não, isso também é um achado e deve ser discutido. Use linguagem de associação: internações dependem de muitos fatores além do saneamento, e há municípios com taxas atípicas no apêndice do ABES.

*5.6 Discussão.* Três a cinco parágrafos: (1) o que os resultados dizem sobre o problema real (distância da meta de 2033); (2) o que confirmam e o que contradizem na literatura citada no bloco 3.1; (3) o que a abordagem de compensação limitada acrescentou ao que o índice oficial já dizia; (4) implicações para a política pública, com cautela (*"sugerem priorizar"*, não *"demonstram que se deve"*); (5) uma ponte para as limitações.

**Erros comuns:**

- Tabela com todas as posições no corpo do texto. Vai para apêndice ou suplemento.
- Figura GAIA sem o δ (variância explicada). Abaixo de 60%, o plano é pouco confiável e isso precisa ser dito.
- Reportar robustez em uma frase ("o ranking mostrou-se estável") sem métrica.
- Concluir causalidade. O ranking descreve; não explica por que o município está onde está.
- Discutir só os municípios do topo. As mudanças de posição no meio e na base são o achado.

## Seção 6 — Limitações e trabalhos futuros

Limitações bem escritas aumentam a credibilidade; mal escritas parecem desculpa. A regra: cada limitação vem com (a) o que ela afeta, (b) o que foi feito para mitigá-la e (c) o trabalho futuro que a resolve. Três a cinco limitações bastam; mais do que isso sugere que o estudo não deveria ter sido feito.

**Tipologia das limitações** (escolha as que se aplicam e redija uma por parágrafo curto):

| Tipo | Exemplo (Ideia 1) | Mitigação já feita | Trabalho futuro |
| --- | --- | --- | --- |
| Dados: cobertura | 1.289 dos 1.794 municípios não habilitados no ABES, com cobertura de 3% no Piauí a 52% no Ceará; [n] sem os cinco indicadores no SINISA 2025 | Imputação de 1 indicador ausente; testes só com completos e com imputação total; Kendall τ reportado | Repetir com as próximas edições do SINISA |
| Dados: autodeclaração | Indicadores informados pelos prestadores, sem auditoria | Validação externa com DRSAI | Incorporar o módulo de regulação do SINISA quando publicado |
| Dados: quebra de série | SNIS e SINISA têm definições distintas; a própria ABES pede cautela na comparação entre edições | Análise restrita a um ano-base | PROMETHEE temporal quando houver três ou mais edições do SINISA |
| Critérios: só acesso | Os cinco indicadores medem cobertura e destinação, não qualidade, perdas ou investimento | Escolha justificada pela comparação controlada com o ABES | Modelo ampliado com perdas, investimento e qualidade da água |
| Método: pesos objetivos | CRITIC reflete o que os dados discriminam, não a prioridade política | AHP Gaussiano, pesos iguais e SMAA | PROMETHEE-GDSS com representantes das companhias estaduais de saneamento, das agências reguladoras e das prefeituras |
| Método: limiares empíricos | q e p derivados dos quartis das diferenças | Sensibilidade ±50% | Elicitação de limiares com especialistas |
| Escopo: benchmark parcial | ABES só inclui municípios com todos os indicadores | Comparação restrita aos habilitados | Comparação com outros índices (IDSC-BR, ODS 6) |
| Escopo: inferência | Ranking é descritivo; não identifica causas | Linguagem de associação na discussão | Modelo explicativo (ML + SHAP) sobre o fluxo líquido |

**Como redigir cada parágrafo.** Modelo: *"A principal limitação decorre da cobertura do SINISA 2025: dos 1.794 municípios nordestinos, [n] não dispunham dos cinco indicadores, e o Ranking ABES exclui 1.289. Este estudo manteve os que tinham apenas um indicador ausente, imputado pela mediana de seu porte na região de saúde; o ranking restrito aos municípios completos concorda com o principal em τ = [valor]. A repetição do estudo com as edições seguintes do SINISA é o desdobramento natural."*

**Trabalhos futuros que valem a pena mencionar** (escolha dois ou três; os demais ficam implícitos na tabela):

- Extensão temporal com Temporal PROMETHEE II assim que houver três ou mais edições do SINISA.
- Validação com decisores reais via PROMETHEE-GDSS, transformando o estudo de dados secundários em instrumento de gestão.
- Replicação para outras UFs do Nordeste ou para o Brasil inteiro, com análise de equidade regional.
- Camada explicativa com aprendizado de máquina e SHAP sobre o fluxo líquido, ligando posição no ranking a fatores contextuais (renda, porte, modelo de prestação).

**Erros comuns:**

- Listar limitações sem mitigação nem desdobramento. Vira uma lista de defeitos.
- Apresentar como limitação algo que era escolha de escopo. Escolha de escopo se justifica na Seção 2.
- Prometer trabalhos futuros genéricos ("aplicar outros métodos"). Cada trabalho futuro deve nascer de uma limitação nomeada.
- Omitir a limitação de dados autodeclarados. O revisor vai apontá-la.

## Seção 7 — Conclusão

A conclusão responde à pergunta de pesquisa em uma frase, com número, e não traz nada que não esteja nos Resultados. Escreva-a em dois parágrafos curtos.

**Parágrafo 1 — Resposta e contribuição.** Responda à PP literalmente, com o principal número (por exemplo, quantos municípios mudam de quartil em relação ao ABES e o Spearman ρ com pesos iguais). Em seguida, uma frase para cada contribuição da Introdução, na mesma ordem dos três bullets.

**Parágrafo 2 — Implicação e próximo passo.** Uma frase sobre o que gestores e reguladores podem fazer com o ranking (com a cautela da Discussão) e uma frase com o trabalho futuro mais importante da Seção 6.

**O que não fazer:**

- Não repita o resumo nem a metodologia.
- Não introduza resultado, citação ou limitação nova.
- Não termine com frase genérica ("mais estudos são necessários"); termine com o próximo passo concreto.

## Referências

Um artigo de anais com 12 a 15 páginas comporta entre 25 e 40 referências, distribuídas em quatro grupos. A lista abaixo é o núcleo; corte para caber no limite. Confira cada DOI antes de incluir.

**Grupo A — Núcleo PROMETHEE (obrigatório, 6 a 8 referências):**

- Brans, J.P.; Vincke, Ph. (1985). A preference ranking organisation method: The PROMETHEE method for MCDM. *Management Science*, 31(6), 647–656.
- Brans, J.P.; Mareschal, B. (2005). PROMETHEE methods. In: Figueira, J.; Greco, S.; Ehrgott, M. (eds.), *Multiple Criteria Decision Analysis: State of the Art Surveys*. Springer, cap. 5.
- Brans, J.P.; Vincke, Ph.; Mareschal, B. (1986). How to select and how to rank projects: The PROMETHEE method. *EJOR*, 24(2), 228–238.
- Mareschal, B.; Brans, J.P. (1988). Geometrical representations for MCDA (GAIA). *EJOR*, 34(1), 69–77.
- Behzadian, M.; Kazemzadeh, R.B.; Albadvi, A.; Aghdasi, M. (2010). PROMETHEE: A comprehensive literature review on methodologies and applications. *EJOR*, 200(1), 198–215. DOI 10.1016/j.ejor.2009.01.021.
- Corrente, S.; Figueira, J.R.; Greco, S. (2014). The SMAA-PROMETHEE method. *EJOR*, 239(2), 514–522.
- Yu, D.; Liu, Y.; Xu, Z. (2023). Analysis of knowledge evolution in PROMETHEE: A longitudinal and dynamic perspective. *Information Sciences*, 642, 119151.

**Grupo B — Robustez, pesos e variantes recentes (6 a 10 referências):**

- Liu, Y.; Liu, J. (2024). Sensitivity analysis of the parameters for preference functions and rank reversal analysis in the PROMETHEE II method. *Omega*, 128, 103116.
- Diakoulaki, D.; Mavrotas, G.; Papayannakis, L. (1995). Determining objective weights in multiple criteria problems: The CRITIC method. *Computers & Operations Research*, 22(7), 763–770.
- Santos, M.; Costa, I.P.A.; Gomes, C.F.S. (2021). Multicriteria decision-making in the selection of warships: a new approach to the AHP method. *International Journal of the Analytic Hierarchy Process*, 13(1). (Origem do AHP Gaussiano; confira os dados da referência.)
- Lahdelma, R.; Salminen, P. (2001). SMAA-2: Stochastic multicriteria acceptability analysis for group decision making. *Operations Research*, 49(3), 444–454.
- Wątróbski, J.; Bączkiewicz, A.; Ziemba, E.; Sałabun, W. (2023). Temporal PROMETHEE II — New multi-criteria approach to sustainable management of alternative fuels consumption. *Journal of Cleaner Production*, 413, 137445.
- Costa, H.G.; Lima, G.B.A. (2026). Inequalities matter when prioritizing sustainable goals: a novel multi-criteria-clustering modeling (KRP2). *Annals of Operations Research*. DOI 10.1007/s10479-026-07125-w. (Referência ainda não conferida.)
- Tarnanidis, T.; Papathanasiou, J.; Mareschal, B. et al. (2026). Sustainable value creation in global marketing decisions: a systematic PRISMA review of PROMETHEE applications. *Journal of Marketing Analytics*. DOI 10.1057/s41270-026-00486-y. (Referência ainda não conferida.)
- Pereira, V.; Basilio, M.P.; Santos, C.H.T. (2024). pyDecision: a comprehensive library of MCDA methods in Python. arXiv:2404.06370.

**Grupo C — Domínio de aplicação (10 a 15 referências).** Para a Ideia 1: estudos de desempenho em saneamento no Brasil (DEA, índices, regressão), metodologias do Ranking ABES e do Ranking do Trata Brasil, literatura internacional sobre benchmarking de utilities (Berg; Marques; Walter et al.), saúde e saneamento (DRSAI), marco regulatório (Heller; Britto). Metade deve ser de 2020 em diante.

**Grupo D — Bases, normas e documentos oficiais (5 a 10 referências).** Cite como documento, com órgão, título, ano e URL com data de acesso:

- BRASIL. Lei nº 14.026, de 15 de julho de 2020 (Marco Legal do Saneamento).
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório dos Serviços de Abastecimento de Água* (ano de referência 2024). Brasília, dez. 2025.
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório dos Serviços de Esgotamento Sanitário* (ano de referência 2024). Brasília, dez. 2025.
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório de Gestão Municipal* (ano de referência 2024). Brasília, dez. 2025.
- ABES — ASSOCIAÇÃO BRASILEIRA DE ENGENHARIA SANITÁRIA E AMBIENTAL. *Ranking ABES da Universalização do Saneamento 2026*. 2026.
- BRASIL. Ministério da Saúde. DATASUS. Sistema de Informações Hospitalares do SUS (SIH/SUS). Acesso em [data].
- BRASIL. Ministério das Cidades. *PLANSAB — Plano Nacional de Saneamento Básico*, revisão vigente.

**Gestão das referências.** Use Zotero ou Mendeley desde o primeiro dia, com o estilo do modelo Springer indicado pela organização do Rii Forum. Exporte a biblioteca em `.bib` para o repositório. Antes de submeter, confira: todo item citado está na lista e todo item da lista está citado; DOIs resolvem; nenhuma referência aparece em duas versões (preprint e publicada). Documentos brasileiros (leis, relatórios do SINISA, ABES) devem ter título traduzido entre colchetes.

## Título, resumo, palavras-chave e destaques

Estes quatro elementos são escritos por último e são os únicos que a maioria dos leitores vai ler. O editor decide por eles se o artigo vai a revisores.

**Título (12 a 16 palavras).** Fórmula: *[o que o método faz] + [objeto] + [contexto] + [sinal metodológico]*. Evite dois-pontos seguidos de subtítulo genérico ("a multicriteria approach"). Exemplos:

- *Same data, different priorities: how the aggregation rule of a public sanitation ranking shapes municipal prioritisation in Northeast Brazil*
- *Limited-compensation PROMETHEE versus an additive public ranking: evidence from sanitation universalisation in the municipalities of Northeast Brazil*

**Resumo (no formulário do Rii Forum, siga o limite indicado no próprio formulário, que a chamada não informa; no artigo completo, siga o limite do modelo Springer, em geral até 250 palavras), estruturado mesmo que o evento não exija.** Uma ou duas frases por item, sem citações:

1. Contexto e problema (com um número).
2. Lacuna (uma frase).
3. Objetivo e pergunta.
4. Método: alternativas, número de critérios, base de dados, variante PROMETHEE, esquemas de pesos, testes de robustez.
5. Resultado principal com número (ex.: *"[n] dos [m] municípios habilitados mudam de quartil em relação ao ranking oficial; o ranking é estável nas 15 primeiras posições em 94% dos cenários SMAA"*).
6. Implicação para a política pública (uma frase).
7. Contribuição metodológica (uma frase).

**Palavras-chave (5 a 6).** Combine: o método (PROMETHEE; SMAA), o objeto (sanitation; municipal performance), o contexto (Brazil; semi-arid), e um termo de busca da área (multicriteria decision aid; public policy). Não repita palavras do título; elas já são indexadas.

**Destaques / Highlights (não exigidos pelos anais Springer; use-os como roteiro do resumo e dos slides).** Um resultado por bullet, nunca uma descrição do que foi feito:

- Limited-compensation PROMETHEE ranks [c + k] of Northeast Brazil's 1,794 municipalities, [m] more than the official ranking
- [n] municipalities change quartile when criteria compensation is limited
- Equal-weight PROMETHEE vs ABES ranking isolates the effect of aggregation
- Top-15 ranking is stable in [x]% of SMAA weight scenarios
- CRITIC and Gaussian AHP weights converge (Kendall τ = [valor])

**Teste final:** entregue título, resumo e highlights a alguém da área que não leu o artigo e peça para dizer, em uma frase, qual foi o achado. Se a pessoa descrever o método em vez do achado, reescreva.

## Checklist final e resposta a revisores

**Antes de submeter:**

- [ ] Cada seção abre com sua frase-ponto; o artigo pode ser lido só pelas primeiras frases
- [ ] Pergunta de pesquisa respondida literalmente na Discussão e no Resumo, com número
- [ ] Os três bullets de contribuição da Introdução correspondem a resultados reportados
- [ ] Tabela-síntese da revisão inclui o próprio artigo na última linha
- [ ] Tabela de critérios com unidade, direção, fonte, função de preferência, q e p
- [ ] Pesos: CRITIC principal e esquemas de robustez (AHP Gaussiano, pesos iguais, SMAA) descritos; frase explícita de que nenhum peso foi definido pelos autores
- [ ] Robustez reportada com métricas (aceitabilidade SMAA, intervalos de estabilidade, τ para q/p, reversão de ordem)
- [ ] Comparação com o Ranking ABES 2026 feita (com pesos CRITIC e com pesos iguais) e discutida município a município nas divergências
- [ ] GAIA com variância explicada (δ) informada
- [ ] Todas as figuras legíveis em preto e branco; eixos com unidades; legendas autossuficientes
- [ ] Data de extração de cada base no texto; URL e ano-base nas referências
- [ ] Repositório público com dados tratados, scripts e `README`; DOI (Zenodo) citado
- [ ] Limitações com mitigação e trabalho futuro para cada uma
- [ ] Referências conferidas (DOI resolve; citado ↔ listado)
- [ ] Formato dos anais: modelo Springer, limite de páginas confirmado com a organização, resumo, palavras-chave, texto em inglês revisado
- [ ] Resumo enviado pelo formulário do Rii Forum até 15/11/2026, dentro do limite do formulário e com a trilha escolhida; artigo completo até 30/12/2026

**Roteiro de resposta a revisores.** A resposta é um documento à parte, com uma tabela de três colunas (comentário do revisor, resposta, alteração no manuscrito com página/linha). Regras:

1. Responda a todos os comentários, inclusive os elogiosos, na ordem em que vieram.
2. Para cada crítica, faça a mudança pedida ou explique, com evidência, por que não. "Discordamos" sem evidência não é resposta.
3. Quando a crítica for sobre pesos ou sensibilidade, aponte a tabela/figura que já existe e, se preciso, acrescente o teste pedido em material suplementar.
4. Quando a crítica for sobre novidade, remeta aos três bullets de contribuição e à tabela-síntese; se o revisor citar um estudo que você não conhecia, inclua-o na tabela e mostre a diferença.
5. Nunca altere o resultado principal para agradar o revisor; altere a apresentação, os testes e a discussão.

**Objeções mais prováveis para um artigo PROMETHEE aplicado e a resposta pronta:**

| Objeção | Onde a resposta já está | O que acrescentar, se pedido |
| --- | --- | --- |
| "Por que PROMETHEE e não TOPSIS/AHP/ELECTRE?" | Bloco 3.2 (compensação limitada, incomparabilidades, GAIA) | Tabela de concordância com TOPSIS/VIKOR em suplemento |
| "Os pesos são arbitrários" | Seção 4.5 e Tabela T2 | Gráfico de walking weights |
| "Não há análise de sensibilidade" | Seção 5.3 e Tabela T3 | Variação de q/p por critério individual |
| "Os dados são autodeclarados" | Seção 6, limitação 2 | Correlação entre SINISA e SIH/SUS como validação cruzada |
| "O caso é local demais" | Introdução, parágrafo 1 e Discussão | Parágrafo ligando o Nordeste ao semiárido global e a economias emergentes |
| "Qual a contribuição teórica?" | Introdução, bullet 2, e Discussão item 3 | Uma frase sobre o que o contraste entre agregação compensatória e de compensação limitada ensina sobre índices oficiais em geral |
