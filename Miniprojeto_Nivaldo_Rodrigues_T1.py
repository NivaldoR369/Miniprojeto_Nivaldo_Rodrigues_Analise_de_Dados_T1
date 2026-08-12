
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
df = pd.read_csv("Base Varejo.csv", sep=";")

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


