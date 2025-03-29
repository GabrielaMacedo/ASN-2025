# %%

lista = [1,2,3,4,5]
lista_01 = [1]

tupla = (1,2,3,4,5)
tupla_01 = (1,)

dicionario = {"nome": "teo", "idade": 32}
# %%

import pandas as pd

s = pd.Series(lista)
s

# %%
teo = pd.Series(dicionario)
teo
# %%
