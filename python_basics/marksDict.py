# d={
#     "Rahul": 85,
#     "Aman": 92,
#     "Riya": 78
# }
# for k,v in d.items():
#     print(k," ",v)
# for i in d.keys():
#     print(i)
# for i in d.values():
#     print(i)
n=int(input("Enter no of key value pairs: "))
d={}
for i in range(n):
    k=input("enter key: ")
    v=int(input("enter value: "))
    d[k]=v
toppername=""
avgmarks=0
maxmarks=0
for k,v in d.items():
    if(v>maxmarks):
        maxmarks=v
        toppername=k
    avgmarks+=v
print("Topper Name is: ",toppername)
print("Avg marks are: ",avgmarks/n)

