import json
from datetime import datetime
import glob


def step3():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    agesum = 0
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
        agesum = agesum + age
    return agesum/len(ages)

def part4():
    f = open("presidents.json")
    presidents = json.load(f)

    states = []
    for president in presidents :
        State = president['State']
        states.append(State)

    states.sort()
    pres = []
    for state in states:
        for president in presidents :
            if president.get('State') == state:
                print(president['First'], president['Last'])

part4()