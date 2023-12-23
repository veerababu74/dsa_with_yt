class BST:
    def __init__(self,key):
        self.key=key
        self.rchild=None
        self.lchild=None


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

    def  serch(self,data):
        if self.key is None:
            print('bst is empty')
            return
        if self.key==data:
             print(data,"node is found")
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
            print('bst is empty')
            return
        print(self.key,"-->",end="")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def delete(self,data):
        if self.key is None:
            print('bst is empty')
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("node is not found")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("node is not found")
        else:
            if self.lchild is None:
                temp =self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(data)
        return self
    def delete1(self,data,curr):
        if self.key is None:
            print("bst is empty")
            return
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete1(data,curr)
            else:
                print("node is not here")
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete1(data,curr)
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
            self.rchild=self.rchild.delete1(node.key,curr)
        return self

    def min_node(self):
        if self.key is None:
            print("bst is empty")
            return
        current=self
        while current.lchild:
            current=current.lchild
        print("min node",current.key)

    def max_node(self):
        if self.key is None:
            print("bst is empty")
            return
        current=self
        while current.rchild:
            current=current.rchild
        print("max node",current.key)




            
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
    root.delete1(10,root.key)
else:
    print("pakkai velli aduko")

print("after delete preorder")
root.preorder()

root.max_node()
root.min_node()