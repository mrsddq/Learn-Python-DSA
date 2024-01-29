class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data, self.head)
        if self.head is None:
            self.tail = new_node
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

my_list = LinkedList()
my_list.insert(1)
# my_list.insert(2)
# my_list.insert(3)
my_list.print_list()