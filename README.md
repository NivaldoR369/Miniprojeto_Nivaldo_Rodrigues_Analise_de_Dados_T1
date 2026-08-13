# Mini-Projeto Avaliativo — Análise Exploratória de Dados no Varejo

**Aluno:** Nivaldo Rodrigues
**Turma:** Analise_de_Dados_T5
**Disciplina:** Análise de Dados
**Projeto:** Análise Exploratória de Dados aplicada ao Varejo
**Linguagem:** Python
**Biblioteca principal:** Pandas, secundaria: Numpy, Matplotlib

---

## 1. Apresentação do Projeto

Este projeto apresenta uma **Análise Exploratória de Dados (AED)** aplicada a uma base de dados de varejo.

O objetivo principal é demonstrar como dados brutos podem ser carregados, analisados, tratados, transformados e organizados para posteriormente serem utilizados em análises mais avançadas, relatórios ou ferramentas de Business Intelligence (BI).

A análise foi desenvolvida utilizando a linguagem **Python** e a biblioteca **Pandas**, seguindo uma sequência de etapas de tratamento e exploração dos dados.

Durante o desenvolvimento foram realizadas atividades de:

- importação da base de dados;
- identificação da estrutura da tabela;
- verificação dos tipos de dados;
- identificação de valores ausentes;
- identificação de registros duplicados;
- tratamento de categorias inconsistentes;
- transformação de strings;
- conversão de dados numéricos;
- conversão de datas para o tipo `datetime`;
- remoção de duplicatas;
- cálculo de estatísticas descritivas;
- agrupamento dos dados;
- análise temporal;
- interpretação dos principais resultados.

---

# 2. Contextualização

A análise exploratória de dados é uma etapa importante no processo de preparação de informações para tomada de decisão.
Em uma situação real de trabalho, os dados normalmente não chegam completamente preparados. Podem existir registros duplicados, valores ausentes, erros de preenchimento, categorias inconsistentes e tipos de dados inadequados.
Por esse motivo, antes de produzir gráficos, indicadores ou dashboards, é necessário verificar a qualidade da base.

Neste projeto foi utilizada uma base de dados de varejo contendo informações relacionadas a:

- compras;
- clientes;
- gênero;
- segmento;
- escolaridade;
- número de filhos;
- produtos;
- categorias;
- datas.

A análise procura transformar esses dados brutos em informações que permitam compreender melhor o comportamento dos registros de compra.
# 3. Objetivos
## 3.1 Objetivo Geral

Realizar uma Análise Exploratória de Dados utilizando Python e Pandas, identificando problemas de qualidade, realizando a limpeza e transformação dos dados e obtendo informações por meio de estatísticas descritivas e agrupamentos.
## 3.2 Objetivos Específicos

- Carregar a base de dados utilizando Pandas;
- verificar a quantidade de registros e colunas;
- identificar os tipos de dados;
- verificar valores nulos;
- identificar registros duplicados;
- identificar inconsistências nas categorias;
- transformar dados de texto;
- converter colunas numéricas;
- converter a coluna de data para `datetime`;
- remover registros duplicados;
- tratar categorias não identificadas;
- calcular estatísticas sobre o número de filhos dos clientes;
- realizar agrupamentos por gênero e categoria;
- realizar uma análise temporal;
- apresentar conclusões sobre os principais resultados.

-4. Fonte dos Dados
A base utilizada neste projeto foi a base de varejo disponibilizada para o Mini-Projeto Avaliativo.
Arquivo utilizado:
```text
Base Varejo.csv
```
A base foi carregada localmente no projeto e utilizada como fonte para todas as etapas de análise.
---

# 5. Tecnologias Utilizadas

Para o desenvolvimento do projeto foram utilizadas as seguintes tecnologias:

### Python

Linguagem de programação utilizada para desenvolver o script de análise.

### Pandas

Biblioteca utilizada para:

- leitura do arquivo CSV;
- manipulação dos dados;
- tratamento de valores ausentes;
- remoção de duplicatas;
- conversão de tipos;
- agrupamentos;
- cálculos estatísticos.

### VS Code

Ambiente utilizado para desenvolvimento e execução do programa.

### Git

Sistema utilizado para controle de versões do projeto.

### GitHub

Plataforma utilizada para armazenamento e publicação do repositório.

---

# 6. ETL e Qualidade dos Dados

## 6.1 O que é ETL?

ETL é uma sigla para:

**Extract — Transform — Load**

Em português:

**Extração — Transformação — Carga**

O processo ETL é utilizado para preparar dados provenientes de diferentes fontes para análise.

