class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node:[ {self.data} : {self.next} ]'


class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head:
            temp_node = self.head

            while temp_node.next:
                temp_node = temp_node.next

            temp_node.next = node
        else:
            self.head = node

    def display(self):
        print(self.head)


simple_linked_list = SimpleLinkedList()
simple_linked_list.insert(Node(1))
simple_linked_list.insert(Node(2))
simple_linked_list.display()