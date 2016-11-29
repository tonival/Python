#Sequence: 1×2+3×4+5×6+7
#Write a program that asks a user to enter a sequence of digits and then calculates the value of the sequence, as defined above. 
#Output:
#
#Enter number sequence: 123456
#44
#
#Enter number sequence: 1234567
#51
#
#Enter number sequence: 1230123
#7

seq=input("Enter a sequence of numbers: ")
num=[int(x) for x in seq]
o=len(num)
sum=0
if o%2!=0:
    for i in range(1,o,2):
        sum+=num[i-1]*num[i]
    t1=sum+num[o-1]
else:
    for i in range(1,o,2):
        sum+=num[i-1]*num[i]
    t2=sum
print(t2)
