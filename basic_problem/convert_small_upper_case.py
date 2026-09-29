def converter(val:str)->str:
    '''ord() method that return the ASCII value of the character and chr() that return the Character of the ASCI value so that is not build in method '''
    print(ord(val))
    ans=chr(ord('A')+(ord(val)-ord('a')))
    return ans
    
def main():
    str=input('enter the character: ')
    ans=converter(str)
    print(f'{str} capital character: {ans}')

main()