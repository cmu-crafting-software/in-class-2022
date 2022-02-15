from builtins import print
import glob

import json
from datetime import datetime

def step3():
    f = open("presidents.json")
    presidents = json.load(f)

    SOB=[]
    ages = []
    name=[]
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
        SOB.append(president['StateOfBirth'])
        name.append(president['Last'])
    return [SOB, name]

list=step3()
list.sort()
print(list)


files = glob.glob('**/*.csv', recursive=True)
#print(files)
