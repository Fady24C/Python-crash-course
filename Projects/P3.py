# Calculator
print ("(: Welcome to calculator :)")
First_num=int(input("Enter the First number: "))
Operation=input("Enter the operation: ")
Second_num=int(input("Enter the second number: "))

if Operation=="+":
    print(f"{First_num} + {Second_num} = {First_num + Second_num}" )
elif Operation=="-":
    print(f"{First_num} - {Second_num} = {First_num - Second_num}" )
elif Operation=="*":
    print(f"{First_num} x {Second_num} = {First_num * Second_num}" )
elif Operation=="/":
    print(f"{First_num} / {Second_num} = {First_num / Second_num}" )

print ("(: End of the program :)")