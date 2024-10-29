def es_numero_par(numero):
    """
    Input: numero, factor positive int
    Returns True if numero is even, otherwise False
    """
    print('Evaluando ', numero)
    resto = numero % 2
    return resto == 0

resultado = es_numero_par(3)
print(resultado)