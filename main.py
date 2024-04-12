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
def add_board():
         name=input("Enter board name \n>>").strip()
         if name in b:
              print("Board Already Exists !!!")
              return
         else:
              os.mkdir(name)
              b.append(name)