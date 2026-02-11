arr=[]
while(True):
    n=int(input("for adding press 1, for show all tasks press 2 and for exit press 3: "))
    if(n==1):
        m=input("Enter task you want to add: ")
        arr.append(m)
    elif(n==2):
        size = len(arr)
        if(size==0): print("No tasks yet")
        else :
            for i in range (size):
                print(i+1,arr[i])
    elif (n==3):
        print("Exitting!")
        break
    else:
        print("Press correct button")
