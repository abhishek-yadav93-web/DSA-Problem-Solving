n=int(input("enter the number of size of the array: "))
arr=[]
for i in range(0,n,1):
    el=int(input(f"enter the ellement at {i+1} position in the array: "))
    arr.append(el)

print(arr)
curent_sum=0
max_sum=float('-inf')

for i in range(0,len(arr),1):
    curent_sum=curent_sum+arr[i]
    max_sum=max(curent_sum,max_sum)
    if curent_sum<0:
        curent_sum=0

print(max_sum)