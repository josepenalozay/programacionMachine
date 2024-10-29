def multiplicacion(a, b):
    # caso base
    if b == 1:
        return a
    # llamada recurrente
    else:
        return a + multiplicacion(a, b - 1)

print(multiplicacion(8,7))