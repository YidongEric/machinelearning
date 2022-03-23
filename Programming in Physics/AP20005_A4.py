import math as m


def Factorial(n):
    if n == 0:
        return 1

    return n * Factorial(n-1)


def app_sin(x):
    OddNumber = 1
    totalNum = x
    i = (x**OddNumber)/Factorial(OddNumber)
    while i > 10**(-12):
        OddNumber += 2
        totalNum -= (x**OddNumber)/(Factorial(OddNumber))
        i = (x**OddNumber)/Factorial(OddNumber)
        if i > 10**(-12):
            OddNumber += 2
            totalNum += (x**OddNumber)/(Factorial(OddNumber))
            i = (x**OddNumber)/Factorial(OddNumber)
        else:
            return totalNum
    return


theta = (m.pi)/4
print(app_sin(theta))
print(m.sin(theta))
# difference_esti = abs(sin(theta)-m.sin(theta))
# print("the estimated value is:", sin(theta))
# print("the difference between them is:", difference_esti)

X = [0, 1, 0, 1, 2]
Y = [0, 0, 1, 1, 1]


def sum(x, y):
    S = 0
    for i in range(5):
        for j in range(4-i):
            dis1 = (x[i] - x[4-j])**2
            dis2 = (y[i] - y[4-j])**2
            S += (dis1 + dis2)**(-1)
    return S


print("the sum is:", sum(X, Y))
