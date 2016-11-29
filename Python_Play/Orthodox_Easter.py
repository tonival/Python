#To calculate Orthodox Easter Sunday for any year between 1900 and 2099, we can use the following algorithm. Suppose that  yy  is the year.
#a=ymod4a=ymod4 
#b=ymod7b=ymod7 
#c=ymod19c=ymod19 
#d=(19c+15)mod30d=(19c+15)mod30 
#e=(2a+4b−d+34)mod7e=(2a+4b−d+34)mod7 
#month=[((d+e+114)/31)].
#day=((d+e+114)mod31)+1day=((d+e+114)mod31)+1 
#The result is the day and the month in the Julian calendar. To convert it to the Gregorian calendar, which we actually use, we have to add 13 days. 
#Be careful, this may change the month.
#
#Write a program that asks the user for a year and then displays the month and the day of Orthodox Easter in the Gregorian calendar. 
#Output:
#Enter year: 2011
#Day: 24 Month: 4

import math
y=int(input("Enter year: "))
a=y%4
b=y%7
c=y%19
d=(19*c+15)%30
e=(2*a+4*b-d+34)%7
month=math.floor(((d+e+114)/31))
day=((d+e+114)%31)+14
print("Day: ", day, "Month: ", month)
    
    
