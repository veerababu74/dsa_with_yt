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
            print("bst is none")
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
            print("best si empty")
            return
        print(self.key,"-->",end="")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.key is None:
            print("best si empty")
            return
        if self.lchild:
            self.lchild.inorder()
        print(self.key,"-->",end="")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.key is None:
            print("best si empty")
            return
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,"-->",end="")

    def delete(self,data,curr):
        if self.key is None:
            print("bst is empty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print("node is not here")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("node is not here")  
        else:
            if self.lchild is None:
                temp=self.rchild
                if data == curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return   
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data ==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return 
                self=None
                return temp
            node= self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self


def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
root =BST(1)

list1=[10,22,45,66,77,33,96,2,5,8]
for i in list1:
    root.insert(i)
# root.serch(77)
print("below is pre order traversal")
root.preorder()

if count(root)>1:
    root.delete(10,root.key)
else:
    print("pakkai velli aduko")

print("after delete preorder")
root.preorder()



        
            
