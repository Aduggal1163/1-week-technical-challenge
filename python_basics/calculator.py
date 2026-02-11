n1=int(input("enter first number: "))
o=input("enter operator: ")
n2=int(input("enter second number: "))
if(o=='*'):
    print(n1*n2)
elif(o=='+'):
    print(n1+n2)
elif(o=='-'):
    print(n1-n2)
elif(o=='/'):
    print(n1/n2)
else:
   #print("please enter valid operator")
   raise ValueError("please enter valid operator")