import os 
import glob
os.chdir("jan-27-paths")
files_= glob.glob('**/*.csv', recursive=True)
print(files_)