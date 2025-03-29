# %%

# f(x ; mu, sigma) = (1 / (sqrt(2*pi) * sigma)) * exp( (-1 / 2) * ((x - mu) / sigma)**2 )
# mu -> média populacional
# sigma -> variância populacional
# x -> variável

# %%

# f(x) = x ** 2

def f_quadrado(x):
    return x ** 2

# %%
f_quadrado(100)

# %%

def normal(x, mu=0, sigma=1):
    resultado = (1 / ( (2 * 3.1415 * (sigma ** 2))**0.5)) * (2.71 ** ( (-1 / 2) * ((x - mu) / sigma)**2 ))
    return resultado

# %%

print(normal(1))
print(normal(1, 10 ,1))

# %%

def eh_par(x: int):
    """
    eh_par: função para exibir se um número é par ou ímpar.

    x: um número inteiro

    Essa funçao não retorna nada!
    """
    if x % 2 == 0:
        print(x, "é par!")
    else:
        print(x, "é impar!")


# %%

eh_par(4)
eh_par(7)
eh_par(10)
eh_par("dois")

# %%

y = normal(0)
print(y)

# %%

y = eh_par(6)
print(y)

# %%

z = print("ola mundo!")
print(z)