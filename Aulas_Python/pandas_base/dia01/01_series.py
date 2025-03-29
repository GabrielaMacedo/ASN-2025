# %%
import pandas as pd

# %%
idade = [32,12,43,26,72,13,45,32,67,86,34]

media = sum(idade) / len(idade)
print("Média:", media)

total = 0
for i in idade:
    total += ((i -media) ** 2)

variancia = total / (len(idade)-1)
print("Variância:", media)

# %%
idades_series = pd.Series(idade)
idades_series

# %%
idades_series.mean()

# %%
idades_series.var()

# %%
idades_series.median()

# %%
idades_series.describe()

# %%

idades_series = pd.Series(idade, name="idades")
idades_series

# %%
idade[0]

# %%
idades_series = idades_series.sort_values()
idades_series

# %%
idades_series.iloc[0] # é posiçao na series

idades_series.loc[0]    # é o valor do índide
idades_series[0]        # é o valor do índide

# %%
idades_series.shape

# %%

idades_series.index  = ["a", "b", "c",
                        'd', 'e', "f",
                        "h", "i", "j",
                        "k", "e"]

idades_series['e']