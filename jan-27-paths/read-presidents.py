import json
import csv

from datetime import datetime


f = open("presidents.json")
presidents = json.load(f)

avAge = 0
now = datetime.now()
for prez in presidents:
    avAge += (now - datetime.strptime(prez["DOB"], '%Y-%m-%d')).days

avAge = avAge/len(presidents)
print(str(round(avAge/365.25)) + ' years')

presidents.append({
    "First": "William ",
    "Last": "Harrison",
    "DOB": "1779-02-09"
  })


presidents[0]['Birth State'] = 'Pennsylvania'
presidents[1]['Birth State'] = 'New York'
presidents[2]['Birth State'] = 'Hawaii'
presidents[3]['Birth State'] = 'Connecticut'
presidents[4]['Birth State'] = 'Arkansas'
presidents[5]['Birth State'] = 'Georgia'
presidents[6]['Birth State'] = 'Virginia'

sortedPresidents = sorted(presidents, key = lambda prez : prez['Birth State'])
print(sortedPresidents)