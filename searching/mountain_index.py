'''in that we find the top ellement in the array where that is half part in increasing order and after that some part is in decreasing order'''
def created():
    size=int(input('enter the size of the array: '))
    arr=[]
    for i in range(0,size,1):
        ell=int(input('enter the ellement in the array: '))
        arr.append(arr)
    return arr

def func(arr:list[int]):
    start,end=0,len(arr)-1
    ans=-1
    mid=-1
    while(start<=end):
        mid=start+(end-start)//2
        mid=end+(start-end)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            start=mid+1
        else:
            end=mid-1
    return mid

def second_approach(arr:list[int]):
    start,end=0,len(arr)-1
    while(start<end):
        mid=start+(end-start)//2
        if arr[mid]<arr[mid+1]:# then move left side becouse here next element is greateer then that's
            start=mid+1
        else:
            end=mid
    return start

def main():
    arr=created()
    ans=second_approach(arr)
    print(f'the peak element in the array is {ans}')