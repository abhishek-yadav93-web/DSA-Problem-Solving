def find_elle(pos:int)->int:
    ''' that function is returnt he nth posotion ellement in the finonacci sequence '''
    arr=[0]*pos #that is created the n size of the array
    arr[0]=0
    arr[1]=1
    print(arr)
    for i in range(2,len(arr),1):
        arr[i]=arr[i-1]+arr[i-2]
    
    print(arr)
    return arr[pos-1]

def main():
    pos=int(input('enter the which posotion ellement you want to find: '))
    ans=find_elle(pos)
    print(f'att {pos} the ellement is {ans} in the fibonacci sequence')

main()