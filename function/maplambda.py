cost = []
for i in range(0,5):
 n = int(input("enter the cost"))
 cost.append(n)

gst =list(map(lambda x:x+x*0.12,cost)) 
print(gst)

in1marks = []
m = int(input("enter no of students"))
print("enter the marks of first internals")
for h in range(0,m):
   in1marks.append(int(input()))

in2marks = []
print("enter the marks of second internals")
for h in range(0,m):
   in2marks.append(int(input())) 

in3marks = []
print("enter the marks of third internals")
for h in range(0,m):
   in3marks.append(int(input()))      

avg = list(map(lambda x,y,z:(x+y+z)/2,in1marks,in2marks,in3marks))

print(avg)

working_days = [20,15,15,25,32]
attendence = [12,15,9,21,28]

present_attendence = list(map(lambda x,y:(y/x)*100,working_days,attendence))

print(present_attendence)