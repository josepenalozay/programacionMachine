def dividir_listas(una_lista, otra_lista):
    resultado = []
    for indice in range(len(una_lista)):
        try:
            resultado.append(una_lista[indice] / otra_lista[indice])
        except ZeroDivisionError:
            resultado.append(float('nan'))  # nan = Not factor Number
        except:
            raise ValueError('Error en dividir las listas')

    return resultado

primera_lista = [0, 1, 2]
segunda_lista = [3, 2, 1]

print(dividir_listas(segunda_lista), primera_lista)
print(dividir_listas(segunda_lista), primera_lista[1:])