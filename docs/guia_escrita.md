# Guia de Escrita — Artigo Aplicado de Análise Multicritério

Guilherme de Farias · 5 out. 2026 · revisado em 24 out. 2026 (escopo ampliado do Ceará para o Nordeste), em 2 nov. 2026 (pergunta principal reformulada em torno da validade externa com a DRSAI) e em 8 nov. 2026 (inclusão dos métodos compensatórios AHP clássico e AHP Gaussiano)

## Como usar este guia

Este guia cobre as sete seções do artigo na ordem em que serão lidas (Introdução, Pergunta e escopo, Revisão, Metodologia, Resultados e discussão, Limitações, Conclusão), mais as Referências, com o que cada uma precisa conter, parágrafos-modelo e os erros que mais levam à rejeição. O exemplo condutor é o projeto deste repositório: o desempenho em saneamento dos municípios do Nordeste com a base SINISA 2025 (ano-base 2024), ordenado por quatro métodos de agregação (soma ponderada, TOPSIS, VIKOR e PROMETHEE II) com quatro esquemas de pesos (iguais, CRITIC, AHP Gaussiano e AHP clássico, este com pesos de Saaty), e os 16 rankings resultantes comparados entre si, com o Ranking ABES da Universalização do Saneamento 2026 e com a taxa de internações por DRSAI.

**Tamanho-alvo** para os anais do Rii Forum 2027, publicados pela Springer e indexados na Scopus, escritos em inglês. A chamada (`Rii2027 call for papers 2027-09-30.pdf`, na raiz do repositório) não informa a série dos anais nem o limite de páginas; o planejamento abaixo assume 12 a 15 páginas no modelo Springer, cerca de 4.500 a 5.500 palavras com referências. Confirme o limite com info@rii-forum.org antes de começar a cortar.

| Seção | Palavras | Figuras/tabelas típicas |
| --- | --- | --- |
| Introdução ao problema | 500–650 | nenhuma |
| Pergunta de pesquisa e escopo | 150–250 | nenhuma |
| Revisão de literatura | 700–900 | 1 tabela-síntese de estudos anteriores |
| Metodologia | 900–1.200 | tabela de critérios, tabela de pesos |
| Resultados e discussão | 1.200–1.500 | divergência entre os 16 rankings, validade com a DRSAI, perfil dos que mudam, robustez (4 a 5 exibições no total) |
| Limitações e trabalhos futuros | 250–350 | nenhuma |
| Conclusão | 150–250 | nenhuma |
| Referências (fora da contagem de seções) | 25–40 itens | — |

**Convenções adotadas ao longo do guia:**

- Cada seção começa pelo seu ponto principal. O leitor (e o revisor) deve conseguir ler só a primeira frase de cada seção e entender o argumento.
- Parágrafos de 3 a 5 frases. Frases com menos de 25 palavras sempre que possível.
- Toda afirmação sobre o estado da arte leva citação. Toda afirmação sobre dado leva fonte, ano-base e data de extração.
- Escreva os Resultados antes da Introdução. A introdução promete o que os resultados entregam, então ela só pode ser finalizada depois.
- Mantenha o arquivo [`log_decisoes.md`](log_decisoes.md) com cada escolha metodológica e sua justificativa. Ele vira a seção de Metodologia e as respostas aos revisores.

## Antes de escrever: o que precisa estar fechado

Não comece a redigir antes de fechar as nove decisões abaixo. Cada uma aparece em pelo menos três seções do artigo, e mudá-la depois obriga a reescrever tudo.

| Decisão | Situação | Escolha | Onde aparece no artigo |
| --- | --- | --- | --- |
| Unidade de análise (alternativas) | Fechada | Os 1.794 municípios dos nove estados do Nordeste (AL, BA, CE, MA, PB, PE, PI, RN, SE) como universo; entram no ranking os que têm dados suficientes (regra abaixo) | Escopo, Metodologia, Resultados |
| Recorte temporal e base | Fechada | SINISA 2025 (ano-base 2024); SINISA 2024 (ano-base 2023) só como contexto, ainda não baixado para `dados/SINISA/2024/` | Escopo, Dados, Limitações |
| Conjunto de critérios | Fechada | Os cinco indicadores do Ranking ABES: IAG0001, IES0001, IES2003, IRS0001 e IRS3002 (adaptado) | Revisão, Metodologia, Resultados |
| Pesos | Fechada | Quatro esquemas cruzados com todos os métodos: pesos iguais, CRITIC, AHP Gaussiano e AHP clássico (Saaty, único subjetivo); SMAA com 10.000 vetores como teste de robustez | Metodologia, Resultados, Limitações |
| Métodos compensatórios AHP | Fechada (8 nov. 2026) | AHP clássico (matriz de Saaty preenchida pelo autor, pesos pela média geométrica das linhas, RC = 0,0152) e AHP Gaussiano (pesos pelo coeficiente de variação), ambos com soma ponderada dos valores normalizados pela soma. Os dois entram como colunas de pesos do desenho cruzado: as células soma ponderada × AHP Gaussiano e soma ponderada × AHP clássico são os dois AHP da literatura, e os pesos de Saaty também alimentam TOPSIS, VIKOR e PROMETHEE II, o que eleva o total a 16 rankings. Calculados em `planilhas/` e comparados com o ABES no [parecer técnico](Parecer%20técnico%20dos%20métodos%20multicritério.md) | Revisão, Metodologia, Resultados, Limitações |
| Métodos de agregação | Fechada | Soma ponderada (compensação total; é a regra do ABES), TOPSIS (total), VIKOR (parcial) e PROMETHEE II (limitada), o que, com os quatro esquemas de pesos, dá 16 rankings; PROMETHEE II com CRITIC é o ranking de referência para GAIA, PROMETHEE I (diagnóstico) e SMAA-PROMETHEE | Revisão, Metodologia, Resultados |
| Benchmark externo | Fechada | Ranking ABES da Universalização do Saneamento 2026 (mesma base, ano e critérios; soma com pesos iguais; 4 categorias nacionais, das quais 3 aparecem entre os habilitados do Nordeste, uma delas com só 7 municípios). A soma ponderada com pesos iguais sobre as notas brutas reproduz exatamente a pontuação do ABES nos 505 habilitados | Introdução, Resultados, Discussão |
| Validade externa | Fechada | Taxa de internações por DRSAI do arquivo do ABES, só para avaliar os rankings, nunca como critério; Spearman, bootstrap de Δρ e controle mínimo por UF e porte; renda, atenção primária e acesso hospitalar ficam como limitação | Pergunta, Metodologia, Resultados, Limitações |
| Veículo | Fechada | Rii Forum 2027 (Roma; anais pela Springer, Scopus); texto em inglês | Todo o texto |

**Decisão derivada: normalização da soma ponderada.** O parecer técnico dos AHP mostrou que a normalização muda o ranking mesmo com pesos fixos. O ABES soma as notas brutas (0 a 100) com pesos iguais; os dois AHP dividem cada indicador pela sua soma nos 505 municípios e só então aplicam os pesos. Aplicar 20% a cada valor normalizado pela soma não reproduz o ABES (ρ = 0,95, deslocamento médio de 33 posições), porque pesos iguais nas notas brutas equivalem, na escala normalizada, a pesos proporcionais à soma de cada indicador: Coleta 31,3%, Água 26,7%, Destinação 18,7%, Esgoto 13,7% e Tratamento 9,5%. Para comparar pesos entre métodos, use sempre esses pesos equivalentes do ABES. Com os pesos CRITIC, a normalização é min-max (pior município = 0, melhor = 1) tanto no cálculo dos pesos quanto na soma ponderada. A normalização pela soma foi descartada para o CRITIC: com ela, o desvio-padrão de cada indicador vira CV ÷ 505 e, como o fator de conflito varia pouco entre os critérios (3,26 a 3,88), o CRITIC reproduziria o AHP Gaussiano (ρ = 0,998 entre os dois rankings). O min-max é a normalização do artigo original (Diakoulaki et al., 1995) e mantém o peso na mesma escala em que ele é aplicado. A decisão está registrada no [`log_decisoes.md`](log_decisoes.md).

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

A amostra (só os completos) deixa de fora 1.289 dos 1.794 municípios, e quase todo o Maranhão e o Piauí, provavelmente os pequenos municípios do interior com pior saneamento. Esse viés de cobertura entra nas Limitações. A desigualdade de cobertura entre estados também é um achado: registre-a e teste se o ranking muda quando cada estado é retirado.

**Armadilha do arquivo do ABES:** nele, dado ausente aparece como "0,00", e não como célula vazia. Não é possível distinguir ausência de zero verdadeiro: entre os 505 habilitados, 248 têm 0 em IRS3002, 154 em IES2003 e 1 em IES0001 e em IAG0001. Nunca use os zeros dos 1.289 não habilitados como valores no PROMETHEE, porque eles contariam como o pior desempenho possível. A taxa de DRSAI também vale 0,00 em 789 municípios, 145 deles habilitados; trate esses casos como ausentes na validação. Entre os 505 municípios da amostra, sobram 360 com taxa válida. Os números estão gravados como texto, com vírgula decimal e ponto de milhar (100 taxas de DRSAI passam de 1.000, como `10.220,55`), e precisam ser convertidos removendo o ponto antes de trocar a vírgula (no Calc: Dados → Texto para colunas, idioma Português do Brasil).

