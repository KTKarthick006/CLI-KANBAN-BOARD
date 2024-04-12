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
def rm_board(): #remove board
        for i,board in enumerate(b):
            print(f"{i+1}. {board}")
        choice=int(input("Enter Board Number \n>>"))
        if choice>len(b):
            print("Enter valid choice !!!")
            return
        for file in os.listdir(b[choice-1]):
            os.remove(os.path.join(b[choice-1],file))
        os.rmdir(b[choice-1])
def init(): #initialize
        files=["todo.csv","done.csv","inprogress.csv","queued.csv","waiting.csv"]
        for file in files:
            if not os.path.exists(os.path.join(path,file)):
                with open(file,"w") as f:
                    pass
def name_parser(): #name parser
        usr=input("Enter Names split by comma\n>>")
        names=[]
        for name in usr.split(","):
            names.append(name.strip())
        return names
def add():
    print("1. ToDo")
    print("2. In Progress")
    print("3. Queued")
    print("4. Waiting")
    print("5. Done")
    choice=int(input("Enter type of task\n>>"))-1
    files=["todo.csv","inprogress.csv","queued.csv","waiting.csv","done.csv"]
    if choice+1>len(files):
        print("Enter valid choice !!!")
        return
    file=os.path.join(path,files[choice])
    task=input("Enter Task Name\n>>")
    print("Assignees:")
    assign=name_parser()
    print("Report")
    report=name_parser()
    print("Priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    priority=int(input("Enter Priority\n>>"))
    with open(file,"r")as f:
        task_id=f"F{choice}-"+str(len(list(csv.reader(f)))+1)
    with open(file,"a") as f:
        writer=csv.writer(f)
        writer.writerow([task_id,task,assign,report,priority])
def pr(i):
    if i == 1:
        return "High"
    elif i==2:
        return "Medium"
    elif i==3:
        return "Low"
def ft(i):
    nbr=int(i.pop())
    p=pr(nbr)
    i.append(p)
    return i
def ls():
    files=["todo.csv","done.csv","inprogress.csv","queued.csv","waiting.csv"]
    for file in files:
        print(f"\n\n{file.capitalize()}\n{'_'*35}\n")
        with open(file,"r") as f:
            reader=csv.reader(f)
            table=[]
            for i in reader:
                table.append(ft(i))
            print(tabulate.tabulate(table,headers=['Task Id','Task Name','Assignees','Reporters','Priority'],tablefmt="fancy_grid"))
def rmv():
    ls()
    id=input("Enter Task ID to delete\n>>")
    files=["todo.csv","inprogress.csv","queued.csv","waiting.csv","done.csv"]
    file=int(id[1])

    with open(files[file],"r") as f:
        reader=csv.reader(f)
        old=list(reader)
    new=[]
    i=1
    for j in old:
        if j[0]==id:
            continue
        j[0]=f"F{file}-{i}"
        new.append(j)
        i+=1
    with open(files[file],"w") as f:
        writer=csv.writer(f)
        writer.writerows(new)
        
def mv():
    ls()
    id=input("Enter Task ID to change status\n>>")
    files=["todo.csv","inprogress.csv","queued.csv","waiting.csv","done.csv"]
    file=int(id[1])
    print("1. ToDo")
    print("2. In Progress")
    print("3. Queued")
    print("4. Waiting")
    print("5. Done")
    choice=int(input("Enter new status for the task\n>>"))-1
    with open(files[file],"r") as f:
        reader=csv.reader(f)
        old=list(reader)
    print(old)
    new=[]
    i=1
    for j in old:
        if j[0]==id:
            popped=j
            continue
        j[0]=f"F{file}-{i}"
        new.append(j)
        i+=1
    with open(files[file],"w") as f:
        writer=csv.writer(f)
        writer.writerows(new)
    if choice+1>len(files):
        print("Enter valid choice !!!")
        return
    file_new=os.path.join(path,files[choice])
    with open(file_new,"r")as f:
        task_id=f"F{choice}-"+str(len(list(csv.reader(f)))+1)
    popped[0]=task_id
    with open(file_new,"a") as f:
        writer=csv.writer(f)