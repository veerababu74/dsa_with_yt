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
            return
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

    def serch(self,data):
        if self.key is None:
            print("bst is data")
            return
        if self.key==data:
            print("node is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.serch(data)
            else:
                print("node is not found")
        else:
            if self.rchild:
                self.rchild.serch(data)
            else:
                print("node is not found")
    def preorder(self):
        if self.key is None:
            print("bst is empty")
            return
        print(self.key,"-->",end="")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

root=BST(10)
root=BST(10)
list1=[1,22,45,66,77,33,96,2,5,8]
for i in list1:
    root.insert(i)
root.serch(77)
print("below is pre order traversal")
root.preorder()
       