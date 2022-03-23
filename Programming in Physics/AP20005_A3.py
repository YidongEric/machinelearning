import math as m
# from itertools import count
# sum1 = 0


# def sum_of_list(l):
#     total = 0
#     for val in l:
#         total = total + val
#     return total


# list = [1, 3, 7, 12, 13.5, 18, 22]  # creation of the list
# Xaverage = sum_of_list(list) / len(list)

# for i in range(len(list)):
#     sum1 += (list[i] - Xaverage) ** 2
#     σ = (sum1 / len(list)) ** 0.5

# print("The standard deviation of list is", σ)
# print("The average of list is", Xaverage)

# π = 0
# i = 0
# while i < 100000:
#     π += (4 * ((-1)**(i) / (2*i+1)))
#     i += 1
# print(π)

x = 46  # where x is in radian
i = 0
while i < 100:
    f = m.cos(x)
    x = f
    i += 1
    if i > 95:
        print(f'The {i} output is:', f)
    else:
        continue
