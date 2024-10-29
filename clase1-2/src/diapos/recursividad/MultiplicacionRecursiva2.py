def multiplicar_recursivo(factor, otro_factor):
    # caso base
    if otro_factor == 1:
        return factor
    # llamada recurrente
    else:
        return factor + multiplicar_recursivo(factor, otro_factor - 1)

print(multiplicar_recursivo(8, 7))