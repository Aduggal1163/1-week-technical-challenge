arr=list(map(int,input("Enter numbers by space: ").split()))
# arr=[1,2,3]
# arr=(1,2,3)
n=len(arr)
sum=0
largest=float('-inf')
smallest=float('inf')
for i in range (n):
    sum+=arr[i]
    if(arr[i]>largest):
        largest=arr[i]
    if(arr[i]<smallest):
        smallest=arr[i]
print(sum)
print(largest)
print(smallest)