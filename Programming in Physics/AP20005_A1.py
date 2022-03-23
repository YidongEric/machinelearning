# 1.Remarking includes putting Human Readable Descriptions within PC programs itemizing what the Code is doing.
# Appropriate utilization of remarking can make code support a lot simpler, as well as aiding make finding bugs quicker.
# Further, remarking is vital while composing capacities that others will utilize.

# r = float(input("Input the radius of the circle : "))
# π = 3.1416
# print("The area of the circle with radius " + str(r) + " is: " + str(π * r**2))

# R1 = float(input("Resistor 1 : "))
# R2 = float(input("Resistor 2 : "))
# R3 = float(input("Resistor 3 : "))
# R4 = 1/R1 + 1/R2 + 1/R3
# R = 1/R4
# print("The overall resistance R is: " + str(R) + 'Ω')

h0 = float(input("h0 is : "))
t = float(input("t is : "))
g = 9.8
y = h0 - 1/2 * g * t**2
if y > 0:
    print("Height y is: " + str(y) + 'm')
else:
    print("Height y is: 0 m")
