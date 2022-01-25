import json
from datetime import datetime

def averageAge():
    file = open("presidents.json")
    presidents = json.load(file)

    total_age = 0
    number = 0

    for president in presidents:
        date_of_birth = datetime.strptime(president['DOB'],'%Y-%m-%d')
        age = 2022 - date_of_birth.year
        total_age = total_age + age
        number = number + 1
    
    print(number)
    print(total_age/number)
    


averageAge()
