class Pila:
    def __init__(self):
        self.items = []

    def pila_esta_vacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamanio(self):
        return len(self.items)

p = Pila()
print("Lista esta vacia? ", p.pila_esta_vacia())
p.incluir('perro')
print("Elemento agregado: ", p.inspeccionar())
print("tamaño: ", p.tamanio())
print(p.pila_esta_vacia())
p.incluir(9)
print("Elemento agregado: ", p.inspeccionar())
print("tamaño: ", p.tamanio())
print("El elemento que se extrajo: ", p.extraer())
print("El nuevo tamaño:", p.tamanio())



# m = Pila()
# m.incluir('x')
# m.incluir('y')
# m.extraer()
# m.incluir('z')
# m.inspeccionar()

# m = Pila()
# m.incluir('x')
# m.incluir('y')
# m.incluir('z')
# while not m.estaVacia():
#    m.extraer()
#    m.extraer()