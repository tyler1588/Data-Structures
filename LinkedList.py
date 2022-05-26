class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

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
    
  def printList(self):
    currentNode = self.head
    if not currentNode:
      print("The list is empty!")
      
    while True:
      if currentNode is None:
        break
      print(currentNode.value)
      currentNode = currentNode.next

list = LinkedList()
list.append(10)
list.append(5)
list.append(16)
list.append(20)
list.printList()
  

