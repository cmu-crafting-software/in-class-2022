import json
from datetime import datetime

def printAvgage():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for president in presidents:
        president = datetime.strptime(president['DOB'], '%Y/%m/%d')
        print (president.year)

printAvgage()

