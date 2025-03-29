# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de garrafas de água

opcao = input("Entre com a opcao NATURAL(1), GAS(2), LIMAO(3): ")

valor = 0

if opcao == "1":
    valor = 1.5
elif opcao == "2":
    valor = 2.5
elif opcao == "3":
    valor = 3.0
else:
    print("Entre com uma opcao válida, por favor.")

if valor > 0:
    qtde = int(input("Entre com a quantidade comprada: "))
    valor_final = valor * qtde
    print("Sua conta ficou: R$", valor_final)