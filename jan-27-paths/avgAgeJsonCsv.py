import glob
import os
from datetime import datetime
import json
import csv

os.getcwdb

def step7():

    files = glob.glob('**/*.json', recursive=True)
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

    filesCSV = glob.glob('**/*.csv', recursive=True)
    print(filesCSV)

    for fileCSV in filesCSV:
        with open(fileCSV, newline='') as csvfile:
            peopleCSV = csv.DictReader(csvfile)

            for personCSV in peopleCSV :
                dob = datetime.strptime(personCSV['DOB'], '%Y-%m-%d')
                today = datetime.today()
                age = today.year - dob.year
                if (today.month, today.day) <  (dob.month, dob.day) :
                    age = age - 1
                ages.append(age)


    print(ages)
    avgAge = sum(ages)/len(ages)
    print(avgAge)
    return avgAge


step7()

# need to remove duplicates