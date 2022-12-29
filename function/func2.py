def add(a, b, e, c=0):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("e = ", e)
    d = a+b+c+e
    return d


def date(d, m, y, s="-"):
    print(d, s, m, s, y)


def addcontact(name, mobile, country='+91'):
    print("-"*30)
    print("name = ", name)
    print("mobile = ", mobile)
    print("countrycode = ", country)

    print("-"*30)


def interest(amount, time, interest=8.5):
    SI = (amount*time*interest)/100
    return SI

def add(*p):
    s= 0               # if we give *p as an argument we can give number of arguments we want to give it stores in the form tuple("Python Tuple is a collection of objects separated by comma")
    for e in p:
        s = s+e
    return s    

print("sum is", add(10, 20, 40))
print("sum is", add(10, 20, 30, 40))

date(21, 9, 2002)
date(25, 11, 2020, "/")

addcontact("gourav", "6362458547")
addcontact("robert downey junior(RDJ)(IRONMAN)", "6362458548", "+044")


amount = int(input("enter loan amount"))
time = int(input("enter how many  year"))


print("1.calculate on normal interest basics")
print("2.caluculate on consideration interest bascis")
    
ch = int(input("enter your choice"))
if ch == 1:
  print("Interest =", interest(amount, time))
elif ch == 2:
    r = eval(input("enter interest"))
    print("interest = ", interest(amount, time, r))


print(add(10,20))
print(add(10,20,30,40,50)) 
print(add(10,20,36,25,14,74,25,63))      
    
