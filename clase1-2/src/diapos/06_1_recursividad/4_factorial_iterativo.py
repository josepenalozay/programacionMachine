# discos! = discos*(discos-1)*(discos-2)*(discos-3)* ... * 1
def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

print (factorial_iterativo(4))
print (factorial_recursivo(4))