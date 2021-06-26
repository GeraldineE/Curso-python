class Stack:
    def __init__(self):
        self.elemento = [] #definir el elemento como algo vacio
    
    def elemento_vacio(self):
        return self.elemento == []
    
    def insertar_elemento(self, elemento):
        self.elemento.append(elemento)
            
    def remover_elemento(self):
        self.elemento.pop()
            
    def recorrer(self):
        return self.elemento

stack = Stack()

stack.elemento_vacio

stack.insertar_elemento('Primer elemento')
print(stack.recorrer())
stack.insertar_elemento('Segundo elemento')
print(stack.recorrer())




#################


# contruir una pila

class Pila:
    def __init__(self):
        self.elemento=[] ##definir el elemento como algo vacio
    def elemento_vacio(self):
        return self.elemento == [] ##devolver un boleano
    def apilar(self,elemento):
        self.elemento.append(elemento)
    def remover(self): 
        self.elemento.pop() 
    def devolver(self): 
        print(self.elemento)

    
pila = Pila()
pila.elemento_vacio()
pila.apilar(1)
pila.apilar(2)
pila.devolver()