**Regra adotada:**

1. Extrair os cinco indicadores das planilhas da Base Municipal do SINISA 2025 em `dados/SINISA/2025/` para os 1.794 municípios do Nordeste (filtro pela coluna `Macrorregião` = `Nordeste`), onde o ausente aparece como vazio. Para o IAG0001, usar a versão retificada (`SINISA_AGUA_Indicadores_Base Municipal_2024_Retificação.xlsx`) e registrar isso no `log_decisoes.md`. Município que não aparece na planilha conta como ausente em todos os indicadores dela: a de indicadores de água traz 1.528 dos 1.794 municípios nordestinos (BA 406, PB 214, CE 182, PE 180, MA 175, RN 163, AL 97, SE 75 e só 36 do PI).
2. Classificar cada município pelo número de indicadores faltantes entre os quatro contabilizados (IAG0001, IES0001, IES2003 e IRS0001). Se o IRS3002 estiver ausente, assume-se disposição final inadequada (valor adaptado 0), e ele não conta como faltante.
3. **Amostra:** só os completos (505). Todo município com algum dos quatro ausentes fica fora e é listado em apêndice.
4. Registrar no `log_decisoes.md` quantos municípios caem em cada classe e quais indicadores faltam com mais frequência.
5. **Verificar** se os completos no SINISA coincidem com os 505 habilitados no ABES. É a hipótese de trabalho, mas a habilitação do ABES pode ter outras exigências e o arquivo do ABES grava ausência como 0,00. A subamostra de comparação com o ABES é sempre a dos habilitados; se as duas listas divergirem, registre quais municípios diferem e por quê.

Daqui em diante, "amostra" designa os 505 municípios completos, que coincidem com os habilitados no ABES. Nenhum deles tem o IRS3002 ausente, então a presunção de disposição inadequada não altera nenhum valor da amostra atual; ela fica registrada como regra para as próximas edições. Usar a mesma amostra do ABES tem uma vantagem: a soma ponderada com pesos iguais reproduz exatamente a nota oficial, o que dá ao artigo uma âncora verificável.

**Consequência de usar os mesmos critérios do ABES.** Com base, ano e critérios idênticos, toda diferença entre os 16 rankings vem do método de agregação, dos pesos ou da normalização, e o desenho cruzado separa o efeito da agregação do efeito dos pesos. Como o ABES traz a taxa de internações por DRSAI de cada município, ela serve de teste de validade externa: qual das ordenações se associa mais fortemente à saúde? Esse é o argumento central do artigo. Três princípios valem em todo o texto:

1. **O ranking é só de saneamento.** A DRSAI não entra como critério nem calibra parâmetros. Métodos, pesos e limiares são fixados antes de olhar a DRSAI e registrados no `log_decisoes.md`; nada é escolhido pelo que dá a maior correlação. Isso vale também para a matriz de Saaty do AHP clássico: registre que ela foi preenchida antes de qualquer correlação com a DRSAI e não a altere depois.
2. **Validade externa não é robustez.** Robustez é o ranking se manter quando mudam os pesos ou os limiares (SMAA, sensibilidade a q e p). Validade externa é o ranking se associar a um desfecho que ele deveria refletir. As duas análises ficam em subseções separadas.
3. **A compensação explica o resultado.** Os métodos diferem principalmente em quanto deixam um indicador bom compensar um ruim. A hipótese é que o risco sanitário depende do componente mais fraco (boa água não protege quem não tem esgoto tratado), e que por isso métodos de compensação limitada se associariam melhor à DRSAI. Ela entra como pergunta secundária.

### Cronograma até o Rii Forum 2027

| Data | Marco | Tipo |
| --- | --- | --- |
| 1 nov. 2026 | Fim da inscrição com desconto (on-line 300 EUR, depois 350 EUR; presencial 550 EUR, depois 650 EUR) | Prazo do evento |
| até 2 nov. 2026 | Dados do SINISA 2025 e do apêndice do ABES extraídos e matriz montada | Interno |
| 8 nov. 2026 | AHP clássico e AHP Gaussiano calculados nas planilhas de `planilhas/` e comparados com o ABES no parecer técnico (`docs/`) | Interno |
| até 12 nov. 2026 | Os 16 rankings rodando e primeira correlação com a DRSAI, para saber se a pergunta principal tende a uma resposta afirmativa; primeiros números para o resumo | Interno |
| 15 nov. 2026 | Envio do resumo pelo formulário do site (limite de palavras a confirmar no formulário) | Prazo do evento |
| até 30 nov. 2026 | Bootstrap de Δρ, controle por UF e porte, SMAA, sensibilidade a q/p e comparação com o ABES concluídos | Interno |
| até 20 dez. 2026 | Versão completa revisada, no modelo Springer | Interno |
| 30 dez. 2026 | Envio do artigo completo | Prazo do evento |
| 6 abr. 2027 | Apresentações on-line | Evento |
| 8–9 abr. 2027 | Apresentações presenciais em Roma | Evento |

**Trilha sugerida no formulário:** *Artificial Intelligence, Algorithms and Data-Driven Governance*, com o enquadramento de que rankings públicos são instrumentos algorítmicos de priorização, de que a regra de agregação muda quem é priorizado e de que um desfecho de saúde ajuda a julgar qual regra é mais coerente. Alternativas: *Complexity Management and Decision Support Systems*, a trilha mais próxima do método, e *Politics, Public Policy, Democracy and Regulation*, a mais conservadora.

**Checklist de reprodutibilidade** (o que precisa existir antes do primeiro parágrafo):

- [x] Dados brutos baixados em `dados/` (SINISA 2025 e ABES 2026), com a URL de origem nos arquivos `.url`
- [ ] Data de extração de cada base registrada no `log_decisoes.md` (registradas as datas dos commits como limite superior; falta confirmar a data real de download)
- [ ] Conjunto de notebooks numerados em `jupyter notebooks/` (já existe `01_filtragem_municipios`; faltam pesos, os 16 rankings, validade com a DRSAI e robustez; o AHP clássico e o AHP Gaussiano, hoje em planilhas do LibreOffice, também precisam ser portados para notebook) que gera todas as tabelas e figuras a partir dos dados brutos, com as versões das bibliotecas em `requirements.txt`
- [x] Matriz de decisão gerada: `resultados/municipios_5_indicadores.csv` (505 alternativas), com as alternativas nas linhas e os critérios nas colunas
- [x] Tabela de critérios com nome, unidade, direção (max/min), fonte, função de preferência, limiares q e p (no `log_decisoes.md`, seções 3 e 4)
- [x] Dicionário de pesos para cada esquema, com o cálculo documentado (`log_decisoes.md`, seção 6, com os pesos iguais também na escala normalizada pela soma)
- [x] Métodos, pesos e parâmetros (q, p e v) registrados no `log_decisoes.md` antes de calcular qualquer correlação com a DRSAI (congelados em 9 nov. 2026)
- [x] Repositório no GitHub criado
- [ ] Repositório ligado ao Zenodo para receber o DOI antes da submissão
- [x] `log_decisoes.md` iniciado (`docs/log_decisoes.md`)

Se algum item não puder ser cumprido (por exemplo, a base não permite redistribuição), registre isso agora: será uma frase na seção de Dados e outra em Limitações.

## Seção 1 — Introdução ao problema a ser resolvido

A introdução tem um único objetivo: convencer o revisor, em cinco parágrafos, de que existe um problema real, que a forma atual de medi-lo é inadequada, e que o artigo entrega algo que não existia. Estrutura em funil, do geral ao específico.

**Parágrafo 1 — O problema no mundo.** Comece pelo fato, não pelo método. Uma frase de abertura com número e fonte oficial. Exemplo:

> *No Brasil, a Lei 14.026/2020 fixou metas de universalização de 99% de cobertura de água e 90% de coleta e tratamento de esgoto até 2033; para o ano de 2024, apenas 45,9% dos municípios brasileiros enviaram ao SINISA os dados necessários para calcular os cinco indicadores básicos de saneamento (ABES, 2026).*

Siga com duas ou três frases sobre as consequências (saúde, desigualdade regional, custo fiscal) e sobre a situação do Nordeste. Fonte em cada número.

**Parágrafo 2 — Como o problema é medido hoje e por que isso é insuficiente.** Apresente o índice ou a prática corrente (no seu caso, o Ranking ABES da Universalização do Saneamento, que soma cinco indicadores com pesos iguais e classifica os municípios em quatro categorias) e sua limitação estrutural. No caso do ABES, a limitação é que a regra de agregação (soma com pesos iguais, plenamente compensatória) é uma escolha entre várias possíveis, nunca testada contra um desfecho, além da exclusão dos municípios não habilitados; a cobertura parcial dos 100 maiores municípios é limitação de outro índice, o do Trata Brasil. Não critique o índice; mostre que outra regra, igualmente defensável, priorizaria outros municípios, e que não se sabe qual delas é mais coerente com a saúde da população.

