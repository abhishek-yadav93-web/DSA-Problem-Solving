def digit_sum(num:int)->int:
    ans=0
    while(num>0):
        ans=ans+num%10
        num=num//10
    print(f'digit sum is {ans}')

def single_digit(num:int)->int:
    while(num>9):
        ans=0
        while(num>0):
            ans=ans+num%10
            num=num//10
        num=ans
    print(f'single digit {num}')

def main():
    num=int(input("enter the number: "))
    digit_sum(num)
    single_digit(num)

main()