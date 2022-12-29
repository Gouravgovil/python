inmarks = []
n = int(input("enter the number of students"))


print("enter the internal marks")
for  i in range(0,n):
   inmarks.append(int(input()))

extmarks = []
print("enter the external marks")
for i in range(0,n):
    extmarks.append(int(input()))

res = list(map(lambda x,y:x+y,inmarks,extmarks))
failed = list(filter(lambda x:x<35,res))

marksneeded  = list(map(lambda x: 35-x,failed))

print("internal marks awarded is",inmarks)
print("enternal marks awarded is",extmarks)
print("add os internalmarks and externalmarks",res)
print("students those who got below 35",failed)
print("marks needed to get pass",marksneeded)
