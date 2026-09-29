from array_creation import creating_func,print_func
def func(array:list[int]):
    start=0
    end=len(array)-1
    while(start<end):
        if(array[start]==0):
            temp=array[start]
            array[start]=array[end]
            array[end]=temp
            end-=1
        start +=1
    return array

array=creating_func()
new_array=func(array)
print_func(new_array)