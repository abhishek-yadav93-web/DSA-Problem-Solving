def count_digit(num):
    count=0
    while(num>0):
        count=count+1
        num=num//10
    return count

def armstrong_number(num:int,digit_count:int)->int:
    ans=0
    while(num>0):
        rem=num%10
        ans=ans+pow(rem,digit_count)
        num=num//10
    return ans
        
def main():
    num=int(input('enter the number: '))
    digit_count=count_digit(num)
    ans=armstrong_number(num,digit_count)
    if num==ans:
        print('armstrong number')
    else:
        print('not a armstrong number')