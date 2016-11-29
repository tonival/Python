#Write a program that asks the user for a 9-digit number and then prints it in three lines. Each line must contain three digits. 
#Output:
#Enter 9 digit number: 123456789
#1  4  7
# 2  5  8
#  3  6  9

digit=input('Enter 9 digit number: ')
for i in range(int(digit[0]),int(digit[-1]),3):
    print(i, end=' ')
for i in range(int(digit[1]),int(digit[-1]),3):
    if i==2:
        print('\n', i, end=' ')
    else:
        print(i, end=' ')
for i in range(int(digit[2]),10,3):
    if i==3:
        print('\n ', i, end=' ')
    else:
        print(i, end=' ')