Neste projeto, o conceito de ETL pode ser observado da seguinte forma:

### Extract — Extração

A extração ocorreu quando o arquivo:

```text
Base Varejo.csv
```

foi carregado utilizando o Pandas.

Foi utilizado:

```python
df = pd.read_csv("Base Varejo.csv", sep=";")
```

O método `read_csv()` realiza a leitura do arquivo CSV e transforma os dados em um DataFrame.

---

## 6.2 Transform — Transformação

A transformação ocorreu durante as etapas de:

- limpeza das strings;
- conversão das colunas numéricas;
- conversão da coluna de data;
- tratamento das categorias;
- remoção das duplicatas.

Por exemplo, a coluna `DATA`, inicialmente armazenada como texto, foi transformada para o tipo `datetime`.

```python
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)
```

Essa transformação é importante porque permite realizar operações temporais posteriormente.

---

## 6.3 Load — Carga

Neste projeto, o resultado tratado permanece disponível no DataFrame `df`, podendo posteriormente ser exportado para outro arquivo ou utilizado em uma ferramenta de Business Intelligence.

O objetivo é deixar os dados preparados para uma possível etapa posterior de análise, visualização ou construção de dashboard.

---

# 7. Qualidade dos Dados

A qualidade dos dados é fundamental para que uma análise produza resultados confiáveis.

Durante o projeto foram verificados diferentes aspectos da qualidade da base:

- completude;
- consistência;
- duplicidade;
- formato;
- tipos de dados;
- validade das datas;
- padronização das categorias.

Foram identificados problemas que poderiam prejudicar uma análise posterior.

Entre eles destacam-se:

- colunas completamente vazias;
- registros duplicados;
- categorias representadas por `#N/D`;
- coluna de data armazenada inicialmente como texto.

Esses problemas foram tratados durante o processo de limpeza.

---

# 8. Sprint 1 — Importação dos Dados

A primeira etapa do projeto teve como objetivo conhecer a estrutura inicial da base.

Foi utilizada a biblioteca Pandas:

```python
import pandas as pd
```

Depois a base foi carregada:

```python
df = pd.read_csv("Base Varejo.csv", sep=";")
```

O parâmetro:

```python
sep=";"
```

foi utilizado porque os campos do arquivo CSV estão separados por ponto e vírgula.

---

## 8.1 Verificação da quantidade de registros

Foi utilizado:

```python
df.shape
```

O atributo `shape` informa a quantidade de linhas e colunas do DataFrame.

A base inicialmente apresentou:

- **830.000 registros**
- **14 colunas**

---

## 8.2 Identificação das colunas

Foi utilizado:

```python
df.columns.tolist()
```

Esse comando apresenta os nomes das colunas existentes na base.

---

## 8.3 Verificação dos tipos de dados

Foi utilizado:

```python
df.dtypes
```

Essa função permite verificar se cada coluna está armazenada como texto, número, data ou outro tipo.

Essa verificação é importante porque uma coluna que representa uma data, por exemplo, não deve permanecer como texto quando será utilizada em análises temporais.

---

## 8.4 Verificação de valores nulos

Foi utilizado:

```python
df.isnull().sum()
```

O comando calcula a quantidade de valores ausentes em cada coluna.

Essa etapa permite identificar possíveis problemas de completude dos dados.

---

## 8.5 Identificação de duplicatas

Foi utilizado:

```python
df.duplicated().sum()
```

Foram encontrados:

**96.553 registros duplicados exatos.**

A identificação dessas duplicidades foi importante para evitar que os mesmos registros fossem contabilizados mais de uma vez.

---

# 9. Sprint 2 — Transformação dos Dados

Na segunda Sprint foram realizadas transformações necessárias para melhorar a qualidade e a padronização dos dados.

---

## 9.1 Remoção de colunas completamente vazias

A base apresentava quatro colunas sem informações relevantes.

Foi utilizado:

```python
df = df.dropna(axis=1, how="all")
```

O parâmetro:

```text
axis=1
```

indica que estamos trabalhando com colunas.

O parâmetro:

```text
how="all"
```

determina que a coluna somente será removida quando todos os seus valores forem ausentes.

Essa abordagem evita eliminar colunas que possuem pelo menos alguma informação.

---

# 10. Limpeza das Strings

As colunas de texto foram padronizadas.

Foram utilizadas operações como:

```python
.str.strip()
```

para remover espaços desnecessários no início e no final dos textos.

Também foi utilizado:

```python
.str.upper()
```

para transformar os textos em letras maiúsculas.

Foi utilizada expressão regular:

