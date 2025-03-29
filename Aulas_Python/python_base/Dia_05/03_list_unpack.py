# %%
a = 10
b = 5
print(a)
print(b)

a,b = b, a

print(a)
print(b)

# %% 

a, *c, b = 1, 2, 3, 4, 4, 5, 6, 7, 98
print(a,b, c)