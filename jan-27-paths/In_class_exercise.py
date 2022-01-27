import json
import pandas as pd



def birth_state():
    f = open("presidents.json")
    presidents = json.load(f)
    prezs = []
    
    for president in presidents :
        pd.sort_values(by='BirthPlace')
        prez = (president['First'])
        prezs.append(prez)
    print(prezs)
print(birth_state())