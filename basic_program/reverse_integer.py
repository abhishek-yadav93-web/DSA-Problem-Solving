def reverse_number(num:int)->int:   
    ans=0
    int_min=-2**31
    int_max=2**31-1
    while(num>0):
        ans=10*ans+num%10
        if ans>int_max or ans<int_min:
            return -1
        num=num//10
        print(pow(2,32))
    return ans

def main():
    num=int(input('enter the number: '))
    if num<0:
        new_num=-1*num
        ans=reverse_number(new_num)
        ans=-1*ans
    else:
        ans=reverse_number(num)  
    print(f'{num} reverse number is {ans}')
    
main()
