import glob
import os
from datetime import datetime
import json

def step5():
    print(os.getcwd())
    os.chdir('musicians/rock')
    files = os.listdir(os.getcwd())
    for f in files:
        print(f)

def computeAverageAge(paths):
    ages = []
    today = datetime.today()
    for path in paths:
        f = open(path)
        people = json.load(f)
        for person in people :
            dob = datetime.strptime(person['DOB'], '%Y-%m-%d')
            age = today.year - dob.year
            if (today.month, today.day) <  (dob.month, dob.day) :
                age = age - 1
            ages.append(age)

    return sum(ages)/len(ages)



def step6(cwd):
    os.chdir(cwd)
    files = glob.glob('**/*.json', recursive=True)
    print(files)
    print(computeAverageAge(files))


cwd = os.getcwd()
step5()
step6(cwd)