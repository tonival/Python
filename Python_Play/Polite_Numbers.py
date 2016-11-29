#The positive integer numbers that can be written as the sum of two or more consecutive positive integers are called polite numbers. 
#The rest are called impolite numbers.
#It can be proven that the impolite numbers are the powers of 2. 
#Write a program that asks the user for an upper limit and then prints out the polite numbers up to and including the limit.
#The numbers should be written in rows of 10 (expect possibly for the last line). 
#Examples:
#
#Enter limit: 10
#3 5 6 7 9 10
#
#Enter limit: 16
#3 5 6 7 9 10 11 12 13 14
#15
#
#Enter limit: 25
#3 5 6 7 9 10 11 12 13 14
#15 17 18 19 20 21 22 23 24 25

lim=int(input("Enter limit: "))
a=[]
b=[]
for i in range(1, lim+1):
    a.append(i)

for i in range(1, lim):
    if(2**i)<=max(a):
        b.append(2**i)
for i in range(len(b)+1):
    a.remove(2**i)

if len(a)<=10:
    for i in range(len(a)):
        print(a[i], end=" ")
else:
    for i in range(len(a)):
        if i%10 !=0:
            print(a[i], end=" ")
        else:
            print()
            print(a[i], end=" ")
