from math import *

#менять тута
data = \
'''
1 3 5 7 9
5.4 10.3 17.2 20.8 25.1
'''
x0 = 2.5#7.93
#выбрать нужный после lambda
get_method = lambda: gau
#x = "1.1 2.3 3.7 4.5 5.4 6.8 7.5"
#y = "2.73 5.12 7.74 8.91 10.59 12.75 13.43"
data = data.replace(",",'.')
data = data.splitlines()
x = data[1]
y = data[2]
X = [float(i) for i in x.split(" ")]
Y = [float(i) for i in y.split(" ")]

N = len(X)
print("вход:")
print(X)
print(Y)
print("решение:")

dots = [(X[i],Y[i]) for i in range(N)]
def lag(dots, x):
    """ Многочлен Лагранжа """
    result = 0

    n = len(dots)
    for i in range(n):
        c1 = c2 = 1
        for j in range(n):
            if i != j:
                c1 *= x - dots[j][0]
                c2 *= dots[i][0] - dots[j][0]
        l = dots[i][1] * c1 / c2
        print(f"l_{i} = {c1:.6f}/{c2:.6f}*{dots[i][1]}={l:.6f}")
        result += l

    return result


def t_calc_nwt(t, n, forward=True):
    """ Вычислить параметр 't' для многочлена Ньютона """
    result = t

    for i in range(1, n):
        if forward:
            result *= t - i
        else:
            result *= t + i

    return result

def t_calc_gau(t, n, forward=True):
    """ Вычислить параметр 't' для многочлена Гаусса """
    result = t

    for i in range(1, n):
        if forward:
            if(i % 2 == 0):
              result *= (t - int((i+1)/2))
            else:
              result *= (t + int((i+1)/2))
        else:
            if(i % 2 == 1):
              result *= (t - int((i+1)/2))
            else:
              result *= (t + int((i+1)/2))
    return result


def add_column(data,last):
    for i in range(len(data)):
        row = data[i]
        # Now add the new column to the current row
        row.insert(0,last[i])
def fmt_table(matrix):
    s = [[str(round(e,4)) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))

def nwt(dots, x):
    """ Многочлен Ньютона с конечными разностями """
    n = len(dots)
    h = dots[1][0] - dots[0][0]
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][0] = dots[i][1]

    for i in range(1, n):
        for j in range(n - i):
            a[j][i] = a[j + 1][i - 1] - a[j][i - 1]
    

    print(f'i       x_i     dy_i     ... deltas')
    #####################
    table  = list(map(list, a))
    add_column(table,X)
    add_column(table,[i for i in range(N)])
    fmt_table(table)
    #####################
    if x <= dots[n // 2][0]:
        # Первая интерполяционная формула Ньютона
        x0 = n - 1
        for i in range(n):
            if x <= dots[i][0]:
                x0 = i - 1
                break
        if x0 < 0:
            x0 = 0
        t = (x - dots[x0][0]) / h
        print("t = ", t)
        result = a[x0][0]
        for i in range(1, n):
            result += (t_calc_nwt(t, i) * a[x0][i]) / factorial(i)
    else:
        # Вторая интерполяционная формула Ньютона
        t = (x - dots[n - 1][0]) / h
        print("t = ", t)
        result = a[n - 1][0]
        for i in range(1, n):
            result += (t_calc_nwt(t, i, False) * a[n - i - 1][i]) / factorial(i)

    return result


def gau(dots, x):
    """ Многочлен Ньютона с конечными разностями """
    n = len(dots)
    h = dots[1][0] - dots[0][0]
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][0] = dots[i][1]

    for i in range(1, n):
        for j in range(n - i):
            a[j][i] = a[j + 1][i - 1] - a[j][i - 1]
    

    print(f'i       x_i     dy_i     ... deltas')
    #####################
    table  = list(map(list, a))
    add_column(table,X)
    add_column(table,[i for i in range(N)])
    fmt_table(table)
    #####################
    if x <= dots[n // 2][0]:
        # вторая интерполяционная формула Гаусса
        x0 = n - 1
        for i in range(n):
            if x <= dots[i][0]:
                x0 = i - 1
                break
        if x0 < 0:
            x0 = 0
        
        t = (x - dots[int(n / 2)][0]) / h
        print("t = ", t)
        result = dots[n//2][1]
        for i in range(1, n):
            print("cur delta: ",a[int((n - i) / 2) + (i % 2 == 0)-1][i])
            
            result += (t_calc_gau(t, i) * a[int((n - i) / 2) + (i % 2 == 0)-1][i]) / factorial(i)
            print("cur res: ", result)
    else:
        # первая интерполяционная формула Гаусса
        t = (x - dots[int(n / 2)][0]) / h
        print("t= ",t)
        result = dots[n//2][1]
        for i in range(1, n):
            print("cur delta: ", a[int((n - i) / 2)][i])
            result += (t_calc_gau(t, i, False) * a[int((n - i) / 2)][i]) / factorial(i)
            print("cur res: ", result)
    return result

print("РЕЗУЛЬТАТ:", get_method()(dots, x0))