'''that section we learn and solve the triangle pattern problem'''
def practice1(size):
    for rows in range(1,size+1,1):
        for cols in range(1,rows+1,1):
            print("*",end=" ")
        print()

def practice2(size):
    for rows in range(1,size+1,1):
        for colls in range(1,rows+1,1):
            print(colls,end=" ")   
        print()

def practice3(size):
    for rows in range(1,size+1,1):
        for colls in range(1,rows+1,1):
            print(rows,end=" ")
        print()

def practice4(size):
    for rows in range(1,size+1,1):
        for colls in range(rows,0,-1):
            print(colls,end=" ")     
        print()

def practice5(size):
    for rows in range(1,size+1,1):
        char=chr(ord('a')+rows-1)
        for colls in range(1,rows+1,1):# inside ther when we want to run the loop at last end then inculde (last+1)
            print(char,end=" ") 
        print()

'''reverse array triangle patterns'''
def practice6(size:int):
    for rows in range(1,size+1,1):
        temp=size-rows+1
        for colls in range(1,temp+1,1):
            print(colls,end=" ")
        print()

def practice7(size:int):
    for rows in range(1,size+1,1):
        temp=size-rows+1
        for colls in range(1,temp+1,1):
            print("*",end=" ") 
        print()
        
def practice8(size:int):
    for rows in range(size,0,-1):
        for colls in range(1,rows+1,1):
            print(colls,end=" ")
        print()

def practice9(size):
    for rows in range(1,size+1,1):
        for colls in range(size,size-rows,-1):
            print(colls,end=" ")
        print()
        
def func():
    size=int(input('enter the size of the pattern: '))
    # print('first pattern')
    # practice1(size)
    # print('second pattern')
    # practice2(size)
    # print('third pattern')
    # practice3(size)
    # print('fourth pattern')
    # practice4(size)
    # print('fifth pattern')
    # practice5(size)
    # print('sixth pattern')
    # practice6(size)
    # print('seventh pattern')
    # practice7(size)
    # print('eighth pattern')
    # practice8(size)
    print('nineth pattern')
    practice9(size)

func()