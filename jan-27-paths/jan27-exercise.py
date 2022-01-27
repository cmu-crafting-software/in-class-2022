import os
import glob

os.getcwd()
os.chdir('musicians/rock')


files = glob.glob('**/*.json', recursive=True)
print(files)