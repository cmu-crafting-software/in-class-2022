import json
from datetime import datetime

def presidentAge():
    f = open('presidents.json')
    presidents = json.load(f)

    ages = []
    for president in presidents :
        birthYear = datetime.strptime(president['DOB'], '%Y-%m-%d')
        DOB = birthYear.year
        #print DOB
        age = 2022 - DOB
        #print age
        ages.append(age) 

    avgAge = sum(ages) / len(ages)
    print "Average  president age: ", avgAge

state = []
def sortByState():
    f = open('presidents.json')
    presidents = json.load(f)

    
    for president in presidents :
        birthPlace = (president['State'])
        #print birthPlace
        state.append(birthPlace)
    print state
        



presidentAge()
sortByState()