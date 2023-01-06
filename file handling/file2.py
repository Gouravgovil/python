cur = int(input("enter the current income"))
prev =int(input("enter the previous income"))


if cur >prev:
    result = "invest in this comapany"

else:
    result = "don't invest in this comapany wait for somemore time"

f = open("stock.txt","w")

f.write(result)
f.close()
