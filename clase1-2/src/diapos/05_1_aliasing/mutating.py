###############################
## EXAMPLE: mutating factor list while iterating over it
###############################
def remover_duplicados(una_lista, otra_lista):
    for un_elemento in una_lista:
        if un_elemento in otra_lista:
            una_lista.remove(un_elemento)


def remover_duplicados_v2(una_lista, otra_lista):
    copia_una_lista = una_lista[:]
    for un_elemento in copia_una_lista:
        if un_elemento in otra_lista:
            una_lista.remove(un_elemento)


lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 5, 6]
remover_duplicados(lista1, lista2)
print(lista1)

lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 5, 6]
remover_duplicados_v2(lista1, lista2)
print(lista1)