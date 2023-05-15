from math import *
a = 1
b = 1.5

h = 0.1
x0=1
y0=-1
def dir(function, h = 0.000000001):
    return lambda x: (function(x+h) - function(x-h)) / (2*h)

xi = x0
yi = y0
for xi in range(x0,b,h):
    print("x = ", x)
    yi