#!/usr/bin/env python3

import json
from datetime import datetime



def step4():
    f = open("presidents.json")
    presidents = json.load(f)
    presidents.sort(key = lambda x: x['BirthState'])

    for president in presidents :
        print(president['BirthState']+": "+ president['Last']+", "+president['First'])

step4()