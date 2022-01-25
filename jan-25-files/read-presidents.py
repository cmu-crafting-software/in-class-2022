import json
import csv

from datetime import datetime
from datetime import date

now = datetime.now()

f = open("presidents.json")
presidents = json.load(f)
avAge = 0
for prez in presidents:
    avAge += (now - datetime.strptime(prez["DOB"], '%Y-%m-%d')).days

avAge = avAge/len(presidents)
print(str(round(avAge/365.25)) + ' years')
presidents.append({
    "First": "William ",
    "Last": "Harrison",
    "DOB": "1779-02-09"
  })