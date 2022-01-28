import glob
import os
from datetime import datetime
import json

os.getcwdb

def step6():

    files = glob.glob('*.json', recursive=False)
    print(files)

    ages = []

    for file in files:
        f = open(file)
        people = json.load(f)

        for person in people :
            dob = datetime.strptime(person['DOB'], '%Y-%m-%d')
            today = datetime.today()
            age = today.year - dob.year
            if (today.month, today.day) <  (dob.month, dob.day) :
                age = age - 1
            ages.append(age)
    print(ages)
    return ages


step6()