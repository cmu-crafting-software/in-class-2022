import json
import csv
import datetime
from datetime import date
from datetime import datetime
def _file_reader(file): 
    with open(file) as f:
        data = json.load(f)
        print(data)

    ages = []
    i = 0
    while i <= len(data)-1:
        birthdate = datetime.strptime(data[i]['DOB'], '%Y-%m-%d')
        days_in_year = 365 
        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) <  (birthdate.month, birthdate.day) :
            age = age - 1
        ages.append(age)
        i += 1
    return ages     
print(_file_reader('presidents.json'))


