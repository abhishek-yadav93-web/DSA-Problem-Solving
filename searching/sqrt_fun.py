class Sqrt_of_x:
    def __init__(self,num):
        self.number=num
        
    def find_sqrt(self)->int:# that function have time complexity is O(n) for find the sqrt of the number 
        res=0
        i=1
        while(res<=self.number):
            res=i*i
            i=i+1
        return i-2
    def bineary_approach(self):# in that time complexity is the big O(log(n))
        if self.number<=2:
            return self.number
        start=1
        end=self.number
        mid=0
        ans=0
        while(start<=end):
            mid=start+(end-start)//2
            if mid*mid==self.number:
                ans=mid
                break
            elif mid*mid<self.number:
                ans=mid
                start=mid+1
            else:
                end=mid-1
        return ans
                
            
    def print(self,res:int):
        print(f'square root of {self.number} is {res}')

def func():
    num=int(input('enter the number: '))
    obj=Sqrt_of_x(num)
    res=obj.bineary_approach()
    obj.print(res)

func()
def int_box_control():
    num=int(input('enter the number: '))
    sqre=num*num
    if 2**32<=sqre<=2**32-1:
        print(f'{sqre} have valid and that is less then int type')
    else:
        print(f'{sqre} is not fit in integer type box')