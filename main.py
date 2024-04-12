import csv
import os
import tabulate
b=[]
working_board=None
path=os.getcwd()
def boards():
    b.clear()
    for dir in os.listdir(path):
        if os.path.isdir(dir):
            b.append(dir)