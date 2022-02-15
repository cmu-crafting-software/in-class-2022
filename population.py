import requests

r = requests.get('https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP&in=state:42&for=county:003&AGEGROUP=19')
print(r.json())