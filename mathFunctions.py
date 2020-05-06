import math

#math is a module in python libraries
#we can also replace usage of math by changing the way we import like 
#import math as m then instead of math.sqrt(x) we can use m.qrt(x) or can use in both ways when implemented this way.
#if you want to use only few operations we can import as like "from math import sqrt,pow"
x=15
y=math.sqrt(x)
print('The square root of x = ',y)
print('floor value = ',math.floor(y))
print('ceil value = ',math.ceil(y))
print('power value = ',math.pow(2,4))
print('value of PI',math.pi)
print('value of Epsilon', math.e)

