'''
step 1 :[5,15,3,12,17,0]
assume 1st value is min

compare 1 st to 2nd (1<2)if its true its min
else compare with other value  total list
if you find min value
then we place samllest value in 0th postion
and comare value to that min positon here we do swap



[0,15,3,12,17,5]

now again start comarision now exclude 0th position


'''


#this work only non duplicate 
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_val=min(arr[i:]) #change max to its work as desending order
        min_index=arr.index(min_val)
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[4,6,9,3,2,8,1,5]
s=selection_sort(arr)
print(s)


#this work for duplicate also

def selection_sort_for_duplicate(arr):
    for i in range(len(arr)):
            min_val=min(arr[i:])
            min_indx=arr.index(min_val,i)
            arr[i],arr[min_indx]=arr[min_indx],arr[i]
    return arr

arr=[4,6,9,3,2,8,1,5,1,4,5,6]
s=selection_sort_for_duplicate(arr)
print(s)
     


#this program using without using min and max

def selection_sort_without_min(arr):
    for i in range (len(arr)):
          m_val =arr[i]
          for j in range(i+1, len(arr)):
               if arr[j]<m_val:
                    m_val=arr[j]
          m_ind=arr.index(m_val,i)
          if arr[i]!=arr[m_ind]:
            arr[i],arr[m_ind]=arr[m_ind],arr[i]
    return arr
arr=[4,6,9,3,2,8,1,5,1,4,5,6]
s=selection_sort_without_min(arr)
print(s)


def selection_sort_without_min_ind(arr):
    for i in range (len(arr)):
          m_ind =i
          for j in range(i+1, len(arr)):
               if arr[j]<arr[m_ind]:
                    m_ind=j
          if arr[i]!=arr[m_ind]:
            arr[i],arr[m_ind]=arr[m_ind],arr[i]
    return arr
arr=[4,6,9,3,2,8,1,5,1,4,5,6]
s=selection_sort_without_min_ind(arr)
print(s)

