stack=[]

def add_elemets_to_stack():
    element = input("enter elemet to add it to stack   :  ")
    stack.append(element)
    print(stack)

def remove_elements_to_stack():
    if not stack:
        print("hey stack is empty you cant delete any items")
    else:
        e= stack.pop()
        print("stack removed this element:",e)
        print("after delet the element now stak is",stack)
while True:
    user_input=int(input("select the choise 1.push 2.pop 3 quit :  "))
    if user_input==1:
        add_elemets_to_stack()
    elif user_input==2:
        remove_elements_to_stack()
    elif user_input==3:
        print("termminating th session")
        break
    else:
        print("you are choose wrong option")