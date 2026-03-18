###################[ If in ch5 ]######################
# - if condition:
#      ->statements.
#   elif condition:
#      ->statements.
#   else:(optional)
#      ->statements.
# - Note: It isn't VIP -> add parentheses
# - Check quality-> ==
# - Set the value-> =
# - Check quality-> !=
# - Multiple conditions: and - or 
# - Checking Whether a Value Is or no in a List-> value in list
# - Check list is not empty-> if list:
# - Loop on the list -> for MyList in MyList:
###################[ If App ]######################
Age = 12;
if Age == 12:
    print("Age is twelve.")
else:
    print("Age isn't twelve.") 

MyList =['A','B','C','D','E'];
if 'A'== MyList[0] or 'A' in MyList:
    print("Exist!!!")
else:
    print("No exist!!!")     

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

print("--------------------------------------------")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("--------------------------------------------")

MyList = ['AAA', 'BBB','CCC','DDD','EEE']
if MyList: # Check if list is not empty
    for MyList in MyList:  # Loop on the list
        print("Adding " + MyList + ".") 
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
