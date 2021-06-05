class Vehiculo():
    def __init__(self, color, ruedas, marca):
        self.color = color
        self.ruedas = ruedas
        self.marca = marca
    
    def __str__(self):
        return "Color {}, ruedas {}, marca {}".format(self.color, self.ruedas, self.marca)
        
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, marca, velocidad, motor):
        super().__init__(color, ruedas, marca)
        self.velocidad = velocidad
        self.motor = motor 
    
    def __str__(self):
        return "velocidad {} km/h, motor {} ".format(self.velocidad, self.motor)


coche = Coche("rojo", "4 ruedas", "chevrolet","60", "4 tiempos")
print(coche)


       


