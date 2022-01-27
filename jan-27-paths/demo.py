import os
import glob

print(os.getcwd())

os.chdir('jan-27-paths')
files = glob.glob('**/*.csv', recursive=True)
print(files)