# %%

import pandas as pd

import os

# %%

os.getcwd()

# %%
df = pd.read_csv("../data/clientes.csv",delimiter=";")

df

# %%
df.to_excel("clientes.xlsx", index=False)

# %%
df_excel = pd.read_excel("clientes.xlsx")
df_excel

# %%
df.to_parquet("clientes.parquet")

# %%
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.to_parquet("transacoes.parquet", index=False)

# %%

df_trans = pd.read_parquet("transacao.parquet")

# %%
ufs = pd.read_clipboard(header=None)
ufs.columns

# %%
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
# %%
uf = dfs[1]

# %%
uf.to_csv("ufs.csv", index=False, sep=";")