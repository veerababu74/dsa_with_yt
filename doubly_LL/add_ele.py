class Node:
    def __init__(self,data):
        self.data =data
        self.nref=None
        self.pref=None

class doubly_LL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref

    def print_LL_rev(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end="")
                n=n.pref

    def add_begin (self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node

        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head =new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n

DLL=doubly_LL()

DLL.add_begin(10)

DLL.add_begin(22)

DLL.add_begin(33)

DLL.add_begin(66)

DLL.add_begin(77)
print("++++++++++++++++++++++++++")
DLL.add_end(10000)
DLL.print_LL()

print("\n------------------------")
DLL.print_LL_rev()

             