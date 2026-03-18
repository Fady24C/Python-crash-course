###################[ Input in ch7 ]######################
# - variable = Input("Prompt")
# - int(input)-> convert string to int.
###################[ Input App ]######################
# Prompt=input("What is title of job? ")
# Prompt+=" "
# Prompt+=input("What's your name? ")
# print("Hello, "+Prompt.title());

# age =input("How old are you? ")
# if int(age)>18:
#     print(Prompt+ " has "+ age)
#     print("You are free")
# else:
#     print(Prompt+ " has "+ age)
#     print("You are young")
    
# print('----------------------------------------------')    
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")    

###################[ While in ch7 ]######################
# - Loop using while -> while condition: statements 
# - flag-> signal to the program : true or false
# - break -> exit the loop imedialtely
# - continue -> skip the remainding code.
# - Removing All Instances of Specific Values from a List using while value in list: list.remove(value)
# - Filling a Dictionary with User Input
###################[ While App ]######################
# rule = ("Enter you word, but if it is quit program will end!!!\n")
# message = '';
# while message !='quit':
#     message=input(rule);
#     if(message=='quit'):
#         break;
    # if(message!='quit'):
    #     print(message)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
for i in unconfirmed_users:# will end when the list is empty (better from for loop as it's bahavior is Unpredictabel)
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


flag =True
MyDic = {};
while flag:
    key=input("Enter Key? ")
    value=input("Enter Value? ")
    MyDic[key]=value
    que=input("Would you like to let another key respond? (yes/ no) ")
    if que == 'yes':
        flag =True;
    else:
        flag=False;    

print("\n--- Poll Results ---")
for key, value in MyDic.items():
    print(key + " would like to climb " + value + ".")