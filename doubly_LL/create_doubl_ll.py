class  Node:
    def __init__(self,data):
        self.data =data
        self.nref=None
        self.pref=None


class double_LL:
    def __init__(self):
        self.head =None

    
    def print_LL(self):
        if self.head == None:
            print("doubly linked list is empty")

        else:
            n=self.head
            while n is not None:
                print(n.data ,"-->",end="")
                n=n.nref

    def print_LL_rev(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data ,"-->",end="")
                n=n.pref