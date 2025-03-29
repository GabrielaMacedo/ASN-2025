# %%
# Faça um programa que receba 4 alturas usando um laço
#  de repetição e realize a soma dessas alturas.

total = 0

for i in range(4):
    # altura = input("Entre com a altura: ")
    # total = total + float(altura)
    total += float(input("Entre com a altura: "))

print(total)

# %%

total = 0
count = 1
while count <= 4:
    # altura = input("Entre com a altura: ")
    # total = total + float(altura)
    print()
    total += float(input("Entre com a altura: "))
    count += 1

print(total)