**Parágrafo 3 — O que a literatura já fez e o que falta.** Dois ou três estudos que aplicaram MCDM ao mesmo domínio, uma frase para cada, e a lacuna que eles deixam. A lacuna precisa ser verificável. A principal aqui: estudos que comparam métodos multicritério costumam medir só a concordância entre os rankings, sem perguntar qual deles reflete melhor um desfecho externo. Lacunas secundárias: base nova ainda não explorada, ausência de análise de robustez, ausência de comparação com o índice oficial. Cite as revisões (Behzadian et al., 2010; Yu et al., 2023; Tarnanidis et al., 2026) só aqui, uma vez.

**Parágrafo 4 — O que este artigo faz.** Uma frase de propósito e, em seguida, três bullets de contribuição. Os bullets são o que o editor lê para decidir se envia a revisores. Modelo:

- Comparação controlada de quatro métodos de agregação (soma ponderada, TOPSIS, VIKOR e PROMETHEE II) e quatro esquemas de pesos (três neutros ou objetivos e um subjetivo, o AHP clássico) sobre a mesma base, o mesmo ano e os mesmos cinco indicadores do Ranking ABES 2026, nos 505 municípios nordestinos com dados completos, os mesmos do ranking oficial. O desenho separa o efeito da regra de agregação do efeito dos pesos, e o efeito de pesos objetivos do de pesos subjetivos.
- Teste de validade externa dos 16 rankings contra a taxa de internações por DRSAI, com o método e os parâmetros fixados antes do teste, o que mostra qual regra de agregação produz a ordenação mais coerente com a saúde da população.
- Explicação das diferenças pelo grau de compensação de cada método: quais municípios mudam de posição, por que mudam (em geral, desempenho muito desigual entre componentes) e o que isso implica para a priorização em um ranking público.

**Parágrafo 5 — Organização do artigo.** Uma frase por seção. Alguns periódicos dispensam este parágrafo; verifique o guia de autores.

**O que não fazer:**

- Não abra com a definição de MCDM ou com a história do PROMETHEE. Isso pertence à revisão.
- Não use "inovador" ou "pioneiro" sobre o próprio trabalho. Mostre a lacuna e deixe o leitor concluir.
- Não prometa o que os resultados não entregam. Escreva a introdução por último.
- Não cite mais de 12 a 15 referências na introdução. O excesso sinaliza que a revisão foi mal separada.

## Seção 2 — Pergunta de pesquisa e escopo do projeto

A pergunta de pesquisa é uma frase interrogativa que o artigo responde com um sim, um não, um ranking ou um número. Se a resposta couber em uma frase da conclusão, a pergunta está bem formulada.

**Fórmula da pergunta principal (PP):** *Em que medida a escolha de [método] altera a ordenação de [alternativas] em [dimensão], e qual dessas ordenações se associa mais fortemente a [desfecho externo]?*

Exemplo (Ideia 1):

> **PP:** Em que medida a escolha do método de agregação multicritério (soma ponderada, como no Ranking ABES 2026, AHP clássico, AHP Gaussiano, TOPSIS, VIKOR e PROMETHEE II) altera a ordenação dos municípios nordestinos quanto ao saneamento, e qual dessas ordenações se associa mais fortemente à taxa de internações por DRSAI, considerando diferenças entre estados e portes?

**Perguntas secundárias (até quatro):** cada uma corresponde a uma subseção dos Resultados.

- **PS1 (divergência):** Quanto as ordenações diferem entre si (Kendall τ, mudanças de quartil) e quais municípios mudam mais de posição?
- **PS2 (compensação):** O grau de compensação do método explica as divergências e as diferenças de associação com a DRSAI? Os municípios com desempenho desigual entre componentes, como zero em tratamento de esgoto, são os que mais mudam?
- **PS3 (robustez):** As conclusões se mantêm sob os quatro esquemas de pesos, sob a variação de pesos do SMAA, sob a variação dos limiares q e p e sob pequenas variações dos julgamentos da matriz de Saaty?
- **PS4 (perfil):** Qual perfil de desempenho caracteriza os municípios que mudam de quartil, em especial entre os habilitados no ABES, e o que isso sugere para a priorização de investimentos?

Na redação, use sempre linguagem de associação (*"se associa mais fortemente"*, *"é mais coerente com"*), nunca *"o melhor método"* em sentido geral nem *"reduz internações"*.

**Escopo** é o que delimita a resposta. Escreva-o em quatro frases, uma por dimensão:

| Dimensão | Como redigir | Exemplo (Ideia 1) |
| --- | --- | --- |
| Espacial | Nomeie a unidade e o universo | Os 1.794 municípios do Nordeste; amostra = os 505 completos, que coincidem com os habilitados no ABES; subamostra de validade = os 360 com taxa de DRSAI válida |
| Temporal | Ano-base e, se houver, série | Ano-base 2024 (SINISA 2025); SINISA 2024 (ano-base 2023) citado apenas na discussão de tendência |
| Temática | Quais dimensões do problema entram | Os cinco indicadores do ABES, que cobrem três dos quatro componentes do saneamento: abastecimento de água, esgotamento sanitário (coleta e tratamento) e resíduos sólidos (coleta e disposição final); drenagem fora; DRSAI só como validade externa, nunca como critério |
| Metodológica | Família de métodos e o que não se compara | Soma ponderada, TOPSIS, VIKOR e PROMETHEE II × pesos iguais, CRITIC, AHP Gaussiano e AHP clássico (Saaty); GAIA e SMAA sobre o PROMETHEE II com CRITIC; associação com a DRSAI ajustada só por UF e porte (sem modelo causal) |

**O que fica fora, dito explicitamente.** Uma frase para cada exclusão relevante e o motivo: *"Drenagem urbana não foi incluída porque o módulo correspondente do SINISA 2025 cobriu apenas [x]% dos municípios nordestinos."* (O módulo de drenagem não está em `dados/`; baixe-o se for usar esse número.) Outra exclusão a declarar: *"A associação com a DRSAI não foi ajustada por renda, cobertura da atenção primária nem acesso hospitalar, o que exigiria bases adicionais; o estudo controla apenas por unidade da federação e porte."* Exclusões não justificadas viram perguntas de revisor.

**Erro comum:** confundir objetivo com pergunta. *"Avaliar o desempenho dos municípios"* é um objetivo e não pode ser respondido. *"Quais municípios estão mais distantes da meta de 2033 quando..."* é uma pergunta.

## Seção 3 — Revisão de literatura

A revisão não é um inventário; é um argumento em três blocos que termina na lacuna que o artigo preenche. Cada bloco tem de 200 a 300 palavras e fecha com uma frase que aponta para o próximo.

**Bloco 3.1 — O problema no domínio de aplicação.** Como o desempenho em [saneamento] é medido e avaliado na literatura e nos instrumentos oficiais. Cubra: (a) os índices oficiais e sua construção (Ranking ABES da Universalização: cinco indicadores SINISA somados com pesos iguais, quatro categorias fixas, das quais três aparecem no Nordeste; Ranking do Trata Brasil, restrito aos 100 municípios mais populosos, só [n] deles nordestinos); (b) estudos acadêmicos que avaliaram o mesmo objeto com qualquer método (DEA, regressão, índices compostos); (c) o que esses estudos concordam que importa (os critérios que você vai usar nascem aqui). Inclua um parágrafo sobre saneamento e saúde: a classificação das DRSAI (doenças de transmissão feco-oral, por inseto vetor, por contato com a água, relacionadas à higiene e geo-helmintos) e os estudos brasileiros que associam cobertura de saneamento a internações. Fecho: *"Esses trabalhos convergem sobre quais dimensões importam, mas as agregam por uma regra escolhida a priori, sem testar se outra regra produziria uma ordenação mais coerente com a saúde."*

**Bloco 3.2 — Métodos multicritério, compensação e comparação entre métodos.** Apresente os métodos em um parágrafo, organizados pelo grau de compensação: soma ponderada, AHP clássico (Saaty, 1980), AHP Gaussiano (Santos et al., 2021) e TOPSIS (compensação total; Hwang & Yoon, 1981), VIKOR (parcial; Opricovic & Tzeng, 2004) e PROMETHEE II (limitada; Brans & Vincke, 1985; Brans & Mareschal, 2005). Em outro parágrafo, os estudos que compararam métodos sobre os mesmos dados e o que mediram (quase sempre só a concordância entre rankings). Depois, as variantes que você usa (SMAA-PROMETHEE, Corrente et al., 2014; GAIA) e os estudos que aplicaram MCDA ao domínio, no Brasil e fora. Para cada estudo citado, uma frase com: objeto, alternativas, número de critérios, forma de definir pesos, se fez análise de sensibilidade. Esses cinco atributos alimentam a tabela-síntese.

**Bloco 3.3 — Lacunas e posicionamento.** Nomeie as lacunas com base nas revisões (Behzadian et al., 2010; Yu et al., 2023; Tarnanidis et al., 2026) e no que a tabela-síntese mostra. A central: a escolha do método raramente é julgada por um desfecho externo. Fecho obrigatório: um parágrafo que diz exatamente o que este artigo faz que os anteriores não fizeram, em diálogo direto com a tabela.

