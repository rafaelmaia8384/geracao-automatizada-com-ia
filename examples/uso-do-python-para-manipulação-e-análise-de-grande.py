# Uso do Python para manipulação e análise de grandes conjuntos de dados utilizando a biblioteca Pandas.

import pandas as pd

# Carregando um conjunto de dados

data_frame = pd.read_csv('nome_do_arquivo.csv')

# Exibindo as primeiras linhas do conjunto de dados

print(data_frame.head())

# Verificando o tamanho do conjunto de dados

print('Tamanho do conjunto de dados:', data_frame.shape)

# Descrição estatística do conjunto de dados

print(data_frame.describe())

# Selecionando uma coluna específica

column = data_frame['nome_da_coluna']
print(column)

# Realizando uma operação de agrupamento

grouped = data_frame.groupby('nome_da_coluna').mean()
print(grouped)

# Aplicando uma função a uma coluna

data_frame['nova_coluna'] = data_frame['nome_da_coluna'].apply(lambda x: x*2)
print(data_frame.head())