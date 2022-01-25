import json
from datetime import datetime

def getAvgAge():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        DOB = datetime.strptime(president['DOB'], "%Y-%m-%d")
        print(DOB)
        age = 2022 - president.Y
        print(age)
        ages.append(age)



getAvgAge()