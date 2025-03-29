# %%

idades = [32,43,23,43,31,56,43]

indice = 0
while indice < len(idades):
    print(indice, idades[indice])
    indice += 1

# %%
for valor in idades:
    print(valor)

# %%
for indice in range(len(idades)):
    print(indice, idades[indice])

# %%

dados = {
    "nome": "Teo",
    "sobrenone": "Calvo",
    "idade": 32,
    "cargos": ["jr", "pl", "sr", "head", "pl"],
    "empresas": ["tapps", "sas", "via", "gc", "globo"],
    "salarios": [3000, 4500, 7600, 12000, 4500],
}

for i in range(len(dados["cargos"])):
    cargo = dados["cargos"][i]
    empresa = dados["empresas"][i]
    salario = dados["salarios"][i]
    print(f"Cargo: {cargo} | Empresa {empresa} | Salario R${salario} ")

# %%

for (chave, valor) in dados.items():
    print(chave, "->", valor)

# %%

values = list(zip(dados["cargos"], dados["empresas"], dados["salarios"]))

for i, j, k in values:
    print(f"Cargo: {i} | Empresa {j} | Salario R${k} ")