```python
.str.replace(r"\s+", " ", regex=True)
```

Essa expressão substitui sequências de espaços repetidos por apenas um espaço.

A padronização reduz problemas causados por diferentes formas de representação de uma mesma informação.

---

# 11. Conversão dos Dados Numéricos

Algumas colunas foram convertidas para formato numérico utilizando:

```python
pd.to_numeric()
```

Foi utilizada a opção:

```python
errors="coerce"
```

Essa opção transforma valores que não podem ser convertidos em números em valores ausentes (`NaN`), permitindo que sejam identificados e tratados posteriormente.

As principais colunas numéricas analisadas foram:

- `CO_ID`;
- `CL_ID`;
- `CL_EC`;
- `CL_FHL`;
- `PR_ID`.

---

# 12. Conversão da Data

A coluna:

```text
DATA
```

estava originalmente armazenada como texto.

Foi realizada a conversão para o tipo `datetime`:

```python
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)
```

O formato:

```text
%d/%m/%Y
```

representa:

- `%d` → dia;
- `%m` → mês;
- `%Y` → ano.

Depois da conversão, a coluna passou a poder ser utilizada em análises temporais.

Também foi realizada uma verificação:

```python
df["DATA"].isna().sum()
```

para identificar possíveis datas inválidas.

---

# 13. Sprint 3 — Limpeza de Nulos e Duplicatas

A terceira Sprint teve como objetivo tratar os problemas identificados anteriormente.

---

## 13.1 Tratamento de categorias

A coluna:

```text
PR_CAT
```

apresentava registros classificados como:

```text
#N/D
```

Esse valor representa uma categoria não identificada.

Foi criada uma função utilizando estrutura condicional:

```python
def tratar_categoria(valor):
    if pd.isna(valor):
        return "SEM CATEGORIA"
    elif str(valor).strip().upper() in ["#N/D", "N/D", "ND", ""]:
        return "SEM CATEGORIA"
    else:
        return str(valor).strip().upper()
```

Essa função utiliza:

- `if`;
- `elif`;
- `else`.

Os registros sem categoria foram padronizados como:

```text
SEM CATEGORIA
```

Essa transformação evita que diferentes representações de ausência de informação sejam tratadas como categorias diferentes.

---

# 14. Tratamento das Duplicatas

Antes da remoção foram identificados:

**96.553 registros duplicados.**

Foi utilizado:

```python
df = df.drop_duplicates()
```

Após o procedimento, as duplicatas exatas foram eliminadas.

É importante destacar que foram removidas apenas duplicatas completas.

Não foram eliminados registros apenas porque possuíam o mesmo identificador de compra (`CO_ID`).

Isso ocorre porque uma mesma compra pode conter vários produtos.

Portanto, duas linhas com o mesmo `CO_ID` não significam necessariamente que sejam duplicadas.

---

# 15. Regra de Negócio do Identificador da Compra

A coluna:

```text
CO_ID
```

representa o identificador da compra.

Foi utilizada:

```python
df["CO_ID"].nunique()
```

para identificar a quantidade de compras distintas.

Também foi analisada a quantidade de itens por compra:

```python
df.groupby("CO_ID").size().describe()
```

Essa análise ajuda a compreender que uma compra pode possuir vários registros de produtos.

Dessa forma, não seria correto simplesmente eliminar todas as linhas que possuem o mesmo `CO_ID`.

---

# 16. Estatísticas Descritivas — Número de Filhos

Uma das exigências do projeto foi realizar estatísticas descritivas da coluna:

```text
CL_FHL
```

Essa coluna representa o número de filhos dos clientes.

Foram calculadas as seguintes medidas:

- contagem;
- média;
- mediana;
- desvio padrão;
- moda;
- mínimo;
- máximo;
- primeiro quartil (Q1);
- terceiro quartil (Q3).

---

## 16.1 Média

Foi utilizado:

```python
filhos.mean()
```

A média encontrada foi aproximadamente:

**1,15 filho por registro.**

A média representa o valor central obtido pela soma dos valores dividida pela quantidade de observações.

---

## 16.2 Mediana

Foi utilizado:

```python
filhos.median()
```

A mediana encontrada foi:

**0 filhos.**

Isso significa que pelo menos metade das observações apresenta número de filhos igual ou inferior a zero, considerando a distribuição da variável.

---

## 16.3 Moda

Foi utilizado:

```python
filhos.mode()
```

A moda encontrada foi:

**0 filhos.**

Portanto, zero é o número de filhos que aparece com maior frequência na base analisada.

---

## 16.4 Desvio padrão

Foi utilizado:

```python
filhos.std()
```

