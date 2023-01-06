from datetime import datetime  
from datetime import timedelta

def add():
    name=input("Enter donar name = ")
    blood = input("Enter blood group = ").upper()
    age = input("Enter age = ")
    
    ch = input("Have you donated blood earlier ?")
    if ch=='y' or ch=='Y':
        prev = input("Enter last donated date =")
    else:
        prev = str(datetime.now().date())
        
    f = open("bloodbank.txt","a")
    data = "{0},{1},{2},{3}\n".format(name,blood,age,prev)
    f.write(data)
    f.close()
    
    
def search():
    blood = input("Enter blood group = ").upper()
    f = open("bloodbank.txt","r")
    recs = f.readlines()
    f.close()
    
    L=list(filter(lambda x:x.split(',')[2]==blood , recs))
    
    for e in L:
        e = e.strip()
        d = e.split(',')[3].split('-')
        LD = datetime(day=int(d[0]) , month=int(d[1]) , year=int(d[2]))
        CD = datetime(datetime.now().date().year,datetime.now().date().month,datetime.now().date().day)
        
        days = str(CD - LD)
        days = int(days.split(' ')[0])

        #print("Days = " ,days)
        if days > 90:
            print(e)


def listall():

    f = open("bloodbank.txt","r")
    recs = f.readlines()
    f.close()
    
    for e in recs:
        e = e.strip()
        print(e)


while True:
    print("1.NEW DONOR DETAILS")
    print("2.search for blood group")
    print("3.list all the blood group")
    print("4.exit")
    ch = int(input("enter your choice\n"))

    if ch == 1:
        add()
    elif ch == 2:
        search()
    elif ch == 3:
        listall()
    elif ch == 4:
        break
