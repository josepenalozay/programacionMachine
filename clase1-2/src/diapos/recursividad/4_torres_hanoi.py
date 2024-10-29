def mostrar_movimientos(origen, destino):
    print('Mover discos desde ' + str(origen) + ' hacia ' + str(destino))

def mover_discos(discos, origen, destino, libre):
    if discos == 1:
        mostrar_movimientos(origen, destino)
    else:
        mover_discos(discos - 1, origen, libre, destino)
        mover_discos(1, origen, destino, libre)
        mover_discos(discos - 1, libre, destino, origen)

print(mover_discos(5, "IZQ", "CENT","DER"))