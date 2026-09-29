def decimal_to_binary(num:int)->int:
    ans=0
    pow=1
    while(num>0):
        rem=num%2
        ans=rem*pow+ans
        pow=pow*10
        num=num//2
    return ans

def binary_to_decimal(bin:int)->int:
    ans=0
    pow=1
    while(bin>0):
        rem=bin%10
        ans=ans+rem*pow
        pow=pow*2
        bin=bin//10
    return ans

def taking_number():
    num=int(input('enter the number: '))
    res=decimal_to_binary(num)
    print(f'{num} is the binary number is {res}')
    dec=binary_to_decimal(res)
    print(f'{num} is the decimall formated is {dec}')
    
taking_number()

        