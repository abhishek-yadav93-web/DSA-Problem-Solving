def arra_created():
    size=int(input('enter the size of the array: '))
    arr=[0]*size
    for i in range(0,len(arr),1):
        el=int(input('enter the value in the array: '))
        arr[i]=el
    print('array is ',arr)
    return arr

def roated_first_appraoch(arr:list[int])->list:# in that program the time complexity is the O(n) but the space complexity is O(n)
    size=len(arr)
    new_arr=[0]*size 
    i,j=0,1
    while(i<len(arr)-1):
        new_arr[j]=arr[i]
        i+=1
        j+=1
    
    new_arr[0]=arr[len(arr)-1]
    for i in range(0,len(arr),1):
        arr[i]=new_arr[i]
    print('rotted array is ',arr)

def ratoated_second_appraoch(arr:list[int],k): # in that program the time 
    if len(arr)<=1:
        print('roated array is ',arr)
        return
    times=1
    while(times<=k):
        temp=arr[len(arr)-1]
        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
        times+=1
    print('rotated array is ',arr)
    
arr=arra_created()
print(arr)
ratoated_second_appraoch(arr)
# roated_first_appraoch(arr)
# print(arr)