from math import *

#менять тута
data = \
'''
1.1 2.3 3.7 4.5 5.4 6.8 7.5
2.73 5.12 7.74 8.91 10.59 12.75 13.43
'''
#выбрать нужный после lambda
get_method = lambda: lna
#x = "1.1 2.3 3.7 4.5 5.4 6.8 7.5"
#y = "2.73 5.12 7.74 8.91 10.59 12.75 13.43"
data = data.splitlines()
x = data[1]
y = data[2]
x = [float(i) for i in x.split(" ")]
y = [float(i) for i in y.split(" ")]
N = len(x)
print("вход:")
print(x)
print(y)

def get_wolphram():
    s = "fit "
    s+= "{"
    for i in range(N):
        s+= "{" + f"{x[i]},{y[i]}" + "},"
    s = s[:-1]
    s+= "}"
    return s

#решение СЛАУ методом Гаусса-Зейделя
def calc_system(array, n):
    max_iterations = 100000
    epsilon = 0.00001
    vector_old_ans = [0] * n
    vector_ans = [0] * n
    difference = epsilon + 1
    num = 0
    found_answer = True
    errors = [0] * n

    while difference > epsilon:
        for i in range(n):
            sum = 0
            for j in range(n):
                if i != j:
                    sum += array[i][j] / array[i][i] * vector_ans[j]
            vector_ans[i] = array[i][n] / array[i][i] - sum
        for i in vector_ans:
            if i == None or i == inf or i == -inf:
                print("Значения расходятся, невозможно найти ответ")
                found_answer = False
                exit(0)

        max_difference = 0.0
        for i in range(n):
            if abs(vector_old_ans[i] - vector_ans[i]) > max_difference:
                max_difference = abs(vector_old_ans[i] - vector_ans[i])
        difference = max_difference
        for i in range(n):
            vector_old_ans[i] = vector_ans[i]
        num += 1
        if (num >= max_iterations):
            print("Не удалось получить ответ за максимальное количество итераций")
            found_answer = False
            break
    return vector_ans

def qerror(f):
    errs = [(f(x[i]) - y[i])**2 for i in range(N)]
    #print("ошибки: ", errs)
    #print("отклонение S: ", sum(errs))
    mid_err = sqrt(sum(errs)/N)
    print("ср.кв.отклонение : ", mid_err)

def lina():
    SX = x
    SXX = [xi**2 for xi in x]
    SY = y
    SXY = [x[i]*y[i] for i in range(N)]
    print("расчеты:")
    print("SX: ",[round(i, 3) for i in SX], "сумм: ", round(sum(SX), 3))
    print("SXX: ",[round(i, 3) for i in SXX], "сумм: ", round(sum(SXX), 3))
    print("SY: ",[round(i, 3) for i in SY], "сумм: ", round(sum(SY), 3))
    print("SXY: ",[round(i, 3) for i in SXY], "сумм: ", round(sum(SXY), 3))
    SX = sum(SX)
    SXX = sum(SXX)
    SY = sum(SY)
    SXY = sum(SXY)
    print("итоговая система, подставить в фотомас:")
    print(f"{SXX} a  + {SX} b = {SXY}")
    print(f"{SX} a + {N} b = {SY}")
    print()
    ans = calc_system([[SXX, SX, SXY],[SX, N, SY]], 2)
    result_func = lambda x: ans[0]*x + ans[1]
    str_result_func = f"{round(ans[0], 3)}x + {round(ans[1], 3)}"
    print("ф-ция: ",str_result_func)
    return result_func

