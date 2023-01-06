n = int(input("enter a number"))


f = open("sum1.txt", "w")

for i in range(1, 11):
    msg = "{0} + {1} = {2}\n".format(n, i, n+i)
    f.write(msg)
f.close() 


n = int(input("enter a number"))


f = open("mutiplication.txt", "w")

for i in range(1, 11):
    msg = "{0} X {1} = {2}\n".format(n, i, n*i)
    f.write(msg)
f.close() 


