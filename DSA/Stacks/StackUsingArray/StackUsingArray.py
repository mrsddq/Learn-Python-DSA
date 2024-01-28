class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey Stack is Empty")
        return self.data.pop()

    def top(self):

    def size(self):

    def isEmpty(self):