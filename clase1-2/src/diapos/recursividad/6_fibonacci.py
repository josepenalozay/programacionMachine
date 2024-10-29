def fibonacci(x):
    """
        asume que x es un  int >= 0
        returns Fibonacci de x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

for numero in range(7):
    print("Fibonacci de " + str(numero) + ": " + str(fibonacci(numero)))