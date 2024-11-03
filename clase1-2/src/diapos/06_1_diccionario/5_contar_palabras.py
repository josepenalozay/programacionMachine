def contar_palabras(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias

cancion = """
si ellos están mintiendo, por favor defiéndete
yo sé que no lo harás, pues dicen la verdad
es una pena siempre seguirás doliéndome
y culpable o no
¿qué le puedo hacer ya?
miénteme como siempre
por favor miénteme
necesito creerte
convénceme
miénteme con un beso
que parezca de amor
necesito quererte
culpable o no
"""

diccionario_frecuencias = contar_palabras(cancion.split())
print(diccionario_frecuencias)

'''


def palabra_mas_comun(frecuencia_por_palabra):
    frecuencias = frecuencia_por_palabra.values()
    maxima_frecuencia = max(frecuencias)
    palabras_comunes = []
    for palabra in frecuencia_por_palabra:
        if frecuencia_por_palabra[palabra] == maxima_frecuencia:
            palabras_comunes.append(palabra)

    return (palabras_comunes, maxima_frecuencia)

palabras_comunes = palabra_mas_comun(diccionario_frecuencias)
print(palabras_comunes)


def palabras_por_frecuencia(frecuencia_por_palabra, frecuencia_minima):
    resultado = []
    terminado = False
    while not terminado:
        palabra_frecuencia = palabra_mas_comun(frecuencia_por_palabra)
        if palabra_frecuencia[1] >= frecuencia_minima:
            resultado.append(palabra_frecuencia)
            for palabra in palabra_frecuencia[0]:
                del(frecuencia_por_palabra[palabra])
        else:
            terminado = True
    return resultado

al_menos_dos_veces = palabras_por_frecuencia(diccionario_frecuencias, 2)
print()
'''


