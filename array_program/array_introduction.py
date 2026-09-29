# decleared one data type of list those are store the single data type value by the user
# be default in python when we takes the input then that is changed in striing data type 
class array_dec:
    def __init__(self,size):
        self.size=size
        self.arr=[0]*size
    
    def set_data(self,index,value):
        if type(value) is not int:
            raise TypeError("please enter the integer value")
        self.arr[index]=value
    
    def get_data(self,index):
        return self.arr[index]
    
def main():
    size=int(input('enter the size of the array: '))
    arr=array_dec(size)
    for i in range(0,size,1):
        el=int(input("enter the value: "))
        arr.set_data(i,el)
    print(arr.arr)

main()