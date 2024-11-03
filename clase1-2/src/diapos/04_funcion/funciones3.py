def func_a():
    print('Ejecutando func_a')

def func_b(y):
    print('Ejecutando func_b')
    return y

def func_c(z):
    print('Ejecutando func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))