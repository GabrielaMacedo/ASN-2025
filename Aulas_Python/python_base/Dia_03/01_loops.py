# %%

inicio = int(input()) # pede para usuário o valor de inicio
fim = int(input())    # pede para usuário o valor de fim

while inicio <= fim:
    if inicio % 2 == 0:
        print(inicio, "é par")
    inicio += 1