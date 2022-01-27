import json
from datetime import datetime


def averageAges():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for pr in presidents :
        dob = datetime.strptime(pr['DOB'], '%Y-%m-%d')
        ages.append(2022-dob.year)

    print(sum(ages)/len(ages))

averageAges()

def printByState():
    f = open("presidents.json")
    presidents = json.load(f)
    presidents.sort(key=lambda x: x['SOB'])

    for pr in presidents:
        print()
    