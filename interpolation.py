
from math import *

#менять тута
data = \
'''
0,1 0,2 0,3 0,4 0,5
1,25 2,38 3,79 5,44 7,14
'''
x0 = 0.15
#выбрать нужный после lambda
get_method = lambda: nwt
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


def t_calc(t, n, forward=True):
    """ Вычислить параметр 't' для многочлена Ньютона """
    result = t

    for i in range(1, n):
        if forward:
            result *= t - i
        else:
            result *= t + i

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

        result = a[x0][0]
        for i in range(1, n):
            result += (t_calc(t, i) * a[x0][i]) / factorial(i)
    else:
        # Вторая интерполяционная формула Ньютона
        t = (x - dots[n - 1][0]) / h

        result = a[n - 1][0]
        for i in range(1, n):
            result += (t_calc(t, i, False) * a[n - i - 1][i]) / factorial(i)

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
        # Первая интерполяционная формула Ньютона
        x0 = n - 1
        for i in range(n):
            if x <= dots[i][0]:
                x0 = i - 1
                break
        if x0 < 0:
            x0 = 0
        t = (x - dots[x0][0]) / h

        result = a[x0][0]
        for i in range(1, n):
            result += (t_calc(t, i) * a[x0][i]) / factorial(i)
    else:
        # Вторая интерполяционная формула Ньютона
        t = (x - dots[n - 1][0]) / h

        result = a[n - 1][0]
        for i in range(1, n):
            result += (t_calc(t, i, False) * a[n - i - 1][i]) / factorial(i)

    return result

def fin_dif(Y):
    n = len(Y)
    matrix =  [[0] * n for _ in range(n)]
    for i in range(len(Y)):
        matrix[i][0] = Y[i]
    for j in range(len(Y)):
        for i in range(len(Y)):
            if i + j <= (int(len(Y)) - 1) and j != 0:
                matrix[i][j] = matrix[i + 1][j - 1] - matrix[i][j - 1]
    fmt_table(matrix)
    return matrix
def gaum( X, x):
    summ = 0
    matrix = fin_dif(Y)
    if x <= X[int(len(X) / 2)]:
        factor = 1
        t = (x - X[int(len(X) / 2)]) / (X[1] - X[0])
        
        for i in range(len(X)):
            summ = summ + matrix[int((len(X) - i) / 2) - (len(X) % 2 == 0)][i] * factor / factorial(i)
            factor = factor * (t - i)
    else:
        factor = 1
        t = (x - X[int(len(X) / 2)]) / (X[1] - X[0])
        for i in range(len(X)):
            summ = summ + matrix[int((len(X) - i) / 2)][i] * factor / factorial(i)
            factor = factor * (t + (-1) ** i * i)
    return summ
print(gaum(X,x0))
print(get_method()(dots, x0))