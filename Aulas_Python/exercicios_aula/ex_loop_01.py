# %%
# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
palavra = input("Entre com uma palavra: ")

qtde_as = 0

for letra in palavra:
    if letra == "a":
        qtde_as += 1

print(qtde_as)

# %%

palavra = input("Entre com uma palavra: ")

qtde_as = palavra.count("a")
print(qtde_as)