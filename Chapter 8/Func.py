###################[ Fuction in ch8 ]######################
# - Define the function -> using def fun():
# - Triple parentheses: """Description of function."""
# - def fun(Parameters):
# -     body of function
# - fun(arguments)
# - It's important to interest with positional arguments
# - fun(arguments="value")->clarify the role of each value in the function call
# - def fun(Parameters="Unknown"): ->uses the parameter’s default value.
# - If the parameter has defult value , it not neccessary that match in arguments
# - If you want to have optional argument -> make parameter = '' then check if true 
# - Return of function -> value or list or dictionary
# - Using functions -> to organise the module
# - fun(list)-> reference for function ,but fun(list[:])-> copy for function
# - Passing an arbitrary number of arguments -> Using *toppings
# - Mixing Positional and Arbitrary Arguments -> Using **toppings -> want a function to accept several different kinds of arguments. && additional key-value pairs
# - Importance of import file or from file import function
# - Alias -> as 
# ###################[ Input App ]######################
def Get_name(name='Adam', title='Student'):
    """Print name and title."""
    print("- My Name: "+name)
    print("- My Job: "+title)
    print('------------------------------------')
Get_name('Fady', 'AI engineer')
Get_name(title="Software Engineer", name="Mosa")
Get_name("Logos")
Get_name()


def get_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name 
    return full_name.title()

musician = get_name('AA', 'BB') 
print(musician)
musician = get_name('AA', 'BB', 'CC')
print(musician)
 
