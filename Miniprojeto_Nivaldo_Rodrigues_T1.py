
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