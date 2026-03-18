###################[ File in ch10 ]######################
# - Read from a file:
# - 1. with open(path) as file_object: --> open the file
# - 2. contents=file_object.read() OR lines = file_object.readlines()
# - New string = Old string.Replace("old",'new')
# - Make List= string.split(seperators)
# - Count= string.count("word/char")
# - write in a file:
# - 1. with open(path,'a') as file_object:  a -> add + old || w -> write after delete all
# - 2. file_object.write("\nHello, I'm AI engineer") 
###################[ App in ch10 ]######################
path="c:\\Users\\PoLa\\Downloads\\test.txt"
with open(path) as file_object:
    contents=file_object.read()
    print(contents.rstrip())

    Lencon=contents.split(" ")
    print(f"Len: {len(Lencon)} words")

with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())
        print("---------------------")

with open(path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
    print("*************************")

Strings_line ="" 
with open(path) as file_object:
    lines = file_object.readlines()
for line in lines:
    Strings_line+=line.rstrip()

print(Strings_line)    
print(len(Strings_line))    
print(Strings_line[:22])

if "We are strong" in Strings_line:
    print("yes,it exist")
else:
    print("No")

print(Strings_line)    


with open(path,'a') as file_object:
    file_object.write("\nHello, I'm AI engineer")    
    file_object.write("\nHello, I'm ML eng")    
print(Strings_line)    

Strings_line = Strings_line.replace("We are happy"," He is nerous ")
print(Strings_line)    

line = "Row, row, row your boat"
print(line.count('row'))
line.lower().count('row')