**Tabela-síntese (obrigatória).** É a figura mais lida da revisão e a prova da lacuna. Uma linha por estudo, 8 a 15 estudos, o seu artigo na última linha.

| Estudo | Objeto/alternativas | Método | Critérios (n) | Pesos | Análise de sensibilidade | Comparação com índice oficial | Validação com desfecho externo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Autor (ano) | 92 municípios do RJ | PROMETHEE II | 7 | Especialistas | Não | Não | Não |
| ABES (2026) | 2.558 municípios habilitados | Soma de indicadores | 5 | Iguais | Não | — | Não |
| Autor (ano) | 27 UFs | DEA | 5 | — | Parcial | Não | Não |
| **Este artigo** | 505 municípios do Nordeste | Soma ponderada, AHP clássico, AHP Gaussiano, TOPSIS, VIKOR, PROMETHEE II (+ GAIA, SMAA) | 5 | Iguais, CRITIC, AHP Gaussiano, Saaty (+ SMAA) | Sim (SMAA, p/q, reversão) | Sim (Ranking ABES 2026) | Sim (internações por DRSAI) |

**Estratégia de busca (um parágrafo ou uma nota de rodapé).** Bases (Scopus, Web of Science, SciELO, Google Scholar para literatura cinzenta brasileira), string de busca (ex.: `PROMETHEE AND (sanitation OR "water supply" OR sewage) AND (municipal* OR Brazil*)`), período (2010–2026), critérios de inclusão e exclusão, número final de estudos. Isso não é uma revisão sistemática completa, mas mostra ao revisor que a amostra de estudos não foi escolhida por conveniência.

**Erros comuns:**

- Listar métodos MCDA (ELECTRE, MOORA...) sem relação com o problema. Cite só os métodos do desenho (incluindo os dois AHP) e os que servem de contraste para eles.
- Resumir cada estudo em um parágrafo. Uma frase por estudo; o detalhe vai para a tabela.
- Fechar a revisão sem a frase de lacuna. O revisor precisa ler, em uma frase, por que o artigo existe.
- Citar só artigos brasileiros ou só internacionais. Periódicos internacionais esperam que o caso brasileiro dialogue com a literatura global de economias emergentes.

## Seção 4 — Metodologia

A metodologia precisa permitir que outro pesquisador reproduza o ranking a partir dos mesmos dados. Organize-a em oito subseções, na ordem do fluxo de trabalho, e abra com um parágrafo que resume as etapas.

1. Fonte e preparação dos dados
2. Alternativas
3. Critérios
4. Parâmetros dos métodos (funções de preferência e limiares do PROMETHEE; v do VIKOR)
5. Pesos
6. Métodos de agregação (soma ponderada, AHP clássico, AHP Gaussiano, TOPSIS, VIKOR, PROMETHEE II; GAIA e SMAA no ranking de referência)
7. Validade externa com a DRSAI
8. Robustez e comparação com o benchmark

### 4.1 Dados

Para cada base, informe em uma tabela: órgão, nome do sistema, ano-base, data de extração, URL, variáveis extraídas, cobertura (quantos municípios reportaram) e tratamento de ausentes. Exemplo:

| Base | Órgão | Ano-base | Extração | Variáveis | Cobertura no Nordeste | Ausentes |
| --- | --- | --- | --- | --- | --- | --- |
| SINISA 2025 — Água | Ministério das Cidades | 2024 | [data] | IAG0001 (planilha retificada) | [n de 1.794] | Regra definida em "Antes de escrever" |
| SINISA 2025 — Esgoto | Ministério das Cidades | 2024 | [data] | IES0001, IES2003 | [n de 1.794] | Idem; IES2003 acima de 100% limitado a 100, como no ABES |
| SINISA 2025 — Resíduos | Ministério das Cidades | 2024 | [data] | IRS0001, IRS3002 (invertido: 100 − disposição inadequada) | [n de 1.794] | Idem |
| Ranking ABES 2026 | ABES | 2024 | [data] | Nota 0–500, categoria, taxa de DRSAI, UF, porte | Nota: 505 habilitados; DRSAI: todos os 1.794 | Comparação com a nota restrita aos habilitados; DRSAI 0,00 tratada como ausente (360 válidas entre os 505) |

**Tratamento de ausentes é decisão metodológica, não nota de rodapé.** Diga o que fez e por quê: só entram os municípios que autodeclararam os quatro indicadores contabilizados, e o IRS3002 ausente é lido como disposição inadequada.

### 4.2 Alternativas

Uma frase com o universo e o critério de inclusão, seguindo a regra de dados ausentes definida em "Antes de escrever". Liste os excluídos em apêndice. Exemplo: *"Dos 1.794 municípios nordestinos, 505 dispunham dos cinco indicadores no SINISA 2025 e coincidem com os habilitados no Ranking ABES 2026; eles compõem a amostra, e os 360 com taxa de DRSAI válida formam a subamostra de validade externa. A ausência do IRS3002 seria lida como disposição final inadequada."*

### 4.3 Critérios

A tabela de critérios é a peça central da metodologia. Os critérios são exatamente os cinco indicadores do Ranking ABES, com as mesmas regras de tratamento (limite de 100% no IES2003 e inversão do indicador de disposição inadequada). Justifique a escolha em duas frases: são os indicadores que representam os componentes do saneamento ligados às metas da Lei 14.026/2020, e usá-los torna a comparação com o ABES controlada.

| Código | Critério | Indicador SINISA | Unidade | Direção | Justificativa |
| --- | --- | --- | --- | --- | --- |
| C1 | Atendimento da população total com rede de abastecimento de água | IAG0001 | % | max | Meta 99% (Lei 14.026/2020) |
| C2 | Atendimento da população total com rede coletora de esgoto | IES0001 | % | max | Meta 90% (Lei 14.026/2020) |
| C3 | Esgoto tratado referido à água consumida | IES2003 (limitado a 100) | % | max | Meta 90% (Lei 14.026/2020) |
| C4 | Cobertura da população total com coleta de resíduos sólidos domiciliares | IRS0001 | % | max | Componente de resíduos da Lei 11.445/2007 |
| C5 | Disposição final adequada de resíduos sólidos urbanos | IRS3002 adaptado (100 − inadequada) | % | max | Fim dos lixões (Lei 14.026/2020) |

**Atenção ao C5.** No ABES, esse indicador é quase binário: muitos municípios aparecem com 0 ou 100. O CRITIC tende a dar peso alto a critérios com essa dispersão, e o C5 pode dominar o ranking. Reporte os pesos, mostre o efeito no GAIA e compare com o cenário de pesos iguais. Para o C5, a função linear não serve: a regra dos quartis da subseção 4.4, aplicada ao IRS3002 dos 505 habilitados no ABES, dá q = 0 e p = 100 (só 23 valores distintos; 248 zeros e 236 valores 100), e a função linear vira, na prática, uma V-shape. Adotou-se a função em U com q = p = 5 (decisão registrada no `log_decisoes.md`): diferenças de até 5 pontos são empate, e acima disso a preferência é total. Ela foi preferida à função nível e à usual porque os poucos municípios com valores entre 95 e 99 empatam com os que têm 100, em vez de perderem para eles por inteiro.

Regras: entre 5 e 10 critérios; verifique a correlação entre eles (matriz de Spearman em apêndice; pares com |ρ| > 0,8 exigem justificativa ou exclusão); mantenha critérios de resultado (saúde) separados dos de insumo (investimento) e diga isso no texto.

### 4.4 Parâmetros dos métodos

A soma ponderada, os dois AHP e o TOPSIS não têm parâmetros além dos pesos e da normalização (informe qual: notas brutas no ABES, pela soma nos AHP, min-max na soma ponderada com CRITIC, vetorial no TOPSIS). O VIKOR tem o parâmetro v, peso da estratégia de "maioria" contra a de "arrependimento individual"; use o valor usual v = 0,5 e teste 0,25 e 0,75 na robustez. O PROMETHEE é o que mais exige: esta é a subseção que os revisores mais cobram e que a maioria dos artigos omite. Para cada critério, informe a função (usual, U-shape, V-shape, nível, linear, gaussiana) e os limiares q (indiferença) e p (preferência). Nunca use a função "usual" para todos os critérios sem justificar.

Regra de derivação empírica, reproduzível e defensável: para o critério j, calcule as diferenças absolutas entre todos os pares de alternativas; q = 1º quartil dessas diferenças e p = 3º quartil. Reporte os valores na tabela de critérios (acrescente duas colunas). Exceção: no C5, a função em U com q = p = 5, justificada na subseção 4.3. Em Resultados, teste q e p nos limites ±50% e mostre o efeito.

A fórmula da função linear (tipo V com indiferença) fica em destaque uma única vez:

```math
P_j(d) = \begin{cases} 0 & d \le q_j \\ \dfrac{d - q_j}{p_j - q_j} & q_j < d \le p_j \\ 1 & d > p_j \end{cases}
```

### 4.5 Pesos

