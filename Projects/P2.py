#Dashboard 
Student ={}
def AddStudent(name):
    Student[name]=[];

def Addgrade(name, grade):
    Student[name].append(grade)

def Average(name):
    Avg=0
    for i in Student[name]:
        Avg+=i
    return Avg/2
    
def ShowAllStudent():
    print("**********")
    for i,k in Student.items():
        print(f"- {i}")
        print("Grade: ")
        for e in k:
            print(f"+ {e}")
    print("**********")

while True:
    print("-------------------")
    print("1. Add Student\n2. Add Grade\n3. Calculate Average\n4. Show All Students\n5. Exist.")
    print("-------------------")
    Menu=int(input("Enter the Num: "))

    if Menu == 1:
        Name=input("Enter name of student: ").title()
        AddStudent(Name)
    
    elif Menu == 2:
        Name=input("Enter name of student: ").title()
        if Name in Student.keys():
            grade=int(input(f"Enter Grade of {Name}: "))
            Addgrade(Name, grade)
        else:
            print("This student isn't exist.")    
    
    elif Menu == 3:
        Name=input("Enter name of student: ").title()
        avg=Average(Name)
        print(f"{Name} has {avg}%")
    
    elif Menu == 4:
        ShowAllStudent()

    elif Menu == 5:
        break
    
    else:
        print("Invalid choice.")


        




