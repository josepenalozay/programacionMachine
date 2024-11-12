# Pets polymorphism
# Three classes, all with myanimal different "speak" method

class Perro():
    def __init__(self, name):
        self.name = name

    def comunicarse(self):
        print(self.name, 'dice guauu, guauuu, guauuu!')


class Gato():
    def __init__(self, name):
        self.name = name

    def comunicarse(self):
        print(self.name, 'dice meeeoooow')


class Ave():
    def __init__(self, name):
        self.name = name

    def comunicarse(self):
        print(self.name, 'dice tweet')


oPerro1 = Perro('Rover')
oPerro2 = Perro('Fido')
oGato1 = Gato('Fluffy')
oGato2 = Gato('Spike')
oAve = Ave('Big Ave')

petsList = [oPerro1, oPerro2, oGato1, oGato2, oAve]

# Send the same message (call the same method) of all pets
for oPet in petsList:
    oPet.comunicarse()
