class Auto(object):

    def __init__(self, id, modelo, color):
        self.id = id
        self.modelo = modelo
        self.color = color


def get_id(self):
    return self.id


def get_modelo(self):
    return self.modelo


def get_color(self):
    return self.color
# Ejemplo de uso
auto = Auto(1, "ModeloX", "Rojo")
print(auto.get_id())  # Imprime: 1
print(auto.get_modelo())  # Imprime: ModeloX
print(auto.get_color())  # Imprime: Rojo
