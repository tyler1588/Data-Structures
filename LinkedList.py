class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            self.head = node
            self.head.next = currentNode
        self.length += 1
        
    def append(self, value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            currentNode = self.head

            while True:
                if currentNode.next is None:
                    break
            
                currentNode = currentNode.next
            currentNode.next = node
        self.length += 1

    def insert(self, index, value):
        node = Node(value)
        prevNode = self.head

        if (index >= self.length):
            self.append(value)
        
        elif (index < 1):
            self.prepend(value)

        else:
            i = 0
            while (i < index - 1):
                prevNode = prevNode.next
                i += 1
            nextNode = prevNode.next
            prevNode.next = node
            node.next = nextNode
            self.length += 1

    def remove(self, index):
        if (index < 0 or index > self.length - 1):
            print("Index out of range.")

        else:
            prevNode = self.head
            i = 0
            while (i != index - 1):
                prevNode = prevNode.next
                i += 1
            unWantedNode = prevNode.next
            prevNode.next = unWantedNode.next
            self.length -= 1
            
    def printList(self):
        currentNode = self.head
        
        if currentNode is None:
            print("The list is empty!")
        while True:
            if currentNode is None:
                break
            print(currentNode.value)
            currentNode = currentNode.next

        
list = LinkedList()
list.append(5)
list.prepend(10)
list.append(30)
list.append(40)
list.insert(3,140)
list.remove(1)
list.printList()
print(list.length)




        
        

        
