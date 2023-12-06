class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("hey linked list isempty")
        else:
            n=self.head
            while n is not None:
                print(n.data ,end="")
                print("-->",end="")
                n=n.ref
                # print("\n this is cheacking,",n)

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node


    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
                # print("serching for  n.ref" ,n)
            n.ref =new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data ==x:
               break
            n=n.ref
        if n is None:
            print(f"element you given {x} is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data ==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n=n.ref
        if n.ref is None:
            print("element is not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref =new_node


LL1=LinkedList()
LL1.add_begin(10)
LL1.add_begin(30)
LL1.add_begin(60)
LL1.add_end(50)
LL1.add_after(100,20)
LL1.add_after(1000,1000)
LL1.add_before("HI",50)
LL1.print_LL()
        


    
    
