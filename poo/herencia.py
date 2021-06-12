"""
    Ejemplo de herencia
"""
class Mamiferos:
    def __init__(self, tipo_animal, genero, color, habitat, tipo_alimentacion):
        self.tipo_animal = tipo_animal
        self.genero = genero
        self.color = color
        self.habitat = habitat
        self.tipo_alimentacion = tipo_alimentacion


class Carnivoros(Mamiferos):
    def __init__(self, tipo_animal, genero, color, tamaño):
        self.tipo_animal = tipo_animal
        self.genero = genero
        self.color = color
        self.tamaño = tamaño
carnivoros = Carnivoros("perro", "macho", "cafe", "mediano")
print(f"los atributos de carnivoros es: {carnivoros.tipo_animal}, {carnivoros.genero}, {carnivoros.color}, {carnivoros.tamaño}")

"""
    Ejemplo de herencia multiple.
    la clase terrestre tiene el metodo caminar
    se crea la clase carnivoro y acuatico
    se crea la clase pinguino, la clase pinguino hereda de:
    Terrestre y Acuatico, mientras que la clase perro hereda de terrestre
    La clase pinguino tiene herencia multiple
"""

class Terrestre:
    def caminar(self):
        print("el animal camina")
    
    def carnivoro(self):
        print("el animal es carnivoro")


class Acuatico:
    def nadar(self):
        print("el animal nada")


class Pinguino(Terrestre, Acuatico):
    pass

class Perro(Terrestre):
    pass


perro = Perro()
perro.caminar()

pinguino = Pinguino()
pinguino.caminar()
pinguino.nadar()


"""
    Otro ejemplo de herencia sobre escribiendo los metodos 
"""

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


       












