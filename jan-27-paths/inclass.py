import json
from datetime import datetime
import glob


def getAvgAge():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
    return ages

def part4():
    f = open("presidents.json")
    presidents = json.load(f)

    states = []
    for president in presidents :
        State = president['State']
        states.append(State)

    states.sort()
    for president in presidents:

        
def part5():
    files = glob.glob('**/*.csv', recursive=True)
    print(files)

part5()