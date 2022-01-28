import json

f = open("presidents.json")
presidents = json.load(f)

#print(presidents)

def orderPresidents(): 
    BirthStates = []
    for president in presidents :
        state = president['BirthState']
        BirthStates.append(state)

    BirthStates.sort()

    presidentOrdered = []
    for BirthState in BirthStates: 
        for president in presidents :
        
            if president.get('BirthState') == BirthState: 
                presidentOrdered.append(president['First'])


    print(presidentOrdered)
    return 

orderPresidents()