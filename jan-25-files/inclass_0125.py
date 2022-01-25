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

#def stateSort():
#    pres = open("presidents.json")
#    presidents = json.load(pres)
#    for president in presidents:
#        stateBirth = president['']

