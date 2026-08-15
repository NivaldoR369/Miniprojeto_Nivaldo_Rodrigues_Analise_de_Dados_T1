
# importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# SPRINT 1 - IMPORTAÇÃO E CONHECIMENTO DA BASE
print("\n" + "=" * 60)
print("SPRINT 1 - IMPORTAÇÃO DOS DADOS")
print("=" * 60)

# Carregamento da base
df = pd.read_csv("Base Varejo.csv", sep=";", encoding="utf-8")
print("\nBase carregada com sucesso!")

# Dimensões da base
print("\nNúmero de registros e colunas:")
print(df.shape)

print(f"\nNúmero de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")

# Nome das colunas
print("\nColunas da base:")
print(df.columns.tolist())

# Tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

# Primeiros registros
print("\nPrimeiros registros:")
print(df.head())
# Valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Duplicatas
print("\nQuantidade de registros duplicados:")
print(df.duplicated().sum())

# SPRINT 2 - TRANSFORMAÇÃO DOS DADOS
print("\n" + "=" * 60)
print("SPRINT 2 - TRANSFORMAÇÃO DOS DADOS")
print("=" * 60)

# Remover colunas totalmente vazias
df = df.dropna(axis=1, how="all")
print("\nColunas após remover colunas totalmente vazias:")
print(df.columns.tolist())

# Colunas de texto
colunas_texto = [
    "CL_GENERO",
    "CL_SEG",
    "PR_CAT",
    "PR_NOME"
]

# Limpeza das strings
for coluna in colunas_texto:
    df[coluna] = (
        df[coluna]
        .astype(str)
        .str.strip()
        .str.upper()
        .str.replace(r"\s+", " ", regex=True) )
print("\nStrings normalizadas com sucesso.")

# Colunas numéricas
colunas_numericas = [
    "CO_ID",
    "CL_ID",
    "CL_EC",
    "CL_FHL",
    "PR_ID"
]
for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )
print("\nTipos numéricos ajustados:")
print(df[colunas_numericas].dtypes)

# Conversão da coluna DATA para datetime
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)
print("\nTipo da coluna DATA após conversão:")
print(df["DATA"].dtype)
datas_invalidas = df["DATA"].isna().sum()
print(f"\nQuantidade de datas inválidas: {datas_invalidas}")

# SPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS
print("\n" + "=" * 60)
print("SPRINT 3 - LIMPEZA")
print("=" * 60)
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Tratamento de categorias ausentes/inconsistentes
def tratar_categoria(valor):
    if pd.isna(valor):
        return "SEM CATEGORIA"
    elif str(valor).strip().upper() in ["#N/D", "N/D", "ND", ""]:
        return "SEM CATEGORIA"
    else:
        return str(valor).strip().upper()
df["PR_CAT"] = df["PR_CAT"].apply(tratar_categoria)
print("\nCategorias após tratamento:")
print(df["PR_CAT"].value_counts())


#Justificativa da remoção 
#Não vamos remover registros apenas porque possuem o mesmo CO_ID, 
# porque uma compra pode conter vários produtos.
#Isso é uma decisão importante de qualidade de dados.

#retirando as duplicadas
duplicatas_antes = df.duplicated().sum()
print(f"\nDuplicatas encontradas: {duplicatas_antes}")
df = df.drop_duplicates()
duplicatas_depois = df.duplicated().sum()
print(f"Duplicatas após limpeza: {duplicatas_depois}")
print(f"\nRegistros após limpeza: {len(df)}")

# Regra de negócio do número da compra:
# A coluna CO_ID representa o identificador da compra.
# Precisamos ter cuidado para não considerar todas as linhas de um mesmo CO_ID como duplicadas,
# porque uma compra pode possuir vários produtos.
#Vamos verificar:
quantidade_compras = df["CO_ID"].nunique()
print(f"\nQuantidade de compras distintas: {quantidade_compras}")
print("\nQuantidade de itens por compra:")
print(df.groupby("CO_ID").size().describe())
#Isso demonstra a regra de negócio.

# SPRINT 4 - ESTATÍSTICAS E AGRUPAMENTOS
#— Estatísticas do número de filhos
print("\n" + "=" * 60)
print("SPRINT 4 - ESTATÍSTICAS DESCRITIVAS")
print("=" * 60)
filhos = df["CL_FHL"]
print("\nEstatísticas do número de filhos:")
print(f"Contagem: {filhos.count()}")
print(f"Média: {filhos.mean():.2f}")
print(f"Mediana: {filhos.median():.2f}")
print(f"Desvio padrão: {filhos.std():.2f}")
print(f"Moda: {filhos.mode().tolist()}")
print(f"Mínimo: {filhos.min()}")
print(f"Máximo: {filhos.max()}")
print(f"Q1: {filhos.quantile(0.25):.2f}")
print(f"Q3: {filhos.quantile(0.75):.2f}")

