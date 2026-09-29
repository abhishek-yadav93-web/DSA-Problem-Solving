def compliment(num:int)->int:
    ans=0
    i=0
    while(num>0):
        rem=num%2
        if rem==0:
            rem=1
        elif rem==1:
            rem=0
        ans=ans+rem*pow(2,i)
        i=i+1
        num=num//2
    
    return ans 

def main():
    num=int(input('enter the number: '))
    ans=compliment(num)
    print(f'compliment of {num} is {ans}')

main()