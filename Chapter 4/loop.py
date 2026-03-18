###################[ List in ch4 ]######################
# - Loop-> For variable in list: indented line. 
# - Any indent without reason give problems.    
###################[ List App ]######################
list= ['F', 'A', 'D', 'Y', 'R', 'O', 'M']
for i in list:
    print("### Letter["+i+']');
    print('--> '+i);

print('-----------------------------------')

for i in list:
    print("### Letter["+i+']');
    
    print('--> '+i);

print('-----------------------------------')

for i in list:
    print("### Letter["+i+']');
print('--> '+i);

###################[ List in ch4 ]######################
# - Range -> range(start,stop end) or range(start,stop end, nums of jumps to skip)
# - list(range()) -> turn to List.(ERROR?!)
# - min(list),max(list),sum(list) 
# - Comprehensions list: list=[var for in range()] without(:)
###################[ List App ]######################
for i in range(2,11):
    print('i: '+ str(i));

Evenlist=[]
for i in range(2,11,2):
    i*=2;
    Evenlist.append(i);
print(Evenlist)
print('Max: '+str(max(Evenlist)))
print('Min: '+str(min(Evenlist)))
print('Sum: '+str(sum(Evenlist)))

squares=[i**2 for i in range(1,7)]
print(squares)
print('-----------------------------------');
###################[ List in ch4 ]######################
# - Slicing a list -> list[start:stop]
# - Without a starting index, Python starts at the beginning of the list
# - Without a ending index, Python ends at the ending of the list
# - Can use loop through slice
# - Copy a list -> list[:] without reference or list1=list2 with reference 
# - Tuple: list without any changes -> tuple(start,end) 
# - Change in tuple-> error ,but overwrite no give error 
###################[ List App ]######################
mylist=['A','B','C','D','E','F']
print(mylist[0:4])
print(mylist[:4])
print(mylist[2:])
print(mylist[-3:])
print(mylist[:])

print('-----------------------------------')

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:") 
for player in players[:3]:
    print(player.title())
    
print('-----------------------------------')

list1=['A','B','C','D','E','F'];
list2=list1[:]  # without reference
list3=list1     # reference
list1.append('G');
print('List1: '+str(list1))
print('List2: '+str(list2))
print('List3: '+str(list3))

print('-----------------------------------')

mytuple=(200,5)
for i in mytuple:
    print(i)

# mytuple[1]=45 -> give error
mytuple=(100,4) # -> Overwrite if you want modification
for i in mytuple:
    print(i)


