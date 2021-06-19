"""
Node: https://files.realpython.com/media/Group_12_2.0ded5fffe97a.png
Linked List: https://files.realpython.com/media/Group_14.27f7c4c6ec02.png

En el mundo real se usan para implementar
Colas, Pilas y Grafos.

Colas: First In/First Output (FIFO)
Pilas: Last Input/First Output (LIFO)
Grafo: Direct Acyclic Graph (DAG)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'

class SimpleLinkedList:
    def __init__(self):
        self.first = None

    def __str__(self):
        return str(self.first)

    def insert_first(self, node):
        self.first, node.next = node, self.first

    def insert_last(self, node):
        if not self.first:
            self.first = node

            return

        current_node = self.first

        while current_node.next:
            current_node = current_node.next

        current_node.next = node

    def remove_first(self):
        if not self.first:
            return
        self.first = self.first.next

    def remove_last(self):
        current_node = self.first

        while current_node.next:
            if current_node.next.next:
                break
            else:
                current_node = current_node.next
        
        current_node.next = None


simple_linked_list = SimpleLinkedList()
simple_linked_list.insert_last(Node(1))
simple_linked_list.insert_last(Node(2))
simple_linked_list.insert_first(Node(3))
print(simple_linked_list)
simple_linked_list.remove_first()
# simple_linked_list.remove_last()
print(simple_linked_list)

