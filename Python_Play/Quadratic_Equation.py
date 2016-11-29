#Write a program that asks the user to enter values for  aa ,  bb ,  cc , then prints the solutions of the quadratic equation they define, if they exist. 
#If they do not exist, it should output an appropriate message.

import math
input_a=input("Enter value for a: ")
input_b=input("Enter value for b: ")
input_c=input("Enter value for c: ")
d=float(input_b)**2-4*float(input_a)*float(input_c)
if d<0:
    print("This equation has no real solution.")
elif d==0:
    x=(-float(input_b)+math.sqrt(d))/2* float(input_a)
    print("This equation has one real solution: ", x)
else:
    x1=(-float(input_b)+math.sqrt(d))/2* float(input_a)
    x2=(-float(input_b)-math.sqrt(d))/2* float(input_a)
    print("This equation has two real solutions: ", x1, "and", x2)
