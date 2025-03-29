# %%

def soma(a: float, b: float, *args):
    return a + b + sum(args)

def soma_quadratica(a: float, b: float, *args):
    a *= a
    b *= b
    quadrado = []

    for i in args:
        quadrado.append(i*i)

    return a + b + sum(quadrado)


# %%

soma_quadratica(1,2,3,2)

# %%

soma(10, 20,10,2)

# %%

def soma_idades(a,*args):
    idades = [a]
    for i in args:
        idades.append(i["idade"])
    
    return sum(idades)

soma_idades(20,{"idade":23, "nome": "Teo"}, {"idade":45, "nome": "lara"})
# %%

def soma(a, *args, **kwargs):
    return a + sum(args)

idades = [12,43,12,54,65,12,34, 53,65,76]

soma(10, *idades)