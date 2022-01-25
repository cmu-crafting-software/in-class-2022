import json
from datetime import datetime

def average_age():
    f = open("presidents.json")
    presidents = json.load(f)

    for person in presidents :
        today = datetime.now()
        dob = datetime.strptime(person["DOB"], "%Y-%m-%d")
        dt = today - dob

        for i in dt :
            age = sum(i)/3
            print(age)
