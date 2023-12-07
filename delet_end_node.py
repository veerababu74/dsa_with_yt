class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None

    
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.ref

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
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref

        if n is None:
            print("node is not here")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref =new_node
    def add_before(self,data,x):
        n=self.head
        if n is None:
            print("linked list is empty")
            return
        
        if n.data == x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head =new_node

        n=n.data
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n=n.ref
        if n is None:
            print("node not found")
        else:
            new_node=Node(data)
            new_node.ref =n.ref
            n.ref=new_node

    def add_ele_when_ll_empt(self,data):
        if self.head is None:
            print("ll is empty")
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("nothing to delete bcz ll is empty")
        else:
            n=self.head
            self.head=n.ref
    def delete_end(self):
        if self.head is None:
            print("nothing to delete ll is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref =None            
