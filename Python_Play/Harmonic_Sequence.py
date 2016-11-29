#Write a program that calculates the first five terms of the harmonic sequence.
#Output:
#1
#1.5
#1.8333333333333333
#2.083333333333333
#2.283333333333333

sum=0
for i in range(1,6):
        sum += 1/i
        print(sum)
