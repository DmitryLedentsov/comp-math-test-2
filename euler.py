from math import *
f = lambda x,y: y+(1+x)*y*y
a = 1
b = 1.5
h = 0.1
x0 = 1
y0 = -1

def dir(function, h = 0.000000001):
    return lambda x: (function(x+h) - function(x-h)) / (2*h)

D= 3
def euler(f, a, b, y0, h):
    print("ЭЙЛЕР")
    dots = [(a, y0)]
    n = int((b - a) / h)
    print(f'| i | x_i   |    y_i |   f_i |')
    f_i = round(f(a,y0),D)
    print(f'| 0 | {a:^.3f} | {y0:>.3f} | {f_i:<.3f} |')
    for i in range(1, n + 1):

       
        x_i = dots[i - 1][0] + h
        y_i = dots[i - 1][1] + h * f_i
        f_i = f(x_i,y_i)
        print(f'| {i:1} | {x_i:^.3f} | {y_i:>.3f} | {f_i:<.3f} |')
        dots.append((round(dots[i - 1][0] + h,D),
                     round(dots[i - 1][1] + h * f(dots[i - 1][0], dots[i - 1][1]),D)))

    return dots
euler(f,a,b,y0,h)
