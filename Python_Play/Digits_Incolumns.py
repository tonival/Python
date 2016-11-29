#Write a program that asks the user for 9 numbers: 1 with 1 digit, 1 with 2 digits, 1 with 3 digits, 
#then again 1 with 1 digit, 1 with 2 digits, 1 with 3 digits, 
#and then again 1 with 1 digit, 1 with 2 digits, 1 with 3 digits. 
#Then the program will print them in columns, where each column will contain 1 single digit number, 1 double digit number, and 1 triple digit number.
#Output:
#Enter numbers: 1 10 100 2 20 200 3 30 300
#  1|  2|  3
# 10| 20| 30
#100|200|300

one=[]
two=[]
three=[]
allnum=[]
for i in range(3):
    n1=int(input('Enter a number with 1 digit: '))
    allnum.append(n1)
    n2=int(input('Enter a number with 2 digits: '))
    allnum.append(n2)
    n3=int(input('Enter a number with 3 digits: '))
    allnum.append(n3)
for i in range(9):
    if len(str(allnum[i]))==1:
        one.append(allnum[i])
    elif len(str(allnum[i]))==2:
        two.append(allnum[i])
    elif len(str(allnum[i]))==3:
        three.append(allnum[i])
for i in range(3):
    print(" ",one[i],end="|")
print()
for i in range(3):
    print("",two[i],end="|")
print()
for i in range(3):
    print(three[i],end="|")
print()
