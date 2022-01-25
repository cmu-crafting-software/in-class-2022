import json
from datetime import datetime

def presidentAge():
    f = open('presidents.json')
    presidents = json.load(f)

    for president in presidents :
        birthYear = datetime.strptime(president['DOB'], '%Y-%m-%d')
        print birthYear.year

    ages = []
    for president in presidents:
        birthYear = datetime.strptime(president['DOB'], '%Y-%m-%d')
        DOB = birthYear.year
        age = 2022 - DOB
        ages.append(age) 
    avgAge = mean(ages)
    print(avgAge)

presidentAge()
