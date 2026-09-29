def reverse_array_01(arr:list[int])->list:
    temp=[0]*(len(arr)-1)
    for i in range(len(arr)-1,0,-1):
        temp=arr[i]
    print(temp)
    
def main():
    print('abc')