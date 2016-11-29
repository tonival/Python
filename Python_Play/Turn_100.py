#The year you will turn 100
from datetime import datetime
now=datetime.now()
a=now.year

name=input("Enter your name: ")
age=int(input("Enter your age: "))
print ("Hi!", name, "the year you will turn 100 is",(a) + (int(100)-age),
       "and you have",(int(100)-age),"years left." )
