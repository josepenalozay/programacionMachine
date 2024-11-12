class Coordenada(object):
    """ A Coordenada made up of an x and y value """
    def __init__(self, x, y):
        """ Sets the x and y values """
        self.x = x
        self.y = y

    def calcular_distancia(self, otra_coordenada):
        """ Returns the euclidean calcular_distancia between two points """
        diferencia_x = (self.x - otra_coordenada.x) ** 2
        diferencia_y = (self.y - otra_coordenada.y) ** 2
        return (diferencia_x + diferencia_y)**0.5


una_coordenada = Coordenada(3, 4)
print(una_coordenada)