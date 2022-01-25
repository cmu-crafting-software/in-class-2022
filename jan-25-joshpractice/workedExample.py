import json
from datetime import datetime

def printYears():
    f = open("constitutional_amendments.json")
    amendments = json.load(f)

    ages = []
    for amendment in amendments :
        ratified = datetime.strptime(amendment['Ratified'], '%m/%d/%Y')
        print(ratified.year)