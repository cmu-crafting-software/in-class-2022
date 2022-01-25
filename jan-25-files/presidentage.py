# -*- coding: utf-8 -*-
import json
#import csv

from datetime import datetime

def printYears():
    f = open("presidents.json")
    presidents = json.load(f)

    for president in presidents :
        birthday = datetime.strptime(president['DOB'], '%Y-%m-%d')
        print(2020-birthday.year)



printYears()