def powa():
    nx = []
    ny = []

    #добавляем в массив только те точки, которые подходят по ОДЗ логарифма
    for i in range(N):
        if x[i] > 0 and y[i] > 0:
            nx.append(x[i])
            ny.append(y[i])
    if(len(nx)!= N or len(ny)!=N):
        print("ВНИМАНИЕ! часть точек утрачена")
    n = len(nx)
    SX = [log(nx[i]) for i in range(n)]
    SXX = [log(nx[i])**2 for i in range(n)]
    SY  = [log(ny[i]) for i in range(n)]
    SXY = [log(ny[i])*log(nx[i]) for i in range(n)]

    print("расчеты:")
    print("SX: ",[round(i, 3) for i in SX], "сумм: ", round(sum(SX), 3))
    print("SXX: ",[round(i, 3) for i in SXX], "сумм: ", round(sum(SXX), 3))
    print("SY: ",[round(i, 3) for i in SY], "сумм: ", round(sum(SY), 3))
    print("SXY: ",[round(i, 3) for i in SXY], "сумм: ", round(sum(SXY), 3))
    SX = sum(SX)
    SXX = sum(SXX)
    SY = sum(SY)
    SXY = sum(SXY)

    print("итоговая система, подставить в фотомас:")
    print(f"{SXX} a  + {SX} b = {SXY}")
    print(f"{SX} a + {n} b = {SY}")
    print()
    ans = calc_system([[SXX, SX, SXY],[SX, n, SY]], 2)
    result_func = lambda x: exp(ans[1])*(x ** ans[0])
    str_result_func = f"{round(exp(ans[1]), 3)}x^{round(ans[0], 3)}"
    print("ф-ция: ",str_result_func)
    return result_func

def expa():
    nx = []
    ny = []

    #добавляем в массив только те точки, которые подходят по ОДЗ логарифма
    for i in range(N):
        if y[i] > 0:
            nx.append(x[i])
            ny.append(y[i])
    if(len(nx)!= N or len(ny)!=N):
        print("ВНИМАНИЕ! часть точек утрачена")
    n = len(nx)
    SX = [i for i in nx]
    SXX = [i**2 for i in nx]
    SY  = [log(i) for i in ny]
    SXY = [nx[i]*log(ny[i]) for i in range(n)]

    print("расчеты:")
    print("SX: ",[round(i, 3) for i in SX], "сумм: ", round(sum(SX), 3))
    print("SXX: ",[round(i, 3) for i in SXX], "сумм: ", round(sum(SXX), 3))
    print("SY: ",[round(i, 3) for i in SY], "сумм: ", round(sum(SY), 3))
    print("SXY: ",[round(i, 3) for i in SXY], "сумм: ", round(sum(SXY), 3))
    SX = sum(SX)
    SXX = sum(SXX)
    SY = sum(SY)
    SXY = sum(SXY)

    print("итоговая система, подставить в фотомас:")
    print(f"{SXX} a  + {SX} b = {SXY}")
    print(f"{SX} a + {n} b = {SY}")
    print()
    ans = calc_system([[SXX, SX, SXY],[SX, n, SY]], 2)
    result_func = lambda x: exp(ans[1])* exp(ans[0]*x)

    str_result_func = f"{round(exp(ans[1]), 3)}e^{round(ans[0], 3)}*x"
    print("ф-ция: ",str_result_func)
    return result_func

def lna():
    nx = []
    ny = []

    #добавляем в массив только те точки, которые подходят по ОДЗ логарифма
    for i in range(N):
        if y[i] > 0:
            nx.append(x[i])
            ny.append(y[i])
    if(len(nx)!= N or len(ny)!=N):
        print("ВНИМАНИЕ! часть точек утрачена")
    n = len(nx)
    SX = [log(i) for i in nx]
    SXX = [log(i)**2 for i in nx]
    SY  = [i for i in ny]
    SXY = [log(nx[i])*ny[i] for i in range(n)]

    print("расчеты:")
    print("SX: ",[round(i, 3) for i in SX], "сумм: ", round(sum(SX), 3))
    print("SXX: ",[round(i, 3) for i in SXX], "сумм: ", round(sum(SXX), 3))
    print("SY: ",[round(i, 3) for i in SY], "сумм: ", round(sum(SY), 3))
    print("SXY: ",[round(i, 3) for i in SXY], "сумм: ", round(sum(SXY), 3))
    SX = sum(SX)
    SXX = sum(SXX)
    SY = sum(SY)
    SXY = sum(SXY)

    print("итоговая система, подставить в фотомас:")
    print(f"{SXX} a  + {SX} b = {SXY}")
    print(f"{SX} a + {n} b = {SY}")
    print()
    ans = calc_system([[SXX, SX, SXY],[SX, n, SY]], 2)
    result_func = lambda x: ans[0]* log(x) + ans[1]

    str_result_func = f"{round(ans[0], 3)} ln(x) + {round(ans[1], 3)}"
    print("ф-ция: ",str_result_func)
    return result_func

f = get_method()()

qerror(f)

