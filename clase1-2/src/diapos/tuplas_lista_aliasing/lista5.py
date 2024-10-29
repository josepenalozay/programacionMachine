una_lista = [2, 1, 3, 6, 3, 7, 0]
una_lista.remove(2)
print("una_lista: ", una_lista)

una_lista.remove(3)
print("una_lista: ", una_lista)

del(una_lista[1])
print("una_lista: ", una_lista)

ultimo_elemento = una_lista.pop()
print("ultimo_elemento: ",ultimo_elemento)
print("una_lista: ",una_lista)