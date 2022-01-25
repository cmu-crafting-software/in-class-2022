import json
import csv
from datetime import datetime 
from statistics import mean

def averageAge():
    pres = open("presidents.json")
    presidents = json.load(pres)
    ages = []
    for president in presidents:
        dateBirth = datetime.strptime(president['DOB'], '%Y-%m-%d')
        yearBirth = dateBirth.year
        age = 2022 - yearBirth
        ages.append(age) 
    avgAge = mean(ages)
    print(avgAge)

averageAge()

def stateSort():
    pres = open("presidents.json")
    presidents = json.load(pres)
    states = []
    names = []
    for president in presidents:
        stateBirth = president['SOB']
        states.append(stateBirth)
        presName = president['First'] + " " + president["Last"]
        names.append(presName)
    
    presDict = {states[i]:names[i] for i in range(len(names))}

    for i in sorted (presDict):
        print ((i, presDict[i]), end = " ")

stateSort()
