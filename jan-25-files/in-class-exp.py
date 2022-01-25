import json
from datetime import datetime

def printYears():
    f = open("presidents.json")
    presidents=json.load(f)
    age=[]
    total_age=[]
    for president in presidents:
        p2 = datetime.strptime(president['DOB'],'%Y-%m-%d')
        age=2022-p2.year
        
        print(age)



age=printYears()
print(age)
