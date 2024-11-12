class Coordenada(object):
    """ A Coordenada made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns myanimal string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def calcular_distancia(self, otra_coordenada):
        """ Returns the euclidean calcular_distancia between two points """
        diferencia_x = (self.x - otra_coordenada.x) ** 2
        diferencia_y = (self.y - otra_coordenada.y) ** 2
        return (diferencia_x + diferencia_y)**0.5


una_coordenada = Coordenada(3, 4)
coordenada_origen = Coordenada(0, 0)

print(una_coordenada.calcular_distancia(coordenada_origen))
print(Coordenada.calcular_distancia(una_coordenada, coordenada_origen))

#print(una_coordenada.x, coordenada_origen.x)
#print(coordenada_origen.calcular_distancia(una_coordenada))
#print(una_coordenada)