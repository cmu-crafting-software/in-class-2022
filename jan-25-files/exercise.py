import json
import os
from datetime import datetime

def printAges():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for guy in presidents :
        yob = datetime.fromisoformat(guy['DOB']).year
        ages.append(2022-yob)

    print(sum(ages)/len(ages))

printAges()

