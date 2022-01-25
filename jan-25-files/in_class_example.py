# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:52:55 2022

@author: jacks
"""

import json
import csv
from datetime import datetime
import mean()
def printAges():
        f = open("presidents.json")
        ages = []
        DOBs = json.load(f)
        for DOB in DOBs :
            BirthDate = datetime.strptime(DOB['DOB'], '%Y-%m-%d')
            years = BirthDate.year
            age = 2022 - years
            print(age)
            ages.append(age)
            avgAge = mean(ages)
            print(avgAge)
printAges()
#         ratifiedDate = datetime.strptime(amendment['Ratified'], '%m/%d/%Y')
#         print (ratifiedDate.year)
    # for amendment in amendments :
    #     print(amendment['Ratified'])