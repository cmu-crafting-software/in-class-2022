import json
import csv
import os
import glob

from datetime import datetime

alljson = glob.glob('.','*.json',recursive=True)

print(alljson)