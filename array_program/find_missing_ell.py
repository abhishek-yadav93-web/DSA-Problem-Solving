def find_ell(arr:list[int])->int:
    '''that function find missing ellement in the arry those are not found in the continous array'''
    size=len(arr)+1
    a=arr[0]
    b=arr[len(arr)-1]
    # total_sum=(size*(size+1))//2 that is work when given the array ellement is starting from 1
    total_sum=((a+b)*(b-a+1))//2 # that is work for all the condition but the different is allays is 1 
    sum=0
    for i in range(0,len(arr),1):
        sum=sum+arr[i]
        
    ans=total_sum-sum
    return ans

def main():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        ell=int(input('enter the ellement in the array: '))
        arr.append(ell)
    
    ans=find_ell(arr)
    print(f'the ellement is {ans} is not found in the array')

main()
        
    
    