# 没写完呢！！！
import math as m
n = 0
ri = 1
ρ = 7.85
M = 0  # set the initial value
while n < 100:
    M += 4/3 * m.pi*(ri)**3 * ρ  # the mass = V * ρ
    print(f'The {n+1} output of total Mass is:', M, 'g')
    ri *= 1.02  # give new value of ri as demanded in the question
    n += 1

# 没写完呢！！！
h0 = 10**(-1)
n = 0
x = 1
x1 = 1
fx = x**2  # set initial value
while n < 20:
    x2 = x1 + h0
    fx2 = x2 ** 2
    gx = (fx2 - fx) / h0
    print(f'The {n+1} output of g(x) is:', gx)
    h0 /= 10
    n += 1
