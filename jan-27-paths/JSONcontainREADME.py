import glob
import json
import os
from datetime import datetime

def getJson():
    ages = []
    path = '/Users/luka0725/17950_CraftingSoftware/in-class-2022/jan-27-paths/'
    if os.path.isfile(path + '/README.md') == True:
         file = glob.glob(path + '/*.json', recursive=True)
         ages.append(str(file))
    for file in glob.glob(path + '**/*', recursive=True):
        if os.path.isdir(file) == True:
            if  os.path.isfile(file + '/README.md') == True:
                file = glob.glob(file + '/*.json', recursive=True)
                ages.append(str(file))
    return ages

def step3(jsonFile):
    f = open(jsonFile)
    presidents = json.load(f)

    ages = 0
    count = 0
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages += age
        count += 1
    return ages / count
def getAverage():
    path = '/Users/luka0725/17950_CraftingSoftware/in-class-2022/jan-27-paths/presidents.json'
    list = getJson()
    averageAges = 0
    count = 0
    for jsonFile in list[:]:
        averageAges += step3(jsonFile)
        count += 1
        return averageAges / count

print(getAverage())