Os quatro esquemas de pesos são cruzados com os quatro métodos, e nenhum deles é "o principal" para a pergunta de pesquisa. Os pesos de Saaty do AHP clássico são o único esquema subjetivo; cruzá-los com todos os métodos permite ver se o efeito da agregação se repete quando os pesos expressam prioridade, e não dispersão. O CRITIC define o ranking de referência usado nas leituras detalhadas (GAIA, PROMETHEE I, SMAA). Justifique cada esquema em uma frase: pesos iguais reproduzem a escolha do ABES; o CRITIC combina dispersão e conflito entre critérios, de modo que indicadores redundantes (coleta e tratamento de esgoto, por exemplo) não contam em dobro; o AHP Gaussiano pondera só pela dispersão e dialoga com a literatura brasileira; o AHP clássico expressa uma prioridade declarada entre os componentes do saneamento. O AHP Gaussiano é, na essência, um método de pesos seguido de soma ponderada; por isso ele entra como coluna de pesos, e não como método de agregação, e a célula "soma ponderada com AHP Gaussiano" é o AHP Gaussiano como aparece na literatura, com os valores normalizados pela soma. O AHP clássico tem a mesma estrutura (pesos seguidos de soma ponderada normalizada), e a célula "soma ponderada com AHP clássico" é o AHP clássico da literatura; os pesos vêm da comparação par a par dos critérios na escala de Saaty, com a razão de consistência (RC) abaixo de 0,10.

| Esquema | Natureza | Como calcular | Papel no artigo |
| --- | --- | --- | --- |
| Pesos iguais | Neutro | 1/n por critério | Desenho cruzado; com a soma ponderada sobre as notas brutas, reproduz o ABES e isola o efeito da agregação |
| CRITIC | Objetivo (dispersão + conflito) | Desvio-padrão dos dados normalizados por min-max × Σ(1 − correlação com os demais), normalizado; a soma ponderada também usa min-max | Desenho cruzado; ranking de referência (com PROMETHEE II) |
| AHP Gaussiano | Objetivo (dispersão) | Fator gaussiano = desvio-padrão ÷ média de cada critério normalizado, normalizado para somar 1 | Desenho cruzado; diálogo com a literatura brasileira |
| AHP clássico | Subjetivo (julgamento do decisor) | Matriz de comparação par a par na escala de Saaty (1 a 9); pesos pela média geométrica das linhas, normalizada; RC < 0,10 | Desenho cruzado; contraste entre pesos subjetivos e objetivos |
| SMAA | Estocástico | 10.000 vetores de pesos sorteados (uniformes no simplex, ou em torno dos pesos CRITIC) | Robustez: índices de aceitabilidade de posição |

Os pesos já calculados nas planilhas ficam assim. ABES, AHP clássico e AHP Gaussiano estão na escala normalizada pela soma (os do ABES são os equivalentes aos 20% nominais sobre as notas brutas). O CRITIC está na escala min-max, em que é aplicado; a última coluna converte esses pesos para a escala pela soma, para comparação direta com as demais:

| Critério | ABES (equivalente) | AHP clássico | AHP Gaussiano | CRITIC (min-max) | CRITIC (equivalente pela soma) |
| --- | --- | --- | --- | --- | --- |
| C1 Água (IAG0001) | 26,7% | 41,7% | 8,5% | 13,4% | 17,7% |
| C2 Esgoto (IES0001) | 13,7% | 16,0% | 20,4% | 15,5% | 10,6% |
| C3 Tratamento (IES2003) | 9,5% | 9,7% | 34,9% | 19,6% | 9,2% |
| C4 Coleta (IRS0001) | 31,3% | 26,3% | 6,8% | 14,9% | 28,5% |
| C5 Destinação (IRS3002) | 18,7% | 6,2% | 29,5% | 36,6% | 34,0% |

No CRITIC, Destinação recebe o maior peso (36,6%), como previsto para o C5 quase binário (seção 4.3).

O AHP clássico concentra 68% do peso em Água e Coleta; o Gaussiano põe 64% em Tratamento e Destinação. Essa oposição é um resultado em si e entra na subseção 5.1.

Diga explicitamente que os pesos do AHP clássico são os únicos definidos pelos autores, informe a matriz de Saaty e a RC em apêndice e que nenhum outro peso foi escolhido por julgamento. Essa frase desarma a objeção mais comum.

### 4.6 Métodos de agregação

Abra com uma tabela dos métodos, ordenados pelo grau de compensação, e um parágrafo curto para cada um. Em Python, todos estão no `pymcdm` ou no `pyDecision`, ou são curtos de implementar.

| Método | Compensação | Ideia em uma frase | Referência |
| --- | --- | --- | --- |
| Soma ponderada | Total | Soma dos critérios multiplicados pelos pesos; com pesos iguais sobre as notas brutas, é a regra do ABES | Fishburn (1967) ou manual de MCDA |
| AHP clássico | Total | Pesos da comparação par a par na escala de Saaty, aplicados aos valores normalizados pela soma | Saaty (1980) |
| AHP Gaussiano | Total | Pesos pelo coeficiente de variação de cada critério, aplicados aos valores normalizados pela soma | Santos et al. (2021) |
| TOPSIS | Total | Proximidade relativa à solução ideal e distância da anti-ideal | Hwang & Yoon (1981) |
| VIKOR | Parcial | Compromisso entre o desempenho médio (S) e o pior desvio individual (R), ponderado por v | Opricovic & Tzeng (2004) |
| PROMETHEE II | Limitada | Comparação par a par com funções de preferência e limiares; uma vantagem grande num critério não cresce sem limite | Brans & Vincke (1985) |

Para o PROMETHEE, que também gera as leituras detalhadas, um parágrafo por etapa: grau de preferência agregado π(a,b), fluxos positivo φ⁺, negativo φ⁻ e líquido φ; PROMETHEE I (pré-ordem parcial; aqui só como diagnóstico, reportando o número de pares incomparáveis e 3 ou 4 casos emblemáticos, pois o diagrama com mais de uma centena de alternativas é ilegível) e PROMETHEE II (pré-ordem total); GAIA (projeção PCA da matriz de fluxos unicritério, com o percentual de variância explicada); SMAA-PROMETHEE (para cada vetor de pesos sorteado, calcule o ranking; o índice de aceitabilidade $b_i^r$ é a fração de sorteios em que a alternativa i fica na posição r). Cite Brans & Mareschal (2005) para o núcleo e Corrente et al. (2014) para o SMAA. Fórmulas só para φ e para $b_i^r$; o resto é referência.

```math
\phi(a) = \phi^{+}(a) - \phi^{-}(a) = \frac{1}{n-1}\sum_{b \ne a}\left[\pi(a,b) - \pi(b,a)\right]
```

### 4.7 Validade externa com a DRSAI

Esta subseção sustenta a pergunta principal. Escreva-a como um protocolo fixado antes de olhar os resultados:

1. **Amostra comum.** Todos os 16 rankings são comparados nos mesmos 360 municípios (amostra com taxa de DRSAI válida). Taxa 0,00 é tratada como ausente.
2. **Associação.** Spearman ρ entre a posição em cada ranking e a taxa de DRSAI. Espera-se ρ negativo entre a pontuação e a taxa: melhor saneamento, menos internações.
3. **Diferença entre métodos.** Os rankings serão muito correlacionados entre si, então as correlações com a DRSAI devem sair próximas. O que importa é a diferença: Δρ entre pares de rankings, com intervalo de confiança por bootstrap (reamostrando municípios, 5.000 vezes, semente fixa) ou o teste de Williams/Steiger para correlações dependentes. Se nenhum intervalo excluir zero, a conclusão é que a escolha do método importa pouco para a associação com a saúde, o que também é um resultado publicável.
4. **Controle mínimo, sem bases novas.** Correlação parcial de Spearman controlando por UF e porte (as duas variáveis vêm do arquivo do ABES). Spearman dentro dos estados com amostra suficiente (BA 121, CE 84, PE 62, RN 35 e PB 27 municípios válidos) e dentro de cada porte (grande porte 57; pequeno e médio porte 303). Os demais estados (AL 12, MA 9, SE 8, PI 2) só entram na análise conjunta. O que interessa é se o método que se sai melhor no geral continua melhor dentro dos grupos.
5. **Valores extremos.** O Spearman já é pouco sensível a eles; reporte também uma versão sem os 5% de taxas mais altas.
6. **Número de rankings.** Não passe de 16: quanto mais rankings comparados à DRSAI, maior a chance de um deles "ganhar" por acaso. Reporte todos, não só o vencedor.

### 4.8 Robustez e benchmark

Liste os testes que serão reportados em Resultados, cada um com sua métrica. Robustez responde se o ranking se mantém; não confunda com a validade externa da subseção anterior.

- Intervalos de estabilidade dos pesos (Visual PROMETHEE ou cálculo próprio): faixa em que cada peso pode variar sem alterar as k primeiras posições.
- Sensibilidade aos julgamentos de Saaty: alterar cada julgamento da matriz em um ponto da escala, mantendo RC < 0,10, e medir o Kendall τ com o ranking original nos quatro métodos.
- SMAA: índices de aceitabilidade no ranking de referência e, se houver tempo, frequência com que cada método vence na associação com a DRSAI sob os pesos sorteados.
- Sensibilidade a q e p (±50%), ao limiar de Destinação (função usual e em U com q = p = 10), a v (0,25 e 0,75) e à normalização do TOPSIS (min-max): Kendall τ entre rankings e efeito sobre o ρ com a DRSAI. Os valores exatos de cada variação estão no `log_decisoes.md`, seção 8.
- Reversão de ordem: retirar a melhor, a pior e uma alternativa aleatória; contar quantos pares trocam de ordem.
- Comparação com o Ranking ABES 2026: a soma ponderada com pesos iguais reproduz a nota do ABES, então ela é o ponto de partida; para cada um dos outros 15 rankings, Spearman ρ com a nota ABES nos 505 habilitados e mudanças de quartil.

