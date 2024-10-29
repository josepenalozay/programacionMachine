# discos! = discos*(discos-1)*(discos-2)*(discos-3)* ... * 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print (factorial(4))