#Primeiro agrupamento — gênero
print("\n" + "-" * 60)
print("AGRUPAMENTO 1 - GÊNERO")
print("-" * 60)
agrupamento_genero = (
    df.groupby("CL_GENERO").agg(
        compras=("CO_ID", "nunique"),
        itens=("CO_ID", "size"),
        clientes=("CL_ID", "nunique")
    )
    .sort_values("compras", ascending=False) )
print(agrupamento_genero)

#Segundo agrupamento — categoria de produto
print("\n" + "-" * 60)
print("AGRUPAMENTO 2 - CATEGORIA")
print("-" * 60)
agrupamento_categoria = (
    df.groupby("PR_CAT")
    .agg(
        compras=("CO_ID", "nunique"),
        itens=("CO_ID", "size"),
        clientes=("CL_ID", "nunique")).sort_values("itens", ascending=False))
print(agrupamento_categoria)

#Verificar categorias depois da limpeza
print("\nDistribuição das categorias:")
print(df["PR_CAT"].value_counts())
#Análise temporal
print("\n" + "-" * 60)
print("ANÁLISE TEMPORAL")
print("-" * 60)
df["ANO_MES"] = df["DATA"].dt.to_period("M")
vendas_mensais = (
    df.groupby("ANO_MES")
    .size()
    .sort_index()
)
print(vendas_mensais)

#  CRIAÇÃO DA PASTA DE GRÁFICOS
import os
os.makedirs("graficos", exist_ok=True)

# GRÁFICO 1 - REGISTROS AO LONGO DO TEMPO
registros_data = (
    df.groupby("DATA")
      .size()
      .reset_index(name="Quantidade")
)
plt.figure(figsize=(12, 6))
plt.plot(
    registros_data["DATA"],
    registros_data["Quantidade"]
)
plt.title("Quantidade de Registros ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Quantidade de Registros")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig(
    "graficos/01_registros_ao_longo_do_tempo.png",
    dpi=300
)
plt.show()

# GRAFICO 2 - REGISTROS POR CATEGORIA
categoria = (
    df["PR_CAT"]
    .value_counts()
    .sort_values(ascending=True)
)
plt.figure(figsize=(10, 6))
categoria.plot(kind="barh")
plt.title("Quantidade de Registros por Categoria de Produto")
plt.xlabel("Quantidade de Registros")
plt.ylabel("Categoria")
plt.tight_layout()
plt.savefig(
    "graficos/02_registros_por_categoria.png",
    dpi=300
)
plt.show()

# GRÁFICO 3 - TOP 10 PRODUTOS
top_produtos = (
    df["PR_NOME"]
    .value_counts()
    .head(10)
    .sort_values(ascending=True)
)
plt.figure(figsize=(10, 6))
top_produtos.plot(kind="barh")
plt.title("Top 10 Produtos com Maior Número de Registros")
plt.xlabel("Quantidade de Registros")
plt.ylabel("Produto")
plt.tight_layout()
plt.savefig(
    "graficos/03_top_10_produtos.png",
    dpi=300
)
plt.show()

# GRÁFICO 4 - DISTRIBUIÇÃO POR GÊNERO
genero = df["CL_GENERO"].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    genero.values,
    labels=genero.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribuição dos Registros por Gênero")
plt.tight_layout()
plt.savefig(
    "graficos/04_distribuicao_genero.png",
    dpi=300
)
plt.show()

# GRÁFICO 5 - DISTRIBUIÇÃO POR SEGMENTO
segmento = df["CL_SEG"].value_counts()
plt.figure(figsize=(8, 5))
segmento.plot(kind="bar")
plt.title("Quantidade de Registros por Segmento de Cliente")
plt.xlabel("Segmento")
plt.ylabel("Quantidade de Registros")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(
    "graficos/05_registros_por_segmento.png",
    dpi=300
)
plt.show()

# GRÁFICO 6 - REGISTROS POR EMPRESA/LOJA
empresa = (
    df["CO_ID"]
    .value_counts()
    .sort_values(ascending=False)
)
plt.figure(figsize=(10, 6))
empresa.plot(kind="bar")
plt.title("Quantidade de Registros por Empresa/Loja")
plt.xlabel("Empresa/Loja (CO_ID)")
plt.ylabel("Quantidade de Registros")
plt.tight_layout()
plt.savefig(
    "graficos/06_registros_por_empresa.png",
    dpi=300
)
plt.show()


# GRÁFICO 7 - TOP 10 CLIENTES
top_clientes = (
    df["CL_ID"]
    .value_counts()
    .head(10)
    .sort_values(ascending=True)
)
plt.figure(figsize=(10, 6))
top_clientes.plot(kind="barh")
plt.title("Top 10 Clientes por Número de Registros")
plt.xlabel("Quantidade de Registros")
plt.ylabel("Cliente")
plt.tight_layout()
plt.savefig(
    "graficos/07_top_10_clientes.png",
    dpi=300
)
plt.show()

# FINALIZAÇÃO
print("\n============================================")
print("ANÁLISE CONCLUÍDA!")
print("============================================")
print("Os gráficos foram salvos na pasta 'graficos'.")
print("Foram gerados 7 gráficos.")
