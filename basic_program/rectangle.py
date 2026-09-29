def check_reactangle_create(a,b,c,d)->bool:
    '''we have four side with that side check, reactangle created or not {combination of two paris taking four is 4c2} '''
    if (a==b and c==d)  or (a==c and b==d) or (a==d and b==c):
        return True
    else:
        return False
    
def main():
    a=int(input("enter the first side: "))
    b=int(input('enter the second side: '))
    c=int(input('enter the third side: '))
    d=int(input('enter the forth side: '))
    ans=check_reactangle_create(a,b,c,d)
    if ans:
        print('with that side we makes the reactangle')
    else:
        print('with that side we not makes the reactangle')