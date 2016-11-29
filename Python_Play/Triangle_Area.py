#If we want to calculate the area of a triange given its sides, we can use Heron's formula.
#Write a program that asks the user for the three sides and calculates its area.

import math
a=int(input("Give side one of the triangle: "))
b=int(input("Give side two of the triangle: "))
c=int(input("Give side three of the triangle: "))
area=(math.sqrt(a+b+c)*(a+b+c)*(a-b+c)*(a+b-c))/4
print("The area of the triangle is", area)
