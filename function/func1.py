def graph(companyname,values):
    print(companyname,":",end= '')
    for i in range(1,values+1):
        print("#",end = '')
    print(values,"%")    

def add(a,b):
    c = a+b
    return c 

def max(a,b):
    if a>b:
        return a
    else:
        return b 
def table(a):
    for i in range(1,11):
        print(a,"X",i,"=",a*i) 

def length(s):
    c=0
    for e in s:
        c = c+1
    return c
def vowels(a):
    c = 0
    for e in a:
        if e in "aeiou":  #or e == "a" or e == e" or e == "i" or e == "o" or e == "u":
            c = c+1
    return c        
def AD(a,b):
    d = a+b
    f = a-b
    return d,f

def travel(kms):
    c1 = kms *8
    c2 = kms *12
    return c1,c2

graph("tata",95)
graph("A",40)        
graph("B",65)
graph("C",10)
graph("D",58)
graph("E",35)


result  = add(50,60)
print("SUM = ",result)

x = input("enter the first number")
y = input("enter the second number")
z = input("enter the third number")

v = max(x,y)
w = max(v,z)
print(w)

print("Largest = ",max(max(x,y),z))

table(3)


print(length("hello"))
print(length("gourav govil r"))

print(vowels("gourav"))
print(vowels("vrtyhjk"))

p,q = AD(50,40)
print("sum = ",p)
print("difference = ",q)

f,o = travel(450)
print("travel through first car",f)
print("travel through second car",o)