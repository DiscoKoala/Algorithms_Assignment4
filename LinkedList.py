class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def showData(self):
        print(self.data)

class LinkedList:
    def __init__(self, data):
        self.head = None

    def list_empty(self):
        return not self.head

    def add_front(self, node):
        node.next = self.head
        self.previous = self.head
        self.head = node

    def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data)
         printval = printval.next
