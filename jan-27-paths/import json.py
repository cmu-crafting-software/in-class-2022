import json
from datetime import datetime

def add():
    f = open("presidents.json")
    presidents = json.load(f)

    presidents.append("Barack Obama")

    print(presidents)

add()


    

   

