class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref


    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref =self.head
        self.head=new_node


    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref

            n.ref =new_node

    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.ref
        if n is None:
            print("node not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        n=self.head
        if n is None:
            print("ll is empty")
            return
        if n.data==x:
            new_node=Node(data)
            new_node.ref =self.head
            self.head=new_node
            return
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("node no here")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def del_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            self.head=n.ref
    def del_end(self):
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def del_by_ele(self,x):
        if self.head is None:
            print("linked list is empty")
        if self.head.data ==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("no element here you give")
        else:
            n.ref=n.ref.ref


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(30)
LL1.add_begin(60)
LL1.add_end(50)
LL1.add_after(100,20)
LL1.add_after(1000,1000)
LL1.add_before("HI",50)

LL1.add_begin("v")
LL1.add_begin("p")
# LL1.del_begin()
# LL1.del_end()
LL1.del_by_ele("HI")
LL1.del_by_ele("HI")
LL1.print_LL()
            


