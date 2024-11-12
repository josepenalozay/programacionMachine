class Auto:
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

# Clase Ejecuta simulada en Python
if __name__ == "__main__":
    a_normal = Auto(0, "clasico", "morado")
    a_deportivo = Auto(1, "deportivo", "verde")
    a_de_lujo = Auto(2, "lujoso", "azul")

    print(f"id: {a_normal.get_id()} modelo: {a_normal.get_modelo()} color: {a_normal.get_color()}")
    print(f"id: {a_deportivo.get_id()} modelo: {a_deportivo.get_modelo()} color: {a_deportivo.get_color()}")
    print(f"id: {a_de_lujo.get_id()} modelo: {a_de_lujo.get_modelo()} color: {a_de_lujo.get_color()}")