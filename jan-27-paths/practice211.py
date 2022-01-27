import json

def state():
    f = open("presidents.json")
    presidents = json.load(f)

    for person in presidents:
        state = person['BirthState']
        President = person['Last']
        print(state + " " + President)
        

state() 
