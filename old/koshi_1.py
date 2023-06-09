a = 1
b = 1.5

h = 0.1
x0=1
y0=-1
def dir(function, h = 0.000000001):
    return lambda x: (function(x+h) - function(x-h)) / (2*h)

f = lambda x,y:  y+(1+x)*(y*y)

def euler(f, a, b, y0, h):
    """ Метод Эйлера """
    dots = [(a, y0)]
    n = int((b - a) / h)
    print(f'| i | x_i   |    y_i |   f_i |')
    print(f'| 0 | {a:^.3f} | {y0:>.3f} | {f(a,y0):<.3f} |')
    for i in range(1, n + 1):

        f_i = f(dots[i - 1][0], dots[i - 1][1])
        x_i = dots[i - 1][0] + h
        y_i = dots[i - 1][1] + h * f_i
        print(f'| {i:1} | {x_i:^.3f} | {y_i:>.3f} | {f_i:<.3f} |')
        dots.append((dots[i - 1][0] + h,
                     dots[i - 1][1] + h * f(dots[i - 1][0], dots[i - 1][1])))

    return dots

def mod_euler(f, a, b, y0, h):
    points = list()
    points.append((a, y0))
    for i in range(1, int((b - a) / h) + 1):
        x = points[i - 1][0] + h
        y = points[i - 1][1] + h / 2 * (f(points[i - 1][0], points[i - 1][1]) + f(points[i - 1][0] + h, points[i - 1][1] + h * f(points[i - 1][0], points[i - 1][1])))
        points.append((x, y))
    return points

def runge_next(func, x, y, h):
    k1 = h * func(x, y)
    k2 = h * func(x + h / 2, y + k1 / 2)
    k3 = h * func(x + h / 2, y + k2 / 2)
    k4 = h * func(x + h, y + k3)
    return y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

def runge(func, x_0, y_0, h, b, e):
    y_prev = y_0
    y_current = 0
    answer_x = [x_0]
    answer_y = [y_0]
    x_prev = x_0
    y_current_h_div_2 = y_0 * 1000 + 10000
    print("h    y_h    y_h/2")
    while (abs(y_current_h_div_2 - y_current) > e):
        y_current = runge_next(func, x_prev, y_prev, h)
        y_current_h_div_1 = runge_next(func, x_prev, y_prev, h/2)
        y_current_h_div_2 = runge_next(func, x_prev + h/2, y_current_h_div_1, h/2)
        print(h, y_current, y_current_h_div_2, )
        h /= 2

    h *= 2

    while x_prev < b:
        y_current = runge_next(func, x_prev, y_prev, h)

        answer_y.append(y_current)
        answer_x.append(x_prev + h)
        x_prev += h
        y_prev = y_current
    return list(zip(answer_x, answer_y))

euler(f,a,b,y0,h)

print(runge(f,x0,y0,h,b,0.01))