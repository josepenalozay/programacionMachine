def multiplicar_iterativo(factor, otro_factor):
    resultado = 0

    while otro_factor > 0:
        resultado += factor
        otro_factor -= 1

    return resultado

print(multiplicar_iterativo(8, 7))

