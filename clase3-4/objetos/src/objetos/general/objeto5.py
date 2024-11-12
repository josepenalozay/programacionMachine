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

mi_instancia = Coordenada(3, 4)

print("mi_instancia=", mi_instancia)
print("type(mi_instancia)=", type(mi_instancia))
print("Coordenada=", Coordenada)

print("isinstance(mi_instancia, Coordenada)=",
isinstance(mi_instancia, Coordenada))