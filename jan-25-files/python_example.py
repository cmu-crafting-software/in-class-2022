import json
import csv
from datetime import datetime
def printYears():
    f = open("constitutional_amendments.json")
    amendments = json.load(f)
    for amendment in amendments :
        ratifiedDate = datetime.strptime(amendment['Ratified'], '%m/%d/%Y')
        print (ratifiedDate.year)
    for amendment in amendments :
        print(amendment['Ratified'])        
printYears()    
def printNumbersCSV():
    with open('constitutional_amendments.csv') as csvfile:
        amendments = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(amendments)
        for amendment in amendments :
            print(amendment[1])