import numpy as np
#this not work for the duplicated values
def linera_serch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            break
        else:
            return f'{key} :element not found'
    return f'{key} is found'

#this work for duplicated values
def linera_serch_with_duplicate(arr,key):
    found=False
    list2=[]
    for i in range(len(arr)):
        if key== arr[i]:
            found=True
            list2.append(arr[i])
    if found:
        for i in list2:
            print(i)
    else:
        print("not founded")


arr=np.arange(1,20,5)
print(arr)
print(linera_serch(arr,6))
list3=[1,2,4,3,65,10,2,10,12,4,6,8,0,75,10]
linera_serch_with_duplicate(list3,10)