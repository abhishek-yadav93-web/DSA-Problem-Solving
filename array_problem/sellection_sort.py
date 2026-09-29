def sellection_sort(arr:list[int]):
    '''that is the algo of sellection sort and that is print the array in the sorted formated there have time complesxity is O(n2)
    that logic is say that find the minimmum ellement position and swap that to the rounded position '''
    
    for i in range(0,len(arr)-1,1):
        minimum=i
        for j in range(i+1,len(arr),1):
            if arr[j]<=arr[minimum]:
                minimum=j
            temp=arr[minimum]
            arr[minimum]=arr[j]
            arr[j]=temp  
    print(f'sorted array is {arr}')


def created_arr():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        ell=int(input("enter the ellement in the array: "))
        arr.append(ell)
    print(arr)
    sellection_sort(arr)