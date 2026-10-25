'''inside there we solve basic pattern problem related to square shape'''
def practice1(size):
    for row in range(1,size+1,1):
        for coll in range(1,size+1,1):
            print("*",end=" ")
        print()

def practice2(size):
    for row in range(1,size+1,1):
        for colls in range(1,size+1,1):
            print(row,end=" ")
        print()
    
def practice3(size):
    for rows in range(1,size+1,1):
        for cols in range(1,size+1,1):
            print(cols,end=" ")
        print()

def practice4(size):
    for rows in range(1,size+1,1):
        for colls in range(1,size+1,1):
            print(colls*colls,end=" ")
        print()
    
def func():
    size=int(input('enter the size: '))
    practice1(size)
    print('second pattern')
    practice2(size)
    print('third pattern')
    practice3(size)
    print('fourth pattern')
    practice4(size)
    
func()