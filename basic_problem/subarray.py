n=int(input("enter the number of size: "))
arr=[]
for i in range(n):
    ell=int(input(f"enter the element at the {i+1} position: "))
    arr.append(ell)

print(f'array is {arr}')

for start in range(0,n,1):
    for end in range(start,n,1):
        sub_arr=[]
        sub_arr_sum=0
        for i in range(start,end+1,1):
            sub_arr.append(arr[i])
            sub_arr_sum=sub_arr_sum+arr[i]
        print(f"{sub_arr} = {sub_arr_sum}")
        