class Persona():
    def __init__(self):
        self.cedula = 13765890
    def mensaje(self):
        print("mensaje desde la clase Persona")
class Obrero(Persona):
    def __init__(self):
        self.__especialista = 1
    def mensaje(self):
        print("mensaje desde la clase Obrero")
obrero_planta = Obrero()
obrero_planta.mensaje()



class Animal:
    def ladrar(self):
        pass

class Perro(Animal):
    def ladrar(self):
        print("Guau!")

class Gato(Animal):
    def ladrar(self):
        print("Miau!")

for animal in Perro(), Gato():
    animal.ladrar()