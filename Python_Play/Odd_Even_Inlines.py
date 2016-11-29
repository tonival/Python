#Write a program that asks the user for a 10-digit number and will then print it in two lines. 
#The first line will contain the numbers in the odd positions and the second line the numbers in the even positions.
#Output:
#Enter 10 digit number: 1234567890
#1 3 5 7 9
# 2 4 6 8 0

digit=input('Enter 10 digit number: ')
num=[int(x) for x in digit]
k=[]
m=[]
for i in range (0,10):
        if i % 2 == 0:
                k.append(num[i])
        else:
                m.append(num[i])
print(*k)
print('', *m)
