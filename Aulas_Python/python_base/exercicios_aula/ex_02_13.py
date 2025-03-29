# Faça um programa que receba um número e exiba seu fatorial.

# %%

def fatorial(x):
    resultado = 1
    for i in range(2, x+1):     # 2 * 3 * 4 * 5 ... * x-1 * * x
    # for i in range(x, 1, -1):   x * x-1 * ... * 3 * 2
        print(i)
        resultado *= i

    return resultado, i


numero = int(input("Entre com um numero: "))

fatorial(numero)

# %%