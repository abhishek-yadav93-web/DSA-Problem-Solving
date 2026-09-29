def factorial(num:int)->int:
    if num==0 or num==1 or num==2:
        return num
    ans=1
    while(num>=1):
        ans=ans*num
        num=num-1
    return ans

def func(num:int)->int:
    ans=0
    while(num>4):
        ans=ans+num//5
        num=num//5
    return ans

def main():
    num=int(input("enter the number: "))
    ans=func(num)
    print(f'in factorial of {num} at last after the number zero comes at {ans} times')
    fact=factorial(num)
    print(f'factorial of the {num} is {fact}')
main()