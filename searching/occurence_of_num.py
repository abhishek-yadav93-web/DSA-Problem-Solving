class Created_Arr:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*size
        
    def created(self):
        for i in range(0,len(self.arr),1):
            el=int(input(f'enter the value at {i+1} index in the array: '))
            self.arr[i]=el
    
    def linear_sorting(self):
        for i in range(0,len(self.arr)-1,1):
            smallest=i
            for j in range(i+1,len(self.arr),1):
                if (self.arr[j]<self.arr[smallest]):
                    self.arr[smallest],self.arr[j]=self.arr[j],self.arr[smallest]
        return self.arr
    
    def print_arr(self):
        print('Array is: ',self.arr)
    
        
class Algo:
    def find_occurence(self,arr:list[int],target:int)->int:
        def first_occurence(arr:list[int],target:int)->int:
            start,end=0,len(arr)-1
            mid=0
            pos=-1
            while(start<=end):
                mid=start+(end-start)//2
                if arr[mid]==target:
                    pos=mid
                    end=mid-1
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return pos
        
        def last_occurence(arr:list[int],target:int)->int:
            start,end=0,len(arr)-1
            mid=0
            pos=-1
            while(start<=end):
                mid=start+(end-start)//2
                if arr[mid]==target:
                    pos=mid
                    start=mid+1
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return pos
        
        first=first_occurence(arr,target)
        last=last_occurence(arr,target)
        if (first==-1):
            return 0
        else:
            return last-first+1

def func():
    size=int(input('enter the size of the array: '))
    obj=Created_Arr(size)
    obj.created()
    array=obj.linear_sorting()
    obj.print_arr()
    target=int(input('enter the target those number occurence want to find: '))
    algo=Algo()
    res=algo.find_occurence(array,target)
    print(f'the {target} is found in the array is {res} times ')

func()

