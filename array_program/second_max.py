def second_max(arr:list)->list:
    int_min=arr[0]
    for i in range(1,len(arr),1):
        if arr[i]>int_min:
            int_min=arr[i]
    ans=arr[0]
    for i in range(1,len(arr),1):
        if arr[i]!=int_min:
            ans=max(ans,arr[i])
    return ans

def main():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        ell=int(input(f'enter the ellement at the {i+1} position in the array: '))
        arr.append(ell)
    
    ans=second_max(arr)
    print(f'second largest ellement in the array {arr} is {ans}')

main()