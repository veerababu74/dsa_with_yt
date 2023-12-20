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
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)

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
                print("node is not prasent here")
        else:
            if self.rchild:
                self.rchild.serch(data)
            else:
                print("node is not prasent here")

    def preorder(self):
        if self.key is None:
            print("bst is empty")
            return
        print(self.key,"-->",end="")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.key is None:
            print("bst is empty")
            return
        if self.lchild:
            self.lchild.preorder()
        print(self.key,"-->",end="")
        if self.rchild:
            self.rchild.preorder()
    def postorder(self):
 
        if self.key is None:
            print("bst is empty")
            return
       
        if self.lchild:
            self.lchild.preorder()
       
        if self.rchild:
            self.rchild.preorder()
        print(self.key,"-->",end="")

    def delete(self,data):
        if self.key is None:
            print("bst is emoty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("given node is not here")
        elif self.key<data:
            if self.rchild:
                self.lchild=self.rchild.delete(data)
            else:
                print("given node is not here")
      #for batter understand watch this https://www.youtube.com/watch?v=kDbqMBgVr9s&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=48
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=temp
                return self
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self
    


root=BST(10)

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


print("delete one item 10 ")
root.delete(10)

root.preorder()
