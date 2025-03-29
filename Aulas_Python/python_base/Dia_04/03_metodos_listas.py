# %%

idades = [32, 45, 32, 56, 21, 24, 26, 34, 27, 18, 19]

print(idades)

# %%
idades.append(55)
print(idades)

# %%
idades.append(34)
idades

# %%
idades.append([23, 36])
print(idades)

# %%
idades.remove([23, 36])
print(idades)

# %%
idades.extend([23, 36])
print(idades)

# %%
idades

# %%

del idades

# %%


A = [1,2,3]
B = A[:]

print("A:",A)
print("B:",B)

B.append(4)
print("A:",A)
print("B:",B)