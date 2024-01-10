def binaryserch(arr,key):

    found=False
    low=0
    high=len(arr)-1
    while low <= high and not found:
        mid=(low+high)//2
        if key == mid:
            found = True
        elif key>arr[mid]:
            low=mid+1
        elif key<arr[mid]:
            high=mid-1
    if found == True:
        print(f"{key } founded")
    else:
        print("not found")

list1=[1,4,6,8,3,66,7,9,0,33,2,5,8]
list1.sort()
binaryserch(list1,9)    
