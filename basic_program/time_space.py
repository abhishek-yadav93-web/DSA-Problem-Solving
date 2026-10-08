class array_dec:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*size
        
    def create_arr(self):
        size=len(self.arr)
        for i in range(0,size,1):
            el=int(input(f'enter the ellement at {i+1} index'))
            self.arr[i]=el
        return self.arr
    
    def print_arr(self,arr):
        print("array: ",arr)
        
    
class sorting:
    def  linear_sorting(self,arr:list[int]):# time complexity is O(n2) in both condition 
        for i in range(0,len(arr)-1,1):
            greates=i
            for j in range(i+1,len(arr),1):
                if arr[j]<arr[greates]:
                    arr[greates],arr[j]=arr[j],arr[greates]
        return arr
    
    def bubble_sort(self,arr:list[int]):
        for i in range(0,len(arr),1):
            for j in range(0,len(arr)-i-1,1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
    def insertion_sort(self,arr:list[int]):
        for i in range(1,len(arr),1):
            for j in range(i,0,-1):
                if arr[j-1]>arr[j]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
                else:
                    break
        return arr
    
size=int(input('enter the size of the array: '))
obj=array_dec(size)
arr=obj.create_arr()
obj.print_arr(arr)
algo=sorting()
# new_arr=algo.linear_sorting(arr)
# obj.print_arr(new_arr)
# new_arr=algo.bubble_sort(arr)
# obj.print_arr(new_arr)
new_arr=algo.insertion_sort(arr)
obj.print_arr(new_arr)

    