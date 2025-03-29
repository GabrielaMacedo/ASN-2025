# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

tipos = "Qual tipo você quer? CASQUINHA(1) | CASCAO(2) | CESTINHA(3): "
tipo = input(tipos)

valor = 0
if tipo == "1":
    valor = valor + 1.00
elif tipo == "2":
    valor += 2.5
elif tipo == "3":
    valor += 4.00

sabor = input("Ente com um sabor: MORANGO(1) | CREME(2) | CHOCOLATE(3): ")

cobertura = input("Entre com a cobertura: CARAMELO(1) | MORANGO(2) | CHOCOLATE(3) | SEM COBERTURA(4): ")

if cobertura in ("1", "2", "3"):
    valor += 1.5
elif cobertura == "4":
    valor += 0

print("Valor total:", valor)