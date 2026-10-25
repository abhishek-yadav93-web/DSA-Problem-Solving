'''inside there we solve addvance pattern problem related to square shape '''
def practice1(size):
    for rows in range(1,size+1,1):
        char=chr(ord('a')+(rows-1)) # in there ord function return the ASCI value of the character and that is int type and char is retunr the character of int value
        for colls in range(1,size+1,1):
            print(char,end=" ")
        print()
    
def practice2(size):
    for rows in range(1,size+1,1):
        for colls in range(1,size+1,1):
            char=chr(ord('a')+colls-1)
            print(char,end=" ")
        print()
    
def practice3(size):
    start=0
    for rows in range(1,size+1,1):
        for colls in range(1,size+1,1):
            start=start+1
            print(start,end=" ")
        print()
        
def practice4(size:int):# practice 4 and practice 5 work like a same but major different between them is inside the practice 4 no created extra function
    for rows in range(1,size+1,1):
        for cols in range(1,size+1,1):
            print(((rows-1)*size)+cols,end=" ")
        print()

def practice5(size:int):
    for  rows in range(1,size+1,1):
        for colls in range(size,0,-1):
            print(colls,end=" ")
        print()
    
def func():
    size=int(input('enter the size: '))
    print('first pattern')
    practice1(size)
    print('second pattern')
    practice2(size)
    print('third pattern')
    practice3(size)
    print('fourth pattern')
    practice4(size)
    print('fifth pattern')
    practice5(size)
    
func()
            