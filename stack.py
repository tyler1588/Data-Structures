class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek(self):
        if not self.bottom:
            return(None)
        return(print(self.top.value))

    def push(self, value):
        node = Node(value)
        if not self.bottom:
            self.bottom = node
            self.top = self.bottom
            return
        holdingPointer = self.top
        self.top = node
        self.top.prev = holdingPointer

    def pop(self):
        if not self.top:
            return
        if not self.top.prev:
            self.bottom = None
            self.top = None
            return
        holdingPointer = self.top
        self.top = self.top.prev
        

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.pop()
stack.pop()
stack.peek()
        