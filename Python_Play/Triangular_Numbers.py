#Write a program that asks the user the number of triangular numbers to produce, then prints them out.
#Output:
#Enter number of triangle numbers: 9
#1 3 6 10 15 21 28 36 45
#Enter number of triangle numbers: 15
#1 3 6 10 15 21 28 36 45 55 66 78 91 105 120

num=int(input("Enter the number of triange numbers: "))
i=1
while i<=num:
    sum=(i*(i+1))/2
    print(int(sum), end=" ")
    i += 1
