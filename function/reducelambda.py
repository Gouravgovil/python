from functools import reduce

a = [25,63,221,78,17]

add = reduce(lambda x,y:x+y,a)

print(add)

from functools import reduce

a = [25,63,221,78,17]

multiply = reduce(lambda x,y:x*y,a)

print(multiply)