students = {}
while True:
    print("\n1 Add student")
    print("2 Show all students")
    print("3 Show topper")
    print("4 Exit")
    choice = int(input("Enter choice: "))
    if(choice == 1):
        name=input("Enter student name: ") 
        marks = int(input("Enter marks: "))
        students[name]=marks
    elif (choice ==2):
        if len(students) == 0:
            print("No student records")
        else:
            print("\nStudent Records:")
            for name, marks in students.items():
                print(name, ":", marks)
    elif (choice ==3):
        if len(students) == 0:
            print("No student records")
        else:
            topper=max(students,key=students.get)
            print("Topper is : ",topper, "with ",students[topper], "marks")
    elif choice ==4:
        print("Exiting !")
        break
    else:
        print("Invalid choice")