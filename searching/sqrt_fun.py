class Sqrt_of_x:
    def __init__(self,num):
        self.number=num
        
    def find_sqrt(self)->int:
        res=0
        i=1
        while(res<=self.number):
            res=i*i
            i=i+1
        return i-2
    
    def print(self,res:int):
        print(f'square root of {self.number} is {res}')

def func():
    num=int(input('enter the number: '))
    obj=Sqrt_of_x(num)
    res=obj.find_sqrt()
    obj.print(res)

func()