import json
from datetime import datetime

def step3():
    f = open("presidents.json")
    presidents = json.load(f)

    birthStates = []
    for president in presidents :
        birthState = president['BirthState']
        firstname = president['First']
        lastname = president['Last']
        #dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        #today = datetime.today()
        #age = today.year - dob.year
        #if (today.month, today.day) <  (dob.month, dob.day) :
         #   age = age - 1
        birthStates.append(firstname + " " + lastname + ": " + birthState)
    return birthStates

print(step3())