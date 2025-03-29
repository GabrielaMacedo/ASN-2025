# %%

dados = {
    "nome": "Teo",
    "sobrenone": "Calvo",
    "idade": 32,
    "cargos": ["jr", "pl", "sr", "head", "pl"],
    "empresas": ["tapps", "sas", "via", "gc", "globo"],
    "salarios": [3000, 4500, 7600, 12000, 4500],
}

dados

# %%
dados["nome"]

# %%
dados["empresas"][-1]

# %%

dados["nome"] = "e agora?"
dados

# %%

endereco = {
    "cep": "19061-070",
    "logradouro": "Rua Antônio Almodova",
    "complemento": "",
    "unidade": "",
    "bairro": "Jardim Aquinópolis",
    "localidade": "Presidente Prudente",
    "uf": "SP",
    "estado": "São Paulo",
    "regiao": "Sudeste",
    "ibge": "3541406",
    "gia": "5629",
    "ddd": "18",
    "siafi": "6929"
}

# %%
endereco.keys()

# %%
endereco.values()

# %%
endereco.items()

# %%