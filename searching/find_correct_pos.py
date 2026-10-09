class Created:
    def  __init__(self,size):
        self.size=size
        
    def created_array(self):
        arr=[0]*self.size
        for i in range(0,len(arr),1):
            el=int(input(f'enter the ellement at the {i+1} index in the array: '))
            arr[i]=el
        return arr
    
    def print_arr(self,arr):
        print("Array is : ",arr)

class Operation:
    def bubble_sort(self,arr:list[int]):
        for i in range(0,len(arr),1):
            for j in range(0,len(arr)-i-1,1):
                if (arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                print('array is: ',arr)
        
    def find_pos(self,arr:list[int],target:int)->int:
        start,end=0,len(arr)-1
        mid=0
        index=len(arr)
        while(start<=end):
            mid=(start+end)//2
            if (arr[mid]==target):
                index=mid
                return index
            elif(arr[mid]<target):
                start=mid+1
            else:
                index=mid
                end=mid-1
        return index
    
def func():
    size=int(input('enter the size of the array: '))
    obj=Created(size)
    arr=obj.created_array()
    obj.print_arr(arr)
    
    opr=Operation()
    sorted_arr=opr.bubble_sort(arr)
    obj.print_arr(sorted_arr)
    target=int(input('enter the target : '))
    res=opr.find_pos(sorted_arr,target)
    print(f'correct posotion of the {target} in the array is {res}')
    
func()