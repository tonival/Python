#A simple way to check binary data is the so-called parity bit. A byte consists of 8 bits, so that we can use the last bit to check whether 
#the previous 7 are OK. We can do that by checking that the sum of the 1 bits is an even number 
#(this is actually called even parity; we might require that the sum of 1 bits is odd, which is called odd parity).
#Write a program that asks the user for an 8-bit binary number and replies whether the parity bit checks OK.
#Output:
#Enter binary number: 01010101
#Parity check OK.
#
#Enter binary number: 11010101
#Parity check not OK.

bin=input('Enter binary number: ')
sum=0
for i in range(0, 8):
    if int(bin[i]) == 1:
        sum += 1
if sum%2==0:
    print('Parity check OK.')
else:
    print('Parity check is not OK.')
