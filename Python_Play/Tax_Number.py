#This Tax Identification Number (TIN) consists of 9 digits. The last digit is a check digit. It is calculated as follows:
#1.We remove the check digit, so that we are left with an 8-digit number.
#2.We take the 8 digits one by one, from the right to the left. We multiply each digit by the power of 2 corresponding to its position: 
#the first from the right will be multiplied by  2121 , the second will be multiplied by  2222 , and so on.
#3.We take these powers and we sum them.
#4.We calculate the remainder of this sum by 11.
#5.We take this remainder and we calculate its remainder by 10. The result must equal the check digit.
#
#Write a program that will ask the user for TIN and will respond whether it is correct or not.
#Output:
#
#Enter Tax Identification Number: 090034337
#Tax Identification Number valid.
#Enter Tax Identification Number: 090034336
#Tax Identification Number not valid.

t=input('Enter Tax Identification Number: ')
sum=0
for i in range(1, 9):
    sum += int(t[-2+i])*2**i
a=(sum%11)%10
if a==int(t[-1]):
    print('Tax Identification Number valid.')
else:
    print('Tax Identification Number not valid.')
