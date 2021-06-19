"""
https://www.instintoprogramador.com.mx/2019/06/lista-doblemente-enlazada-con-ejemplos.html
"""
class Node:  
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.npref = None
    
    def __str__(self):
        return f'{self.item} -> {self.nref}'

class DoublyLinkedList:  
    def __init__(self):
        self.start_node = None
    
    def __str__(self):
        return str(self.start_node)
    
    def insert_in_emptylist(self, data):

        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node
    

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    
    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node
        

    def insert_before_item(self, x, data):
        # si la lista esta vacia
        if self.start_node is None:
            pass
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            # si el elemento no esta en la lista
            if n is None:
                pass
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


    def delete_at_start(self):
        if self.start_node is None:
            pass 
        if self.start_node.nref is None:
            self.start_node = None
            pass
        self.start_node = self.start_node.nref
        self.start_prev = None
    
    def delete_at_end(self):
        #Si no hay elementos a eliminar
        if self.start_node is None:
            pass 
        if self.start_node.nref is None:
            self.start_node = None
            pass
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
            

new_linked_list = DoublyLinkedList() 
new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(5)  
new_linked_list.insert_at_start(9)
new_linked_list.insert_at_end(39)  
new_linked_list.insert_at_end(59)
new_linked_list.insert_after_item(50, 65)
new_linked_list.insert_after_item(39, 8)  
new_linked_list.insert_before_item(59, 100)
new_linked_list.delete_at_start()
new_linked_list.delete_at_end()  
print(new_linked_list)