**Software.** Nomeie biblioteca e versão exatas, tiradas do `requirements.txt` (por exemplo, pyDecision ou pymcdm para PROMETHEE e pesos); código próprio para SMAA (semente fixa); GAIA e intervalos de estabilidade também em Python, para que os scripts gerem todas as figuras. O Visual PROMETHEE (só Windows, não scriptável) serve apenas para conferir os resultados. Link para o repositório. Sem isso, revisores de MCDA costumam pedir os dados e o código.

## Seção 5 — Resultados e discussão

Os resultados respondem às perguntas de pesquisa na ordem em que foram feitas: PP, PS1, PS2, PS3, PS4. A PP depende das divergências da PS1 para fazer sentido, então a subseção 5.1 pode apresentar as duas juntas: primeiro quanto os rankings diferem, depois qual se associa mais à DRSAI. Cada subseção abre com a resposta em uma frase e só depois mostra a evidência. Separe o que o dado mostra (resultado) do que isso significa (discussão); muitos periódicos aceitam as duas coisas na mesma seção, mas o revisor precisa distinguir uma da outra.

**Sequência recomendada de exibições** (quatro a cinco exibições no corpo; o excedente vai para material suplementar):

| # | Exibição | Responde a | O que mostrar |
| --- | --- | --- | --- |
| T1 | Estatística descritiva da matriz de decisão e pesos por esquema | contexto | média, mediana, mín., máx. por critério; n válido; uma coluna de pesos por esquema (iguais em escala normalizada, CRITIC, AHP Gaussiano, AHP clássico) |
| F1 | Validade externa (exibição principal) | PP | os 16 ρ com a DRSAI e seus intervalos bootstrap, em gráfico de pontos agrupado por método e colorido por esquema de pesos; métodos ordenados pelo grau de compensação |
| T2 | Diferenças entre métodos e controle mínimo | PP | Δρ com intervalo de confiança para os pares principais; ρ parcial por UF e porte; ρ dentro de BA, CE, PE, RN, PB e dentro de cada porte |
| F2 | Divergência entre os 16 rankings | PS1 | mapa de calor de Kendall τ entre os rankings; número de municípios que mudam de quartil em relação à soma ponderada com pesos iguais (o ABES) |
| F3/T3 | Compensação e perfil dos que mudam | PS2, PS4 | mudança de posição × desigualdade entre os critérios do município (por exemplo, desvio-padrão dos cinco indicadores); tabela dos municípios que mais mudam, com o critério que explica a mudança |
| T4 | Robustez | PS3 | aceitabilidade SMAA no ranking de referência, Kendall τ por variação de q/p e v, reversões de ordem |
| S | Suplemento | — | plano GAIA (com δ), PROMETHEE I (pares incomparáveis e casos emblemáticos), top 20 e bottom 20 de cada ranking, mapa de calor SMAA |

**Como escrever cada subseção:**

*5.1 Divergência entre os rankings (PS1).* Abra com o número que resume a divergência: o Kendall τ médio entre os 16 rankings e quantos municípios mudam de quartil em relação à soma ponderada com pesos iguais, que reproduz o ABES. Separe o efeito do método (linhas da tabela métodos × pesos) do efeito dos pesos (colunas). Os dois AHP ilustram bem o efeito dos pesos: no parecer técnico, ambos têm ρ de 0,87 a 0,89 com o ABES, mas só 0,76 entre si, porque cada um se afasta do ABES numa direção. Não narre a matriz de τ; diga qual fator move mais o ranking.

*5.2 Validade externa com a DRSAI (PP).* É a subseção central. Abra com a resposta em uma frase: *"A ordenação do [método X com pesos Y] é a que mais se associa à taxa de internações por DRSAI (ρ = [valor]; IC 95% [a; b])"*. Em seguida, mostre se essa vantagem é distinguível dos demais (Δρ com intervalo bootstrap) e se se mantém dentro dos estados e dos portes. Se nenhum intervalo de Δρ excluir zero, diga isso com a mesma clareza: a escolha do método altera quem é priorizado, mas não muda a coerência do ranking com a saúde. Linguagem de associação sempre; internações dependem de muitos fatores além do saneamento.

*5.3 Compensação como explicação (PS2).* Ordene os métodos pelo grau de compensação e veja se o ρ com a DRSAI cresce nessa direção. Mostre que os municípios que mais mudam de posição entre métodos são os de desempenho desigual entre componentes (um zero em disposição de resíduos ou em tratamento de esgoto compensado por bons índices nos demais). Se os métodos de compensação limitada se associarem melhor à DRSAI, a hipótese do componente mais fraco ganha apoio; se não, discuta por quê.

*5.4 Robustez (PS3).* Reporte: (a) se o método que se sai melhor na 5.2 continua melhor sob os quatro esquemas de pesos e sob a variação de q, p e v, e quanto os rankings com pesos de Saaty mudam com pequenas variações na matriz; (b) quantas alternativas têm a mesma posição em mais de 90% dos sorteios SMAA no ranking de referência; (c) o Kendall τ entre os rankings com q/p ±50% (acima de 0,9 é estável); (d) o número de pares que trocam de ordem ao retirar alternativas. Conclua com uma frase de julgamento: *"O ranking é robusto nas posições extremas e instável no terço central, onde pequenas variações de peso trocam posições vizinhas."*

*5.5 Perfil dos que mudam e comparação com o ABES (PS4).* Entre os 505 habilitados, compare o ranking que mais se associa à DRSAI com a nota ABES: Spearman ρ, mudanças de quartil (a matriz de transição das três categorias do ABES no Nordeste é pouco informativa, porque uma delas tem só 7 municípios) e uma linha por município que muda de quartil explicando o porquê. Esta é a parte que interessa ao gestor e ao editor de política pública.

*5.6 Discussão.* Três a cinco parágrafos: (1) o que os resultados dizem sobre a escolha do método num ranking público (a regra de agregação muda quem é priorizado, e a DRSAI indica qual regra é mais coerente com a saúde); (2) o que confirmam e o que contradizem na literatura dos blocos 3.1 e 3.2; (3) o papel da compensação na explicação; (4) implicações para a política pública, com cautela (*"sugerem priorizar"*, não *"demonstram que se deve"*); (5) uma ponte para as limitações, em especial a ausência de ajuste por renda e acesso à saúde.

**Erros comuns:**

- Tabela com todas as posições no corpo do texto. Vai para apêndice ou suplemento.
- Figura GAIA sem o δ (variância explicada). Abaixo de 60%, o plano é pouco confiável e isso precisa ser dito.
- Reportar robustez em uma frase ("o ranking mostrou-se estável") sem métrica.
- Concluir causalidade. O ranking descreve, e a associação com a DRSAI não prova que um método "reduz" internações nem que é o melhor em sentido geral.
- Escolher método, pesos ou limiares pelo que dá a maior correlação com a DRSAI. Isso torna o teste circular e convida a pergunta "por que não uma regressão?".
- Reportar só o ρ de cada ranking sem testar as diferenças entre eles.
- Discutir só os municípios do topo. As mudanças de posição no meio e na base são o achado.

## Seção 6 — Limitações e trabalhos futuros

Limitações bem escritas aumentam a credibilidade; mal escritas parecem desculpa. A regra: cada limitação vem com (a) o que ela afeta, (b) o que foi feito para mitigá-la e (c) o trabalho futuro que a resolve. Três a cinco limitações bastam; mais do que isso sugere que o estudo não deveria ter sido feito.

**Tipologia das limitações** (escolha as que se aplicam e redija uma por parágrafo curto):

