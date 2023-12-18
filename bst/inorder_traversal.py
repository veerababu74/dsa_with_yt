class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None


    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
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
            print("bst is empty")
            return
        if self.key==data:
            print("node is found")
            return
        if self.key>data:
            if self.lchild:
                self.lchild.serch(data)
            else:
                print("node not prasent in l chiled")
        else:
            if self.rchild:
                self.rchild.serch(data)
            else:
                print("node not prasent in r child")

    def preorder(self):
        if self.key is None:
            print("bst is empt")
            return
        print(self.key,"-->",end="")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.key is None:
            print("bst is empt")
            return
        if self.lchild:
            self.lchild.inorder()
        print(self.key,"-->",end="")
        if self.rchild:
            self.rchild.inorder()


    def postorder(self):
        if self.key is None:
            print("bst is empty")
            return
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,"-->",end="")


root=BST(None)

list1=[1,22,45,66,77,33,96,2,5,8]
for i in list1:
    root.insert(i)
root.serch(77)
print("below is pre order traversal")
root.preorder()
print("\nbelow is in order traversal")
root.inorder()
print("\nbelow is post order traversal")
root.postorder()