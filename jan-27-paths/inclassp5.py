import glob
import os

path = os.getcwd()
files = glob.glob('**/*.csv', recursive=True)
print(files)
os.chdir('musicians/rock')
files = glob.glob('**/*.csv', recursive=True)
print(files)