O desvio padrão foi aproximadamente:

**1,42.**

Essa medida indica a dispersão dos valores em relação à média.

---

## 16.5 Mínimo e máximo

Foram utilizados:

```python
filhos.min()
```

e:

```python
filhos.max()
```

Os valores encontrados foram:

- mínimo: **0**
- máximo: **4**

---

## 16.6 Quartis

Foram calculados:

```python
filhos.quantile(0.25)
```

para Q1 e:

```python
filhos.quantile(0.75)
```

para Q3.

Os resultados aproximados foram:

- Q1 = **0**
- Q3 = **2**

Os quartis permitem compreender melhor a distribuição dos dados.

---

# 17. Sprint 4 — Agrupamentos

A análise exploratória também buscou identificar padrões de agrupamento.

Foram realizados pelo menos dois agrupamentos utilizando o método:

```python
groupby()
```

---

# 18. Agrupamento 1 — Gênero

O primeiro agrupamento foi realizado pela coluna:

```text
CL_GENERO
```

Foi utilizado:

```python
df.groupby("CL_GENERO")
```

Foram analisados:

- quantidade de compras;
- quantidade de itens;
- quantidade de clientes.

O resultado indicou que o gênero:

**F**

apresentou maior quantidade de compras distintas do que o gênero:

**M**.

Os valores encontrados foram aproximadamente:

- F: **9.615 compras distintas**
- M: **8.856 compras distintas**

Esse resultado representa uma diferença na quantidade de compras observadas entre os grupos.

---

# 19. Agrupamento 2 — Categoria

O segundo agrupamento foi realizado pela coluna:

```text
PR_CAT
```

Foi utilizado:

```python
df.groupby("PR_CAT")
```

Foram analisadas:

- compras;
- itens;
- clientes.

A categoria que apresentou maior quantidade de itens foi:

**ALIMENTOS**

seguida pelas demais categorias.

A distribuição encontrada após o tratamento apresentou aproximadamente:

| Categoria     | Quantidade de itens |
| ------------- | ------------------: |
| ALIMENTOS     |             384.197 |
| HIGIENE       |             137.702 |
| LIMPEZA       |             128.632 |
| BEBIDAS       |              38.264 |
| PET           |              28.553 |
| ACESSORIOS    |              12.871 |
| SEM CATEGORIA |               3.228 |

Esses resultados demonstram a predominância da categoria ALIMENTOS na base analisada.

---

# 20. Análise Temporal

Também foi realizada uma análise da quantidade de registros ao longo do tempo.

Para isso foi criada uma nova variável:

```python
df["ANO_MES"] = df["DATA"].dt.to_period("M")
```

Depois foi utilizado:

```python
df.groupby("ANO_MES").size()
```

Esse procedimento permite observar a quantidade de registros por mês.

Como a base utilizada não apresenta uma coluna de valor monetário de venda, a análise temporal foi realizada considerando a quantidade de registros/itens, e não faturamento.

Essa decisão foi tomada para não criar informações que não estão presentes na base original.

---

# 21. Principais Insights

A partir da análise realizada, foram identificados os seguintes insights:

### 1. Grande volume de dados

A base inicial possui **830.000 registros**, apresentando quantidade suficiente para uma análise exploratória de dados de varejo.

### 2. Existência de duplicatas

Foram identificados **96.553 registros duplicados exatos**. A remoção desses registros foi necessária para reduzir o risco de contagens duplicadas nas análises.

### 3. Predominância da categoria ALIMENTOS

A categoria **ALIMENTOS** apresentou a maior quantidade de registros, com aproximadamente **384 mil itens**, indicando forte predominância dessa categoria na base analisada.

### 4. Maior quantidade de compras no gênero F

O agrupamento por gênero mostrou aproximadamente **9.615 compras distintas para F** e **8.856 para M**, indicando maior quantidade de compras distintas no grupo F.

### 5. Distribuição do número de filhos

A variável número de filhos apresentou média aproximada de **1,15**, mediana igual a **0** e moda igual a **0**. Isso demonstra que os registros com zero filhos possuem grande participação na base.

### 6. Necessidade de tratamento da qualidade

A existência de duplicatas, categorias `#N/D` e colunas completamente vazias demonstra a importância da etapa de limpeza antes da utilização dos dados em relatórios ou dashboards.

---

# 22. Problemas Remanescentes e Limitações

Apesar das etapas de limpeza, algumas limitações permanecem.

A principal limitação é que a base utilizada não apresenta uma coluna específica de valor monetário das vendas.

Por esse motivo, não foi possível calcular:

