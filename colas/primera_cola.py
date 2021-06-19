class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0,item)
        return item

    def desencolar(self):
        return self.items.pop()

    def tamanio(self):
        return len(self.items)

queue = Cola()
print(queue.estaVacia())
print(queue.tamanio())
print(queue.encolar("primero entre yo"))
print(queue.encolar("segundo entre yo"))
print(queue.encolar("tercerentre yo "))
print(queue.encolar("---- yo entre de ultimo ----"))
print("¿quien sale primero?")
print(queue.desencolar())
print(queue.estaVacia())
