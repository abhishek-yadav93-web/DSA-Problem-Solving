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

class Searching:
    def linear_search(self,arr:list[int],num:int)->bool:# that is work every time array is sorted or not
        for i in range(0,len(arr),1):
            if arr[i]==num:
                return True
        return False
def func():
    size=int(input(f'enter the size of the array: '))
    obj=Created(size)
    arr=obj.created_array()
    obj.print_arr(arr)
    num=int(input('enter the number those you want to find: '))
    sear=Searching()
    res=sear.linear_search(arr,num)
    if res:
        print(f'{num} is found in the array')
    else:
        print(f'{num} is not found in the array')

func()



        