###################[ Dictionary in ch6 ]######################
# - Dictionary: Dic={ Key:value, ... }
# - Loop (v,k) in Dictionary: using for k,v in dic.items:
# - Loop (k) in Dictionary: using for k in dic.keys(): # Default.
# - Loop (k) in Dictionary insort: using sorted()

# - Loop (v) in Dictionary: using for v in dic.values:
# - Loop (v) in Dictionary unique: using set()
# - List of Dictionaries.
# - Dictionary include values are Dictionaries.
# - Dictionary include Dictionaries.
###################[ Dictionary App ]######################
MyDic={
    'Name':'fady',
    'Age': 20,
    "Skills":'ai'
}
print(MyDic)
MyDic['University']='Capital'
print(MyDic['Name'].title())
MyDic['Skills']='ML & Dl'
print(MyDic)    

print('----------------------------------------');
for key, value in MyDic.items():
    print("Key: "+key+" && Value: "+str(value));

print('----------------------------------------');
for key in MyDic.keys():
    print("Key: "+key);

print('----------------------------------------');
for key in MyDic:
    print("Key: "+key);

print('----------------------------------------');
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +", I see your favorite language is " + favorite_languages[name].title() + "!")

print('----------------------------------------');
for value in favorite_languages.values():
    print('Value: '+value);

print('----------------------------------------');
for value in set(favorite_languages.values()):
    print('Value: '+value);

print('----------------------------------------');
if 'Fady' not in favorite_languages.keys():
    print("No exist ,Fady")

print('----------------------------------------');
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print('----------------------------------------');
Dic1={'A':1,'B':2,'C':3};
Dic2={'D':4,'E':5,'M':6};
Dic3={'Q':7,'W':8,'R':9};

Mylist=[Dic1, Dic2, Dic3]
for i in Mylist:
    print(i)

print('----------------------------------------');
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'], 
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
        
print('----------------------------------------');
users= {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton', 
    },
    'mcurie': {
        'first': 'marie', 
        'last': 'curie',
        'location': 'paris'
    },
 }
for username, user_info in users.items(): 
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())