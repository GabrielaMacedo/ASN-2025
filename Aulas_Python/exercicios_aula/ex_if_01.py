# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

opcao = input("Entre com a opcao NATURAL(1) ou GAS(2): ")

if opcao == "1":
    print("Sua conta deu: R$1,50")
elif opcao == "2":
    print("Sua conta deu: R$2,50")
else:
    print("Entre com uma opcao válida, por favor.")