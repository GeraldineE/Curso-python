#Primer paso
# Crear Nodo
class Nodo:
    def __init__(self, dato):

        # Informacion que pondriamos en el nodo
        self.dato = dato
        #propiedad siguiente, donde guardamos el siguiente nodo
        # Se crea como un nodo vacio, porque aun no se ha conectado con otro
        self.siguiente = None

    def __repr__(self):
        return f'Nodo:|dato:{self.dato}|siguiente->|{self.siguiente}| '

#SEGUNDO PASO
#CREAR LISTAS
class ListaEnlazadaSimple:
    ## Inicializamos la cabeza de la lista como vacio
    ## No tenemos ningun nodo, el primer nodo lo metemos en la cabeza
    def __init__(self):
        self.head = None
    
    def __str__(self):
        return str(self.head)

    def insert(self, Nodo):
        ## Comprobar si la cabeza esta vacia o no
        if self.head:
            ## Asignar el nodo temporal a la cabeza
            temp_nodo = self.head

            while temp_nodo.siguiente: 
                temp_nodo = temp_nodo.siguiente
            ## Asignar el nuevo nodo al puntero del siguiente del
            ## ultimo nodo
            temp_nodo.siguiente = Nodo
        else:
            ## Cabeza esta vacia
			## Asignar nodo a la cabeza
            self.head = Nodo

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.siguiente
    
    def remove_last(self):
        current_node = self.head
        while current_node.siguiente:
            if current_node.siguiente.siguiente:
                break
            else:
                current_node = current_node.siguiente
        current_node.siguiente = None
    def display(self):
        ## Creamos una variable para iterar
        print(self.head)


lista_enlazada_simple = ListaEnlazadaSimple()
lista_enlazada_simple.insert(Nodo(1))
lista_enlazada_simple.insert(Nodo(2))
lista_enlazada_simple.insert(Nodo(3))
lista_enlazada_simple.insert(Nodo(4))
print(lista_enlazada_simple)
lista_enlazada_simple.remove_first()
# lista_enlazada_simple.remove_last()
lista_enlazada_simple.display()

