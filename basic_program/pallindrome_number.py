def pallindrome_number(num:int)->bool:
    if num<0:
        return False
    old_num=num
    ans=0
    while(old_num):
        ans=10*ans+old_num%10
        old_num=old_num//10
        
    if ans!=num:
        return False
    return True

def main():
    num=int(input('enter the number: '))
    ans=pallindrome_number(num)
    if ans:
        print(f'{num} pallindrome number ')
    else:
        print(f'{num} is not pallindrome number')

main()