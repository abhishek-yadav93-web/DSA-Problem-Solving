def first_approach(num:int)->bool:
    if num<=0:
        return False
    else:
        while(num!=1):
            if num%2==1:
                return False
            num=num//2
            
    return True