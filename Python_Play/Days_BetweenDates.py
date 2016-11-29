#To calculate the number of days between two days we can use the following algorithm. 
#Let's say that the first date is given by  y1y1 ,  m1m1 ,  d1d1  and the second date is given by  y2y2 ,  m2m2 ,  d1d1  
#( didi  are days,  mimi  are months,  yiyi  are years).
#c1=365y1+y1/4−y1/100+y1/400+[(306m1+5)/10]+(d1−1)c1=365y1+y1/4−[y1/100]+[y1/400]+[(306m1+5)/10]+(d1−1). 
#In essence, c1c1 is the numbers of days passed since 1/1/1 until the first date.
#c2=365y2+y2/4−y2/100+y2/400+[(306m2+5)/10]+(d2−1)c2=365y2+y2/4−[y2/100]+[y2/400]+[(306m2+5)/10]+(d2−1). 
#In essence, c2c2 is the number of days that have passed since 1/1/1 until the second date.
#The days that have elapsed between the two days is c2−c1c2−c1 .
#Write a program that asks the user to enter two dates in the form dd/mm/yyyy and will then display the number of days that have elapsed between the two days. 
#Be careful, the result must not be negative.

twodates=input('Enter 2 dates, separated with /: ')
b=twodates.split()
a=b[0].split('/')
a2=b[1].split('/')
d1=int(a[0])
m1=int(a[1])
y1=int(a[2])
d2=int(a2[0])
m2=int(a2[1])
y2=int(a2[2])
c1=365*y1+y1/4-y1/100+y1/400+((306*m1+5)/10)+(d1-1)
c2=365*y2+y2/4-y2/100+y2/400+((306*m2+5)/10)+(d2-1)
c=c2-c1
print(abs(int(c)), "days.")