| Tipo | Exemplo (Ideia 1) | Mitigação já feita | Trabalho futuro |
| --- | --- | --- | --- |
| Dados: cobertura | 1.289 dos 1.794 municípios não habilitados no ABES, com cobertura de 3% no Piauí a 52% no Ceará; [n] sem os cinco indicadores no SINISA 2025 | Amostra só com completos; perfil (UF e porte) dos excluídos reportado em apêndice | Repetir com as próximas edições do SINISA |
| Dados: autodeclaração | Indicadores informados pelos prestadores, sem auditoria; parte dos zeros em IES2003 e IRS3002 pode ser ausência de informação, e não de serviço, o que pesa mais no AHP Gaussiano (64% do peso nesses dois) | Validade externa com DRSAI | Incorporar o módulo de regulação do SINISA quando publicado |
| Validade: fatores de confusão | Renda, urbanização, cobertura da atenção primária e acesso hospitalar influenciam tanto o saneamento quanto as internações; parte da diferença entre métodos pode refletir esses fatores | Controle por UF e porte; linguagem de associação | Regressão binomial negativa com as contagens do SIH/SUS (população como offset) e covariáveis do IBGE, do e-Gestor AB e do CNES |
| Validade: DRSAI ruidosa | Taxas instáveis em municípios pequenos; 0,00 em parte dos municípios; internação depende de haver hospital acessível | Spearman; zeros como ausentes; versão sem valores extremos | Média de 2022–2024 da DRSAI e suavização bayesiana empírica |
| Dados: quebra de série | SNIS e SINISA têm definições distintas; a própria ABES pede cautela na comparação entre edições | Análise restrita a um ano-base | PROMETHEE temporal quando houver três ou mais edições do SINISA |
| Critérios: só acesso | Os cinco indicadores medem cobertura e destinação, não qualidade, perdas ou investimento | Escolha justificada pela comparação controlada com o ABES | Modelo ampliado com perdas, investimento e qualidade da água |
| Método: pesos objetivos | CRITIC e AHP Gaussiano refletem o que os dados discriminam, não a prioridade política; no Gaussiano, Coleta, quase universalizada, recebe só 6,8%, e os pesos mudam com a amostra | Desenho cruzado com pesos iguais; SMAA; contraste com o AHP clássico | PROMETHEE-GDSS com representantes das companhias estaduais de saneamento, das agências reguladoras e das prefeituras |
| Método: pesos subjetivos | Os pesos do AHP clássico dependem do julgamento de um único decisor; outro decisor chegaria a outros pesos | RC = 0,015; matriz publicada em apêndice; sensibilidade aos julgamentos; comparação com os três esquemas neutros ou objetivos no mesmo desenho | Matriz de Saaty preenchida por um painel de especialistas, com agregação dos julgamentos individuais |
| Método: limiares empíricos | q e p derivados dos quartis das diferenças; v = 0,5 por convenção | Sensibilidade ±50% em q e p; v em 0,25 e 0,75 | Elicitação de limiares com especialistas |
| Escopo: benchmark parcial | ABES só inclui municípios com todos os indicadores | Comparação restrita aos habilitados | Comparação com outros índices (IDSC-BR, ODS 6) |
| Escopo: inferência | Ranking é descritivo; a associação com a DRSAI não identifica causas | Linguagem de associação na discussão | Modelo explicativo (ML + SHAP) sobre a posição no ranking |

**Como redigir cada parágrafo.** Modelo: *"A principal limitação decorre da cobertura do SINISA 2025: dos 1.794 municípios nordestinos, [n] não dispunham dos cinco indicadores, e o Ranking ABES exclui 1.289. Este estudo usou os 505 municípios que autodeclararam todos os indicadores. A repetição do estudo com as edições seguintes do SINISA é o desdobramento natural."* Para a limitação central da validade, use: *"A associação entre as ordenações e a taxa de internações por DRSAI foi ajustada apenas por unidade da federação e porte. Renda, cobertura da atenção primária e acesso hospitalar influenciam tanto o desempenho em saneamento quanto as internações, e parte da diferença observada entre métodos pode refletir esses fatores. Os resultados devem ser lidos como associação, e não como efeito. Um modelo ajustado por essas covariáveis, com as contagens de internações do SIH/SUS, é o passo seguinte desta agenda."*

**Trabalhos futuros que valem a pena mencionar** (escolha dois ou três; os demais ficam implícitos na tabela):

- Ajuste da associação com a DRSAI por renda, cobertura da atenção primária e acesso hospitalar, com as contagens do SIH/SUS e regressão binomial negativa.
- Extensão temporal com Temporal PROMETHEE II assim que houver três ou mais edições do SINISA.
- Validação com decisores reais via PROMETHEE-GDSS, transformando o estudo de dados secundários em instrumento de gestão.
- Replicação para o Brasil inteiro, com análise de equidade regional.
- Camada explicativa com aprendizado de máquina e SHAP sobre o fluxo líquido, ligando posição no ranking a fatores contextuais (renda, porte, modelo de prestação).

**Erros comuns:**

- Listar limitações sem mitigação nem desdobramento. Vira uma lista de defeitos.
- Apresentar como limitação algo que era escolha de escopo. Escolha de escopo se justifica na Seção 2.
- Prometer trabalhos futuros genéricos ("aplicar outros métodos"). Cada trabalho futuro deve nascer de uma limitação nomeada.
- Omitir a limitação de dados autodeclarados. O revisor vai apontá-la.

## Seção 7 — Conclusão

A conclusão responde à pergunta de pesquisa em uma frase, com número, e não traz nada que não esteja nos Resultados. Escreva-a em dois parágrafos curtos.

**Parágrafo 1 — Resposta e contribuição.** Responda à PP literalmente, com os principais números (por exemplo, quantos municípios mudam de quartil entre os métodos e qual ranking tem o maior ρ com a DRSAI, com o intervalo de Δρ). Em seguida, uma frase para cada contribuição da Introdução, na mesma ordem dos três bullets.

**Parágrafo 2 — Implicação e próximo passo.** Uma frase sobre o que gestores e reguladores podem fazer com o ranking (com a cautela da Discussão) e uma frase com o trabalho futuro mais importante da Seção 6.

**O que não fazer:**

- Não repita o resumo nem a metodologia.
- Não introduza resultado, citação ou limitação nova.
- Não termine com frase genérica ("mais estudos são necessários"); termine com o próximo passo concreto.

## Referências

Um artigo de anais com 12 a 15 páginas comporta entre 25 e 40 referências, distribuídas em quatro grupos. Com a nova pergunta, o grupo A deixa de ser só PROMETHEE e passa a cobrir todos os métodos do desenho, incluindo os dois AHP. A lista abaixo é o núcleo; corte para caber no limite. Confira cada DOI antes de incluir.

**Grupo A — Métodos de agregação (obrigatório, 8 a 10 referências):**

- Brans, J.P.; Vincke, Ph. (1985). A preference ranking organisation method: The PROMETHEE method for MCDM. *Management Science*, 31(6), 647–656.
- Brans, J.P.; Mareschal, B. (2005). PROMETHEE methods. In: Figueira, J.; Greco, S.; Ehrgott, M. (eds.), *Multiple Criteria Decision Analysis: State of the Art Surveys*. Springer, cap. 5.
- Brans, J.P.; Vincke, Ph.; Mareschal, B. (1986). How to select and how to rank projects: The PROMETHEE method. *EJOR*, 24(2), 228–238.
- Mareschal, B.; Brans, J.P. (1988). Geometrical representations for MCDA (GAIA). *EJOR*, 34(1), 69–77.
- Behzadian, M.; Kazemzadeh, R.B.; Albadvi, A.; Aghdasi, M. (2010). PROMETHEE: A comprehensive literature review on methodologies and applications. *EJOR*, 200(1), 198–215. DOI 10.1016/j.ejor.2009.01.021.
- Corrente, S.; Figueira, J.R.; Greco, S. (2014). The SMAA-PROMETHEE method. *EJOR*, 239(2), 514–522.
- Yu, D.; Liu, Y.; Xu, Z. (2023). Analysis of knowledge evolution in PROMETHEE: A longitudinal and dynamic perspective. *Information Sciences*, 642, 119151.
- Hwang, C.L.; Yoon, K. (1981). *Multiple Attribute Decision Making: Methods and Applications*. Springer. (Origem do TOPSIS.)
- Opricovic, S.; Tzeng, G.H. (2004). Compromise solution by MCDM methods: A comparative analysis of VIKOR and TOPSIS. *EJOR*, 156(2), 445–455.
- Saaty, T.L. (1980). *The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation*. McGraw-Hill. (Origem do AHP clássico.)
- Saaty, T.L. (1977). A scaling method for priorities in hierarchical structures. *Journal of Mathematical Psychology*, 15(3), 234–281. (Escala de 1 a 9 e razão de consistência.)
- Fishburn, P.C. (1967). Additive utilities with incomplete product sets: application to priorities and assignments. *Operations Research*, 15(3), 537–542. (Referência usual da soma ponderada; confira.)

**Grupo B — Robustez, pesos e variantes recentes (6 a 10 referências):**

