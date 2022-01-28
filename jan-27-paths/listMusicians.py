import glob
import os

os.getcwd
os.chdir('musicians')
os.getcwd
os.listdir



files = glob.glob('**/*.csv', recursive=True)
filesJson = glob.glob('**/*.json', recursive=True)


print(files)
print(filesJson)
