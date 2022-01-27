import glob
import os
from datetime import datetime
import json
import csv

def step7():
    # find all the json files and all the csv files
    jsonfiles = glob.glob('**/*.json', recursive=True)
    csvfiles = glob.glob('**/*.csv', recursive=True)

    # add all the information from json file into a map
    people = dict()
    for jfp in jsonfiles:
        jf = open(jfp)
        jps = json.load(jf)
        for jp in jps:
            fullname = jp['First'] + "@" + jp['Last']
            dobSet = people.get(fullname, set())
            dobSet.add(jp['DOB'])
            people[fullname] = dobSet

    # add all information from csv file into the map
    for cfp in csvfiles:
        cf = open(cfp)
        creader = csv.reader(cf)
        creader.__next__()
        for row in creader:
            fullname = row[0] + "@" + row[1]
            dobSet = people.get(fullname, set())
            dobSet.add(row[2])
            people[fullname] = dobSet
    
    # check people to verify there is no duplicate
            
    ages = []
    today = datetime.today()
    for key in people.keys():
        print(key)
        for dobstr in people[key]:
            dob = datetime.strptime(dobstr, '%Y-%m-%d')
            age = today.year - dob.year
            if (today.month, today.day) <  (dob.month, dob.day) :
                age = age - 1
            ages.append(age)
    return sum(ages)/len(ages)

print(step7())
            

        