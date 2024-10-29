#########################
## EXAMPLE: various list operations
## put print(una_lista) at different locations to see how it gets mutated
#########################
una_lista = [2, 1, 3]
otra_lista = [4, 5, 6]
lista_concatenada = una_lista + otra_lista
print("lista_concatenada: ",lista_concatenada)

print("Antes de extend: ", una_lista)
una_lista.extend([0, 6])
print("Despues de extend: ", una_lista)
