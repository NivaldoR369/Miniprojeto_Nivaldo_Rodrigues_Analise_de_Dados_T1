
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
df = pd.read_csv("Base Varejo.csv", sep=";" )

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
#quantidade_compras = df["CO_ID"].nunique()
#Isso demonstra a regra de negócio.

