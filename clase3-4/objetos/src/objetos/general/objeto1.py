class Coordenada(object):

    def __init__(self, x, y=1):
        self.x = x
        self.y = y

una_coordenada = Coordenada(3, 4)
coordenada_origen = Coordenada(0, 6)
coordenada_origen2 = Coordenada(0)

print("una_coordenada.x=", una_coordenada.x)
print("una_coordenada.y=", una_coordenada.y)
print("coordenada_origen .x=", coordenada_origen.x)