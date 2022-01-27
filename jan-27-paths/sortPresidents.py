import json

f = open("presidents.json")
presidents = json.load(f)

print(presidents)

BirthState = []
for president in presidents :
    state = president['BirthState']
    BirthState.append(state)

print(BirthState)
BirthState.sort()
print(BirthState)