class Stack:
    def __init__(self):
        self.__data = []
    
    def push(self,item):
        self.__data.append(item)
    
    def pop(self):
        if self.isEmpty():
            return -1
        return self.__data.pop()

    def top(self):
        

    