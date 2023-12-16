class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class double_LL:
    def __init__(self):
        self.head=None

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
            print("linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end="")
                n=n.pref
    def insert_when_ll_emty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head = new_node
        else:
            print("ll is not empty")
    def add_beging(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
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
    def add_after(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("element not fund")
            else:
                new_node.nref=n.nref
                new_node.pref=n
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("ll is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n=n.nref
            if n is None:
                print("element not fund")
            else:
                new_node.nref=n
                new_node.pref=n.pref
                if n.nref is not None:
                    n.pref.nref=new_node
                n.nref=new_node
    def del_begin(self):
        if self.head is None:
            print("ll is empty")
            return
        if self.head.nref is None:
            self.head =None
            print("dll is only one link now you delete that link also")
        else:
            n=self.head
            self.head=n.nref
            self.head.pref=None
    def del_end(self):
        if self.head is None:
            print("ll is empy")
            return
        if self.head.nref is None:
            self.head=None
        else: 
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    def del_by_val(self,x):
        if self.head is None:
            print("ll si empty")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head=None
            else:
                print("x is not here")
            return
        if self.head.data==x:
            n=self.head
            self.head=n.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data ==x:
                n.pref.nref=None
            else:
                print("we cant found x")



