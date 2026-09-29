def frequency(arr:list[int])->int:# freq ellement is work like when that is same then it's freq is update and when that is not same then 
                                                  # inside the ans takes that ellement where that is not same and again freq is updated by one
    ans=arr[0]
    freq=1
    for i in range(1,len(arr),1):
        if freq==0:
            ans=arr[i]
            freq=1
        elif ans==arr[i]:
            freq=freq+1
        else:
            freq=freq-1
    print(ans)
    return ans

def majority_ell(arr:list[int]):
    ans=frequency(arr)
    freq=0
    for i in range(1,len(arr),1):
        if ans==arr[i]:
            freq=freq+1
            
    con=len(arr)//2
    if freq>=con:
        print(f'in {arr} have mojority ellement is {ans}')
    else:
        print(f'{arr} have not mojority ellement')

def decelartaion_arr():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        ell=int(input(f"enter the ellement in array at posotion {i+1}: "))
        arr.append(ell)
    print(arr)
    majority_ell(arr)
    
decelartaion_arr()