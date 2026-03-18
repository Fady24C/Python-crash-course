import json

file="S.json"
with open(file) as file_object:
    content = json.load(file_object)
print(content)    