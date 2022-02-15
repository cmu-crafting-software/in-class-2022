import os
import glob

files = glob.glob('**/*.csv', recursive=True) #searches working directory that has a file with any name but filetype .csv
print(os.getcwd()) #prints current working directory
#os.chdir('pathname') used to change directory
print(files)