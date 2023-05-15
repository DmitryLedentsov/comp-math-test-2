from math import *
data = \
'''
0,1 0,2 0,3 0,4 0,5
1,25 2,38 3,79 5,44 7,14
'''
x0 = 0.28
#выбрать нужный после lambda

#x = "1.1 2.3 3.7 4.5 5.4 6.8 7.5"
#y = "2.73 5.12 7.74 8.91 10.59 12.75 13.43"
data = data.replace(",",'.')
data = data.splitlines()
X = data[1]
Y = data[2]
X = [float(i) for i in X.split(" ")]
Y = [float(i) for i in Y.split(" ")]

N = len(X)
def p_cal(p, n): 
  temp = p
  for i in range(1, n):
    if(i % 2 == 1):
      temp *= (p - i)
    else:
      temp *= (p + i)
  return temp



for i in range(N):
    Y[i][0] = X[i] ** 5

for i in range(1, N):
  for j in range(N - i):
    Y[j][i] = round((Y[j + 1][i - 1] - Y[j][i - 1]), 4)

value = float(input('Enter х: '))
sum = Y[int(N/2)][0]
p = (value - X[int(N/2)]) / (X[1] - X[0])

for i in range(1,N): 
  sum += (p_cal(p, i) * Y[int((N-i)/2)][i]) / factorial(i)

print("\nValue at", value, "is", round(sum, 4))