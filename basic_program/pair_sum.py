def pair_sum(arr:list,target:int)->list:
    pair_sum_indx=[]
    for start in range(0,len(arr)-1,1):
        for end in range(start+1,len(arr),1):
            sum=arr[start]+arr[end]
            print(sum)
            if sum==target:
                pair_sum_indx.append(start)
                pair_sum_indx.append(end)
                return pair_sum_indx
    
    return pair_sum_indx

def two_pointer_app(arr:list[int],target:int)->list:# that approach work well when the array is the sorted 
    pair_sum_index=[]
    start=0
    end=len(arr)-1
    while(start<end):
        sum=arr[start]+arr[end]
        if sum<target:
            start=start+1
        elif sum>target:
            end=end-1
        else:
            pair_sum_index.append(start)
            pair_sum_index.append(end)
            return pair_sum_index
        
    return pair_sum_index
            
def created_arr()->list:
    size=int(input("enter the size of the array: "))
    arr=[]
    for i in range(0,size,1):
        ell=int(input(f"enter the ellement at the {i+1} pos in the array: "))
        arr.append(ell)
    
    print(arr)
    return arr

arr=created_arr()
target=int(input("enter the target: "))
result=pair_sum(arr,target)
print(result)