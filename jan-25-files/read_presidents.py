import json 
from datetime import datetime

def printAvgAge():
    f = open("presidents.json")
    presidents = json.load(f)

    age = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        # print(dob.year)
        age.append(2022 - dob.year)
        # print(age)
        
    avgAge = sum(age)/len(age)
    print(avgAge)

printAvgAge()

# def printPresidentName():
#     f = open("presidents.json")
#     presidents = json.load(f)

#     for president in presidents :
#         print(president['First'])

# printPresidentName()
