# %%

# 04.01 - Quantos clientes tem vínculo com a Twitch?
import pandas as pd
# Caminho absoluto com prefixo "r" (raw string)
file_path = r"C:\Users\g_mac\OneDrive\Documentos\00_Projetos_Compartilhados\02_ASN_Rocks\ASN-2025\Aulas_Python\pandas_base\data\clientes.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, delimiter=";")
# df = pd.read_csv("C:\Users\g_mac\OneDrive\Documentos\00_Projetos_Compartilhados\02_ASN_Rocks\ASN-2025\Aulas_Python\pandas_base\data\clientes.csv", delimiter=";")
df.head()

# Maneira 01
df[df['flTwitch']==1].shape[0]

# Maneira 02
(df['flTwitch']==1).sum()

# %%
# 04.02 - Quantos clientes tem um saldo de
#  pontos maior que 1000?

# Maneira 01
df[df["qtdePontos"] > 1000].shape[0]

# Maneira 02
(df["qtdePontos"] > 1000).sum()


# Quem sao esses clientes?
df[df["qtdePontos"] > 1000]["idCliente"]

# %%

# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

file_path = r"C:\Users\g_mac\OneDrive\Documentos\00_Projetos_Compartilhados\02_ASN_Rocks\ASN-2025\Aulas_Python\pandas_base\data\transacoes.csv"

# Carregar o arquivo CSV
df_transacao = pd.read_csv(file_path, delimiter=";")


df_transacao.head(2)

piso = df_transacao["dtCriacao"] >= '2025-02-01'
teto = df_transacao["dtCriacao"] < '2025-02-02'
filtro = piso & teto
df_transacao[filtro].shape[0]

# %%

(pd.to_datetime(df_transacao["dtCriacao"]).dt.date.astype(str) == "2025-02-01").sum()

# %%
