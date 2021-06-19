# Creamos la clase Stack que significa Pila
class Stack: 
    def __init__(self):
        self.items = []
    
    # Metodo para verificar si la pila esta vacia
    def is_empty(self): 
        return self.items == []
    
    # Metodo para insertar elementos a la pila
    def push(self, item): 
        self.items.insert(0, item)
    
    # Metodo para eliminar el ultimo elemento apilado
    def pop(self): 
        return self.items.pop(0)
    
    # Metodo para mostrar los elementos de la pila
    def print_stack(self): 
        print(self.items)

# Creamos una instancia de la pila
pila = Stack() 
 
# ingresamos elementos a la pila
pila.push('manzanas')
pila.push('uvas')
pila.push('peras')

# Mostramos los elementos de la pila
pila.print_stack() 
# Utilizamos el metodo pop 
pila.pop() 
# Mostramos nuevamente los elementos de la pila
pila.print_stack() 