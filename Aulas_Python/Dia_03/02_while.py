# %%

inicio = 1
fim = 1000

while inicio <= fim:

    if inicio == 11:
        inicio += 1
        continue

    if inicio % 11 == 0:
        break

    if inicio == 8:
        inicio += 1
        continue

    if inicio % 2 == 0:
        print(inicio, "é par!")

    inicio += 1