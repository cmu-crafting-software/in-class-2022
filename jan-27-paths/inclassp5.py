import glob
import os
import json
from datetime import datetime



def step3(path1,path2):
    f1 = open(path1)
    f2 = open(path2)
    presidents = json.load(f1)
    musicians = json.load(f2)

    ages = []
    agesum = 0
    for president in presidents :
        dob = datetime.strptime(president['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
        agesum = agesum + age

    for musician in musicians :
        dob = datetime.strptime(musician['DOB'], '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year
        if (today.month, today.day) <  (dob.month, dob.day) :
            age = age - 1
        ages.append(age)
        agesum = agesum + age

    return agesum/len(ages)

#part 5
os.chdir('musicians/rock')
path = os.getcwd()
dir_list = os.listdir(path)
print(dir_list)

#part 6
print(os.getcwd())
path_parent = os.path.dirname('/Users/Taryn/Documents/CMUPhD/Classes/Year2/Spring2022/CraftingSoftware/InClass/in-class-2022/jan-27-paths/musicians')
os.chdir(path_parent)
print(os.getcwd())
files = glob.glob('**/*.json', recursive=True)#searches for files that have .csv
print(files)

print(step3(files[0],files[1]))


