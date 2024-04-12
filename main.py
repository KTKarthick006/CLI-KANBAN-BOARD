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
def use_board():
        global working_board , path
        for i,board in enumerate(b):
            print(f"{i+1}. {board}")
        choice=int(input("Enter Board Number \n>>"))
        if choice>len(b):
            print("Enter valid choice")
        working_board=b[choice-1]
        path=os.path.join(os.getcwd(),working_board)
        os.chdir(path)