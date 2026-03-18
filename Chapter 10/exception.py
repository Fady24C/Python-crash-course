###################[ Errors And Exceptions Raising in ch10 ]######################
# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions
# [7] If exceptions occured -> skip for remained code 
# [8] Exceptions Handling -> Try | Except | Else | Finally
# [9] Try     => Test The Code For Errors
# [10] Except  => Handle The Errors ~ catch error
# [11] Else    => If No Errors
# [12] Finally => Run The Code
# [13] You can use more one except   
###################[ App in ch10 ]######################
y = 10

if type(y) != int:

  raise ValueError("Only Numbers Allowed")
  print("This Will Not Print Because The Error")
  print("This Will Not Print Because The Error")
print("This Will Print Because out of The Error")

print("----------------------------------------------------")

try:  # Try The Code and Test Errors

  number = int(input("Write Your Age: "))
  print("Good, This Is Integer From Try")

except:  # Handle The Errors If Its Found

  print("Bad, This is Not Integer")

else:  # If Theres No Errors # It's Un neccessary

  print("Good, This Is Integer From Else")

finally: # obey even if error occurred or no

  print("Print From Finally Whatever Happens")

print("----------------------------------------------------")

try:
  print(int("Hello"))

except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")

print("----------------------------------------------------")  
# - Advanced Example

open_file = False
Nums_Try = 5

while Nums_Try and open_file == False:
    try:
        print("(: Welcome to my program :)")
        path = input("Enter The File Name With Absolute Path To Open:\n").strip()
        open_file=True
        with open(path) as object_file:
            contents=object_file.read()
            print(contents)

    except:
        print("File Not Found Please Be Sure The Name is Valid")
        Nums_Try-=1

    finally:
        if open_file:
            print("File closed")
            # path.closed()

print("All Tries Is Done")        