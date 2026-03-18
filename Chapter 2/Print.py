###################[ Variable in ch2 ]######################
# - Rules & advices
###################[ Variable App ]######################
message="Hello world!";
print(message);
message = 'Hello Python Crash Course reader!' 
print(message)
message = "One of Python's strengths is its diverse community."
print(message)
message='Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(message)

###################[ String in ch2 ]######################
# - quotes
# - Combination (+)
# - Methods, title, upper, lower
# - spaces: \t,\n,...
# - Strip: rstrip(), lstrip(), strip()
###################[ String App ]######################
name='Fady romany'
org='Original: '+ name
print(org);
title='TitleCase: '+name.title()
print(title)
up='UpperCase: '+name.upper()
print(up)
low='LowerCase: '+name.lower()
print(low)

space=' we are go '
print(space.rstrip()) #delete the right
print(space.lstrip()) #delete the left
print(space.strip())  #delete the right & right

###################[ Number in ch2 ]######################
# - Data types: integer,float
# - Operations: +, -, *, /, %
# - ** -> refer to exponential
# - Division: at least, one is float 
# - str() -> convert num to string 
# - Comment -> using (#), importance
###################[ Number App ]######################
print(1+2);
print(1+2.0)
print(.1+.1)
print(.1+.3)
print(2*.3)
print(3*.3)
age=20
message = "Happy " + str(age) + "rd Birthday!"
print(message)

###################[ The Zen in ch2 ]######################
import this
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!