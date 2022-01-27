import json
import os
import glob
from datetime import datetime 
from statistics import mean

def stateSort():
    pres = open("presidents.json")
    presidents = json.load(pres)
    states = []
    names = []
    for president in presidents:
        stateBirth = president['SOB']
        states.append(stateBirth)
        presName = president['First'] + " " + president["Last"]
        names.append(presName)
    
    presDict = {states[i]:names[i] for i in range(len(names))}

    for i in sorted (presDict):
        print ((i, presDict[i]), end = " ")

#stateSort()
#print(os.getcwd())

# change wd to musicians/rock
os.chdir('musicians/rock')
# print(os.getcwd())
# list all of the files in musicians/rock
files = glob.glob('**/*', recursive = True)
# print(files)

# return to jan-27-paths
os.chdir('../..')

# write a function that finds all json files 
files_json = glob.glob('**/*.json', recursive = True)
# print(files_json)

# compute the average age of all people listed in the files
# format: "1935-01-08"
def averageAge():
    pres = open("presidents.json")
    rock = open('musicians/rock/rock.json')
    presidents = json.load(pres)
    rockers = json.load(rock)
    ages = []
    for president in presidents:
        dateBirth = datetime.strptime(president['DOB'], '%Y-%m-%d')
        yearBirth = dateBirth.year
        today = datetime.today()
        age = today.year - yearBirth
        if (today.month, today.day) < (dateBirth.month, dateBirth.day):
            age = age - 1
        ages.append(age) 
    for rockstar in rockers:
        dateBirth = datetime.strptime(rockstar['DOB'], '%Y-%m-%d')
        yearBirth = dateBirth.year
        today = datetime.today()
        age = today.year - yearBirth
        if (today.month, today.day) < (dateBirth.month, dateBirth.day):
            age = age - 1
        ages.append(age) 
        
    print(ages)
    avgAge = mean(ages)
    print(avgAge)

averageAge()
