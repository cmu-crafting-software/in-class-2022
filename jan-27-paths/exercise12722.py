import json
import csv
import os
from datetime import datetime
import glob

def printAges():
    f = open("presidents.json")
    presidents = json.load(f)

    ages = []
    for guy in presidents :
        yob = datetime.fromisoformat(guy['DOB']).year
        ages.append(2022-yob)

    print(sum(ages)/len(ages))

def printStates():
    f = open("presidents.json")
    presidents = json.load(f)

    states = []
    for guy in presidents :
        state = guy['SOB']
        states.append(state)

    states.sort()
    print(states)

    
def printFiles():
    os.chdir('musicians/rock')
    print(os.listdir())

def printAllAges():
    ages = []
    os.chdir("C:/Users/Dan/Box/Class/Spring 2022/17905 Crafting Software/in-class-2022/jan-27-paths")
    files = glob.glob('**/*.json', recursive=True)
    for f in files:
        file = open(f)
        people = json.load(file)

        for person in people :
            yob = datetime.fromisoformat(person['DOB']).year
            ages.append(2022-yob)

    print(sum(ages)/len(ages))

def printAllAgesBoth():
    allPeople = []
    ages = []
    os.chdir("C:/Users/Dan/Box/Class/Spring 2022/17905 Crafting Software/in-class-2022/jan-27-paths")
    jsons = glob.glob('**/*.json', recursive=True)
    csvs = glob.glob('**/*.csv', recursive=True)
    for f in jsons:
        file = open(f)
        people = json.load(file)
        for person in people :
            allPeople.append(person)

    for f in csvs:
        rowlist = []
        with open(f, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                rowlist.append(row)
            csvToJson = json.dumps(rowlist)
            for person in csvToJson:
                allPeople.append(person)

    for person in allPeople:
        print(person['DOB'])
            yob = datetime.fromisoformat(person['DOB']).year
            ages.append(2022-yob)

    print(sum(ages)/len(ages))




printAllAgesBoth()

