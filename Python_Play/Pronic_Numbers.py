#The pronic numbers are those that are the product of two consecutive integers, so that they have the form n(n+1).
#Write a program that asks the user the number of pronic numbers to output, then goes on and prints them.
#Output:
#Enter number of pronic numbers: 10
#2 6 12 20 30 42 56 72 90 110

num=int(input("Enter the number of pronic numbers: "))
i=1
while i<=num:
    sum=i*(i+1)
    print(int(sum), end=" ")
    i += 1
