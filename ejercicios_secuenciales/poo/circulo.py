# GETTERS --> Acceder a un objeto
# SETTERS --> Fijar un objeto, fijar el valor del objeto


class Persona:
    def __init__(self):
        self._edad = 0
    # Metodo Getter
    def get_edad(self):
        return self._edad
    
    # Metodo setter
    def set_edad(self, e):
        self._edad = e

edad_maria = int(input("ingrese edad"))
maria = Persona()
maria.set_edad(edad_maria)

print(maria.get_edad())


    



    







