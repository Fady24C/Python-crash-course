##################[ Storing data in json in ch10 ]#######
# - 
###################[ Apps in ch10 ]######################
import json

file="SS.json"

print('---Age in Days Calculator---')
try:
    with open(file) as file_object:
        content = json.load(file_object)
    print(content)    

except FileNotFoundError:
    Name=input("Enter your name: ")
    Age=int(input("Enter your age in years: "))
    data=f"Name:{Name} -> Age: {Age}-> lived: {Age*365}"
    with open(file, 'w') as file_object:
        json.dump(data,file_object)
    print(f"You have lived for {Age*365} days")

print('--- :) End the program (: ---')

####################{OR}#########################
print("----------------------------------")
def get_stored_username():
    try:
        with open(file) as file_object:
            content = json.load(file_object)
        return content   

    except FileNotFoundError:
        return None

def get_new_username():
    Name=input("Enter your name: ")
    Age=int(input("Enter your age in years: "))
    data=f"Name:{Name} -> Age: {Age}-> lived: {Age*365} days"
    with open(file, 'w') as file_object:
        json.dump(data,file_object)
    print(f"You have lived for {Age*365} days")
    return data
    
def greet_user():
    content = get_stored_username() 
    if content:
        print("Welcome back!")
        print(content)
    else:
        content = get_new_username() 
        print("We'll remember you when you come back!")
greet_user()