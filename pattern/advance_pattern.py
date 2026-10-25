'''
                       *
                *     *     *
         *     *     *     *     *
    *   *     *     *     *      *     *
'''

def practice1(size):
    for rows in range(1,size+1,1):
        for colls in range(1,size-rows+1,1):
            print(' ',end=' ')
        for colls in range(1,2*rows-1+1,1):
            print('*',end=' ')
        print()
'''
             1
        1   2   1
    1  2   3   2   1
1  2  3   4   3   2   1
'''
def practice2(size):
    for rows in range(1,size+1,1):
        for colls in range(1,size-rows+1,1):
            print(' ',end=' ')
        for colls in range(1,rows+1,1):
            print(colls,end=' ')
        for colls in range(rows-1,0,-1):
            print(colls,end=' ')
        print()
'''  
              *   *    *    *   *   *   
                   *    *    *    *
                         *  *   *
                            *
'''
def practice3(size):
    for rows in range(size,0,-1):
        for colls in range(size-rows,0,-1):
            print(' ',end=' ')
        for colls in range(1,2*rows,1):
            print('*',end=' ')
        print()
        
def func():
        size=int(input('enter the size of the pattern: '))
        print('first pattern')
        practice1(size)
        print('second pattern')
        practice2(size)
        print('third pattern')
        practice3(size)
        
func()
        