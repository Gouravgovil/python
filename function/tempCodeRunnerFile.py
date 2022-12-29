values = []

for i in range(1,11):
    val = int(input("enter the cost"))
    values.append(val)

v = list(filter(lambda x:x<500,values))
print(v)