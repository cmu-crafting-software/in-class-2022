import json 
from datetime import datetime

def printAge():
    f = open("presidents.json")
    presidents = json.load(f)

    age = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        print(dob.year)
        age = dob.year - 2022
        print(age)

printAge()

# def printPresidentName():
#     f = open("presidents.json")
#     presidents = json.load(f)

#     for president in presidents :
#         print(president['First'])

# printPresidentName()
