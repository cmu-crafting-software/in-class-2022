import json
from datetime import datetime

def printYears():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y/%m/%d')
        print(dob.year)

print(printYears())