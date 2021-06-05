# class Mamiferos:
#     def __init__(self, tipo_animal, genero, color, habitat, tipo_alimentacion):
#         self.tipo_animal = tipo_animal
#         self.genero = genero
#         self.color = color
#         self.habitat = habitat
#         self.tipo_alimentacion = tipo_alimentacion


# class Carnivoros(Mamiferos):
#     def __init__(self, tipo_animal, genero, color, tamaño):
#         self.tipo_animal = tipo_animal
#         self.genero = genero
#         self.color = color
#         self.tamaño = tamaño
# carnivoros = Carnivoros("perro", "macho", "cafe", "mediano")
# print(f"los atributos de carnivoros es: {carnivoros.tipo_animal}, {carnivoros.genero}, {carnivoros.color}, {carnivoros.tamaño}")


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
   











