def bublle_sort(arr:list[int])->list:
    for i in range(0,len(arr)-1,1):
        for j in range(0,len(arr)-i-1,1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def bublle_sort_decreassing_order(arr:list[int])->list:
    for i in range(0,len(arr)-1,1):
        for j in range(0,len(arr)-i-1,1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def bublle_sort_att_last_index(arr:list[int])->list:
    for i in range(len(arr)-1,0,-1):
        for j in range(len(arr)-1,len(arr)-i-1,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr
def created_arr():
    size=int(input("enter the size of the array: "))
    arr=[]
    for i in range(0,size,1):
        ell=int(input("enter the ellement in the array: "))
        arr.append(ell)
    print(arr)
    res=bublle_sort_att_last_index(arr)
    print(f"result is {res}")
    
    # new_arr=bublle_sort(arr)
    # print(f"sorted array is {new_arr}")
    # decreassing_order=bublle_sort_decreassing_order(arr)
    # print(f"array in the decreassing order: {decreassing_order}")

created_arr()     

