def reverse_arr(arr:list)->list:
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def main():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        el=int(input(f'enter the value at the position {i+1}: '))
        arr.append(el)
    print('old array is',arr)
    new_arr=reverse_arr(arr)
    print('new array is',new_arr)

main()