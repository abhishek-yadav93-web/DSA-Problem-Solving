def search_algo(arr:list[int],num:int)->bool:
    for i in range(0,len(arr),1):
        if arr[i]==num:
            return True
    return False

def main():
    size=int(input('enter ise of the arr: '))
    arr=[]
    for i in range(0,size,1):
        el=int(input(f'enter the number at position {i+1}: '))
        arr.append(el)
    num=int(input('enter the number those you wnat to search: '))
    res=search_algo(arr,num)
    if res:
        print(f'{num} is present in list')
    else:
        print(f'{num} is not present in list')
    
main()
        