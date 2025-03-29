# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",delimiter=';')
clientes

# %%
clientes[clientes["dtCriacao"].isna()]

# %%
# clientes[~clientes["dtCriacao"].isna()]

clientes[clientes["dtCriacao"].notna()]

# %%

produtos = pd.read_csv("../data/produtos.csv",delimiter=";")

filter_produtos = ['Lista de presença',
                   'Presença Streak',
                   'Resgatar Ponei']

filtro = produtos["descProduto"].isin(filter_produtos)

produtos[filtro]

# %%