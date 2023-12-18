class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:
            return #this is for not allowing duplicates
        
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)


                
    def insert_dup(self,data):
        if self.key is None:
            self.key=data
            return
        #this is for allowing duplicates
        if self.key>=data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
            return
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

root=BST(10)
list1=[1,22,45,66,77,33,96,2,5,8]
for i in list1:
    root.insert(i)