- faturamento;
- ticket médio;
- receita por categoria;
- receita por gênero;
- evolução financeira das vendas.

Assim, os agrupamentos foram realizados utilizando quantidade de compras, itens e clientes.

Outra limitação é que o tratamento de categorias não identificadas não recupera a categoria original. Os registros foram apenas classificados como:

```text
SEM CATEGORIA
```

Isso preserva os registros sem atribuir uma informação que não estava presente na fonte.

---

# 23. Reprodutibilidade

O projeto foi desenvolvido para que possa ser executado novamente em outro computador.

Para executar o projeto é necessário possuir:

- Python instalado;
- biblioteca Pandas instalada;
- arquivo `Base Varejo.csv`;
- arquivo `Miniprojeto_Nivaldo_Rodrigues_T1.py`.

Instalação do Pandas:

```bash
pip install pandas
```

Execução:

```bash
python Miniprojeto_Nivaldo_Rodrigues_T1.py
```

O arquivo CSV deve permanecer na mesma pasta do arquivo Python.

---

# 24. Estrutura do Repositório

A estrutura do projeto é:

```text
Miniprojeto_Nivaldo_Rodrigues_Analise_de_Dados_T1/
│
├── Base Varejo.csv
│
├── Miniprojeto_Nivaldo_Rodrigues_T1.py
│
├── README.md
│
└── README_Nivaldo_Rodrigues_Analise_de_Dados_T1.md
```

---

# 25. Versionamento com Git

O desenvolvimento do projeto foi organizado em etapas utilizando Git.

O objetivo foi demonstrar a evolução do trabalho por meio de commits, conforme solicitado na atividade.

## Sprint 1

```text
Sprint 1: importacao e analise inicial dos dados
```

Nesta etapa foram realizados:

- criação do projeto;
- importação do CSV;
- identificação das colunas;
- identificação dos tipos;
- verificação de nulos;
- identificação de duplicatas.

## Sprint 2

```text
Sprint 2: limpeza de strings, tipos numericos e datas
```

Nesta etapa foram realizados:

- remoção das colunas totalmente vazias;
- padronização de strings;
- utilização de expressão regular;
- conversão das colunas numéricas;
- conversão da coluna DATA para datetime.

## Sprint 3

```text
Sprint 3: tratamento de categorias, nulos e duplicatas
```

Nesta etapa foram realizados:

- tratamento da categoria `#N/D`;
- criação da categoria `SEM CATEGORIA`;
- utilização de `if/elif/else`;
- identificação das duplicatas;
- remoção das duplicatas;
- análise da regra de negócio do `CO_ID`.

## Sprint 4

```text
Sprint 4: estatisticas agrupamentos e conclusoes
```

Nesta etapa foram realizados:

- estatísticas descritivas;
- análise do número de filhos;
- agrupamento por gênero;
- agrupamento por categoria;
- análise temporal;
- elaboração das conclusões.

## Sprint 5

```text
Sprint 5: documentacao final do projeto
```

Nesta etapa foram realizados:

- criação do README;
- documentação do projeto;
- explicação do processo ETL;
- explicação da qualidade dos dados;
- apresentação dos insights;
- revisão final da estrutura do projeto.

---

# 26. Considerações Finais

A realização deste Mini-Projeto permitiu compreender que a análise de dados não começa diretamente pela construção de gráficos ou dashboards.

Antes da análise propriamente dita, é necessário compreender a origem dos dados, verificar sua estrutura e avaliar sua qualidade.

A utilização do Pandas permitiu automatizar diversas tarefas, como leitura do CSV, identificação de valores ausentes, remoção de duplicatas, transformação de tipos, conversão de datas, agrupamentos e cálculo de estatísticas.

O projeto também demonstrou a importância do processo ETL, principalmente da etapa de transformação, pois dados inconsistentes ou duplicados podem produzir resultados incorretos.

A análise mostrou que a base apresenta grande volume de registros e padrões interessantes relacionados às categorias de produtos, gênero dos clientes e número de filhos.

Além disso, o desenvolvimento utilizando Git e GitHub permitiu organizar o projeto por etapas, mantendo um histórico das alterações realizadas.

Dessa forma, o projeto representa uma aplicação prática dos conceitos de **Análise Exploratória de Dados, qualidade de dados, ETL, Python, Pandas e controle de versão**, preparando a base para análises posteriores e possíveis aplicações em ferramentas de Business Intelligence.

---

## 27. Autor

**Nivaldo Rodrigues**

Mini-Projeto Avaliativo — Análise de Dados

**Turma:** Analise_de_Dados_T1

**Ano:** 2026
