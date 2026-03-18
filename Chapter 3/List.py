###################[ List in ch3 ]######################
# - List-> [ , ]
# - Position, Index
# - Can use string method
# - Index start with zero 
# - [-1] -> return the last element
# - values of list as variable
# - Add, remove, modify
# - list.append(value) -> add in the end
# - list.insert(index, value) -> add in any index
# - Variable = list.pop(index) -> Remove in any index
# - Variable = list.pop() -> Remove in the end
# - list.remove(value) -> Remove using the value if (index is Unknown)
# - del list[index] -> Remove using the value if (index is Unknown)
# - list[index] = new value-> Update the value
# - Sort (Permanent) -> In order: list.sort() -> Alphabetical order
#   In reverse order: list.reverse() ->  reverse flip , no alphabetical order
#   or 
#   list.sort(reverse=True) -> Alphabetical order
# - Sort (Temporary) -> In order:sorted(list), reverse order: sorted(list, reverse=True)
# - IndexError
###################[ Number App ]######################
list=['Fady', 'Romany', 'Yuakeem', 'Laundy']
print(list)
print(list[0])
print(list[0].lower())
print(list[0].title())

print(list[-1])
print(list[-2].lower())
print(list[-3].title())

message= 'Hello, '+list[0]+" "+list[1]+'.'
print(message)

list[-1]='Qous'
print(list)

list.append("Son")
print(list)

motorcycles = []
motorcycles.append('Honda') 
motorcycles.append('Yamaha') 
motorcycles.append('Suzuki')
print(motorcycles)

motorcycles.insert(1,'BMW') 
print(motorcycles)

del motorcycles[2]
print(motorcycles)

lastElement=motorcycles.pop();
print(lastElement)
print(motorcycles)

lastElement=motorcycles.pop(1);
print(lastElement)
print(motorcycles)

motorcycles.remove('Honda')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['A', 'D', 'B', 'C']

print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print(sorted(cars, reverse=True))

print("The len: " + str(len(cars)) + ' items')