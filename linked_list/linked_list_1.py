class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head is None:
            print("Linked list empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL1= LinkedList()
LL1.printLL()
