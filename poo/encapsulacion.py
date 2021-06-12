#ejemplo programación orientada a objetos (permite reutilizar códigos).

class Galleta:
        def __init__(self, sabor, color):               #inicializamos los atributos de la clase. Este es el constructor
                self.sabor = sabor                #inicializa atributo sabor. ESte es el atributo xxx...
                self.color = color


sabor = "amargo"
color = "cafe"
galleta = Galleta(sabor, color)                                     #llamamos la clase, no se le debe pasar valores. A la variable le pasamos el objeto
print(galleta.sabor)

print(galleta.sabor)
print(galleta.color)
print(f"el sabor de la galleta es {galleta.sabor} y el color es {galleta.color}")


if galleta.sabor == "chocolate":
        print("el sabor de la galleta es chocolate")

else:
        print("el sabor de la galleta no es chocolate")