- Liu, Y.; Liu, J. (2024). Sensitivity analysis of the parameters for preference functions and rank reversal analysis in the PROMETHEE II method. *Omega*, 128, 103116.
- Diakoulaki, D.; Mavrotas, G.; Papayannakis, L. (1995). Determining objective weights in multiple criteria problems: The CRITIC method. *Computers & Operations Research*, 22(7), 763–770.
- Santos, M.; Costa, I.P.A.; Gomes, C.F.S. (2021). Multicriteria decision-making in the selection of warships: a new approach to the AHP method. *International Journal of the Analytic Hierarchy Process*, 13(1). (Origem do AHP Gaussiano; confira os dados da referência.)
- Lahdelma, R.; Salminen, P. (2001). SMAA-2: Stochastic multicriteria acceptability analysis for group decision making. *Operations Research*, 49(3), 444–454.
- Wątróbski, J.; Bączkiewicz, A.; Ziemba, E.; Sałabun, W. (2023). Temporal PROMETHEE II — New multi-criteria approach to sustainable management of alternative fuels consumption. *Journal of Cleaner Production*, 413, 137445.
- Costa, H.G.; Lima, G.B.A. (2026). Inequalities matter when prioritizing sustainable goals: a novel multi-criteria-clustering modeling (KRP2). *Annals of Operations Research*. DOI 10.1007/s10479-026-07125-w. (Referência ainda não conferida.)
- Tarnanidis, T.; Papathanasiou, J.; Mareschal, B. et al. (2026). Sustainable value creation in global marketing decisions: a systematic PRISMA review of PROMETHEE applications. *Journal of Marketing Analytics*. DOI 10.1057/s41270-026-00486-y. (Referência ainda não conferida.)
- Pereira, V.; Basilio, M.P.; Santos, C.H.T. (2024). pyDecision: a comprehensive library of MCDA methods in Python. arXiv:2404.06370.
- Steiger, J.H. (1980). Tests for comparing elements of a correlation matrix. *Psychological Bulletin*, 87(2), 245–251. (Teste da diferença entre correlações dependentes.)
- Efron, B.; Tibshirani, R.J. (1993). *An Introduction to the Bootstrap*. Chapman & Hall. (Intervalos bootstrap de Δρ.)

**Grupo C — Domínio de aplicação (10 a 15 referências).** Para a Ideia 1: estudos de desempenho em saneamento no Brasil (DEA, índices, regressão), metodologias do Ranking ABES e do Ranking do Trata Brasil, literatura internacional sobre benchmarking de utilities (Berg; Marques; Walter et al.), saúde e saneamento (DRSAI: a classificação da Funasa, de Costa et al., 2002, e estudos brasileiros que associam saneamento a internações), marco regulatório (Heller; Britto). Metade deve ser de 2020 em diante.

**Grupo D — Bases, normas e documentos oficiais (5 a 10 referências).** Cite como documento, com órgão, título, ano e URL com data de acesso:

- BRASIL. Lei nº 14.026, de 15 de julho de 2020 (Marco Legal do Saneamento).
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório dos Serviços de Abastecimento de Água* (ano de referência 2024). Brasília, dez. 2025.
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório dos Serviços de Esgotamento Sanitário* (ano de referência 2024). Brasília, dez. 2025.
- BRASIL. Ministério das Cidades. *SINISA 2025 — Relatório de Gestão Municipal* (ano de referência 2024). Brasília, dez. 2025.
- ABES — ASSOCIAÇÃO BRASILEIRA DE ENGENHARIA SANITÁRIA E AMBIENTAL. *Ranking ABES da Universalização do Saneamento 2026*. 2026.
- BRASIL. Ministério da Saúde. DATASUS. Sistema de Informações Hospitalares do SUS (SIH/SUS). Acesso em [data]. (Só se citar a origem das internações usadas pelo ABES; as contagens do SIH/SUS ficam para trabalho futuro.)
- BRASIL. Ministério das Cidades. *PLANSAB — Plano Nacional de Saneamento Básico*, revisão vigente.

**Gestão das referências.** Use Zotero ou Mendeley desde o primeiro dia, com o estilo do modelo Springer indicado pela organização do Rii Forum. Exporte a biblioteca em `.bib` para o repositório. Antes de submeter, confira: todo item citado está na lista e todo item da lista está citado; DOIs resolvem; nenhuma referência aparece em duas versões (preprint e publicada). Documentos brasileiros (leis, relatórios do SINISA, ABES) devem ter título traduzido entre colchetes.

## Título, resumo, palavras-chave e destaques

Estes quatro elementos são escritos por último e são os únicos que a maioria dos leitores vai ler. O editor decide por eles se o artigo vai a revisores.

**Título (12 a 16 palavras).** Fórmula: *[o que o método faz] + [objeto] + [contexto] + [sinal metodológico]*. Evite dois-pontos seguidos de subtítulo genérico ("a multicriteria approach"). Exemplos:

- *Same data, different priorities: how the aggregation rule of a public sanitation ranking shapes municipal prioritisation in Northeast Brazil*
- *Does the aggregation method matter for health? Comparing multicriteria rankings of sanitation against sanitation-related hospitalisations in Northeast Brazil*

**Resumo (no formulário do Rii Forum, siga o limite indicado no próprio formulário, que a chamada não informa; no artigo completo, siga o limite do modelo Springer, em geral até 250 palavras), estruturado mesmo que o evento não exija.** Uma ou duas frases por item, sem citações:

1. Contexto e problema (com um número).
2. Lacuna (uma frase).
3. Objetivo e pergunta.
4. Método: alternativas, número de critérios, base de dados, os quatro métodos e os quatro esquemas de pesos, o teste de validade com a DRSAI, testes de robustez.
5. Resultado principal com número (ex.: *"[n] dos 505 municípios mudam de quartil conforme o método; a ordenação do [método X] é a que mais se associa às internações por DRSAI (ρ = [valor]), [e a diferença para a soma ponderada do ABES é / mas a diferença para os demais não é] distinguível de zero"*).
6. Implicação para a política pública (uma frase).
7. Contribuição metodológica (uma frase).

**Palavras-chave (5 a 6).** Combine: o método (PROMETHEE; TOPSIS; VIKOR; AHP; compensation), o objeto (sanitation; sanitation-related diseases), o contexto (Brazil; semi-arid), e um termo de busca da área (multicriteria decision aid; external validity; public policy). Não repita palavras do título; elas já são indexadas.

**Destaques / Highlights (não exigidos pelos anais Springer; use-os como roteiro do resumo e dos slides).** Um resultado por bullet, nunca uma descrição do que foi feito:

- Four aggregation methods and four weighting schemes (including classic AHP) rank the 505 Northeast Brazil municipalities with complete data, the same set as the official ranking
- [n] municipalities change quartile depending on the aggregation method
- The [method X] ranking shows the strongest association with sanitation-related hospitalisations (ρ = [valor])
- Methods that limit compensation [do / do not] align better with health outcomes
- The result holds within states and municipality size groups

**Teste final:** entregue título, resumo e highlights a alguém da área que não leu o artigo e peça para dizer, em uma frase, qual foi o achado. Se a pessoa descrever o método em vez do achado, reescreva.

## Checklist final e resposta a revisores

**Antes de submeter:**

- [ ] Cada seção abre com sua frase-ponto; o artigo pode ser lido só pelas primeiras frases
- [ ] Pergunta de pesquisa respondida literalmente na Discussão e no Resumo, com número
- [ ] Os três bullets de contribuição da Introdução correspondem a resultados reportados
- [ ] Tabela-síntese da revisão inclui o próprio artigo na última linha
- [ ] Tabela de critérios com unidade, direção, fonte, função de preferência, q e p
- [ ] Desenho métodos × pesos descrito (quatro métodos, quatro esquemas de pesos); frase explícita de que só os pesos do AHP clássico foram definidos pelos autores, com a matriz de Saaty e a RC em apêndice
- [ ] Métodos, pesos e parâmetros fixados antes do teste com a DRSAI, com registro no `log_decisoes.md`; DRSAI fora dos critérios
- [ ] Validade externa reportada com os 16 ρ, os intervalos bootstrap de Δρ e o controle por UF e porte
- [ ] Robustez reportada com métricas (aceitabilidade SMAA, intervalos de estabilidade, τ para q/p, reversão de ordem)
- [ ] Comparação com o Ranking ABES 2026 feita e discutida município a município nas divergências
- [ ] Limitação dos fatores de confusão (renda, atenção primária, acesso hospitalar) redigida, com linguagem de associação em todo o texto
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
| "Por que esses quatro métodos?" | Bloco 3.2 e Seção 4.6 (cobrem o eixo de compensação, da total à limitada) | ELECTRE como método não compensatório em suplemento |
| "Por que não uma regressão da DRSAI sobre os indicadores?" | Seção 2 e Seção 4.7 | O objetivo é avaliar rankings construídos por preferência sobre o desempenho; a DRSAI só testa a coerência deles com a saúde e nunca calibrou nada |
| "A associação pode ser efeito da renda" | Seção 6, limitação de fatores de confusão; controle por UF e porte | Correlação parcial com PIB per capita municipal (IBGE), a covariável mais fácil de obter |
| "Os pesos são arbitrários" | Seção 4.5 e Tabela T2 | Gráfico de walking weights |
| "Os pesos do AHP clássico refletem só a opinião do autor" | Seção 4.5 (RC e matriz em apêndice) e Seção 6, limitação de pesos subjetivos | Sensibilidade aos julgamentos da matriz; mostrar se as conclusões se repetem com os três esquemas que não dependem de julgamento |
| "Não há análise de sensibilidade" | Seção 5.3 e Tabela T3 | Variação de q/p por critério individual |
| "Os dados são autodeclarados" | Seção 6, limitação 2 | Correlação entre SINISA e SIH/SUS como validação cruzada |
| "O caso é local demais" | Introdução, parágrafo 1 e Discussão | Parágrafo ligando o Nordeste ao semiárido global e a economias emergentes |
| "Qual a contribuição teórica?" | Introdução, bullets 2 e 3, e Discussão itens 1 e 3 | Uma frase sobre o que um desfecho externo ensina sobre a escolha da regra de agregação em índices oficiais em geral |
