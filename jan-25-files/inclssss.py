import json
import csv
from datetime import datetime
def _file_reader(file): 
    with open(file) as f:
        data = json.load(f)
        print(data)

_file_reader('presidents.json')
