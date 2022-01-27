import glob
import os


def step5():
    print(os.getcwd())
    os.chdir('musicians/rock')
    files = os.listdir()
    for f in files:
        print(f)

def computeAverageAge(str[] paths):
    ages = []
    


def step6():
    print(os.getcwd())
    files = glob.glob('**/*.csv', recursive=True)
    print(files)

step5()