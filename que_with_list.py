que =[]

def enque():
    element =input("eneter the elemet to add que : ")
    print(f"you add the this{element} to que")
    que.append(element)
def deque():
    if not que:
        print("que is empty nothing to removve")
    else:
        remove =que.pop(0)
        print(f"this is remove {remove} the element")
def display():
    print(que)
while True:
    user =int(input("select the operation 1.add 2.remove 3.show 4.quit"))
    if user ==1:
        enque()
    elif user ==2:
        deque()
    elif user ==3:
        display()
    elif user==4:
        break
    else:
        print("select corrct operation")