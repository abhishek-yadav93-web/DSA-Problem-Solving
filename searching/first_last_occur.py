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
    def insertion_sort(self,arr):
        for i in range(1,len(arr),1):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else:
                    break
        return arr
    
    def first_last_occur(self,arr:list[int],target:int)->list:
        first=-1
        second=-1
        start=0
        end=len(arr)-1
        mid=0
        while(start<=end):
            mid=(start+end)//2
            if (arr[mid]==target):
                first=mid
                end=mid-1
            elif (arr[mid]<target):
                start=mid+1
            else:
                end=mid-1
        start,end=0,len(arr)-1
        mid=0
        while(start<=end):
            mid=(start+end)//2
            if(arr[mid]==target):
                second=mid
                start=mid+1
            elif(arr[mid]<target):
                start=mid+1
            else:
                end=mid-1
        print(f'{target} first occurence is {first} and last occurence is {second}')
        arr=[first,second]
        return arr

def func():
    size=int(input('enter the size of the array: '))
    obj=Created(size)
    arr=obj.created_array()
    obj.print_arr(arr)

    target=int(input('enter the target: '))
    opr=Operation()
    sorted_arr=opr.insertion_sort(arr)
    obj.print_arr(sorted_arr)
    res=opr.first_last_occur(sorted_arr,target)
    obj.print_arr(res)

func()


