# %%

dados = [
    "Teo",
    "Calvo",
    32,
    ["jr", "pl", "sr", "head", "pl"],
    ["tapps", "sas", "via", "gc", "globo"],
    [3000, 4500, 7600, 12000, 4500],
]

# %%
# Qual o nome e sobre nome dessa pessoa?
nome_sobrenome = " ".join(dados[0:2])
print(nome_sobrenome)

# %%
# Qual a primeira empresa que ela trabalhou?
dados[-2][0]

# %%
# Qual as duas últimas posiçoes no mercado (senioridade)?
cargos = " / ".join(dados[-3][-2:])
print(cargos)

# %%
# Mostre os saltos de 2 em 2 empresas dessa pessoa.
saltos = "->".join(dados[-2][::2])
print(saltos)

# %%
# Mostre o salário do último para o primeiro
dados[-1][::-1]
# %%
