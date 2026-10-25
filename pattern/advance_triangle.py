def practice1(size):
    for row in range(1,size+1,1):
        for coll in range(1,size-row+1,1):
            print(" ",end=" ")
        for coll in range(1,row+1,1):
            print("*",end=" ")
        print()

def practice2(size):
    for row in range(1,size+1,1):
        for coll in range(1,size-row+1,1):
            print(" ",end=" ")
        for coll in range(1,row+1,1):
            print(row,end=" ")
        print()
    
def practice3(size):
    for row in range(1,size+1,1):
        for colls in range(1,size-row+1,1):
            print(' ',end=' ')
        for colls in range(1,row+1,1):
            print(colls,end=' ')
        print()

def practice4(size):
    for rows in range(1,size+1,1):
        for colls in range(1,size-rows+1,1):
            print(' ',end=' ')
        for colls in range(1,rows+1,1):
            char=chr(ord('A')+colls-1)
            print(char,end=' ')
        print()

def practice5(size:int):
    for rows in range(1,size+1,1):
        for colls in range(1,size-rows+1,1):
            print(' ',end=' ')
        for colls in range(rows,0,-1):
            print(colls,end=' ')
        print()
        
def func():
    size=int(input('enter the size of the pattern'))
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