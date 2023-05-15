from math import *
f = lambda x,y: y+(1+x)*y*y
a = 1
b = 1.5
h = 0.1
x0 = 1
y0 = -1
def coef(x,y):

    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    print(f"x = {x:.3f}")
    print(f"y = {y:.3f}")
    print(f"f({x:.3f}, {y:.3f}) = {f(x,y):.3f}")
    print(f"k1 = {h:.3f}*f({x:.3f}, {y:.3f}) =  {k1:.3f}")
    print(f"k2 = {h:.3f}*f({x:.3f} + {h/2:.3f}, {y:.3f}+k1/2) = {k2:.3f}")
    print(f"k3 = {h:.3f}*f({x:.3f} + {h/2:.3f}, {y:.3f}+k2/2) = {k3:.3f}")
    print(f"k4 = {h:.3f}*f({x:.3f} + {h:.3f}, {y:.3f}+k3) = {k4:.3f}")
    #print(f"{k1:.3f},{k2:.3f},{k3:.3f},{k4:.3f}")
    ny = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    print(f"y_i+1 = {ny:.3f}")
    print()
    return ny


y = coef(x0,y0)
x = x0+h
x,y = round(x,3), round(y,3)
i = 0
while x<=b:

    y = coef(x,y)
    x+=h
    x,y = round(x,3), round(y,3)
    

