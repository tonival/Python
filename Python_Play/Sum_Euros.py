#Write a program that asks the user to provide different numbers of banknotes and coins, from €50 to €1. Then output the total sum in euros.

fifty=int(input("Enter number of 50 euro banknotes: "))
twenty=int(input("Enter number of 20 euro banknotes: "))
ten=int(input("Enter number of 10 euro banknotes: "))
five=int(input("Enter number of 5 euro banknotes: "))
two=int(input("Enter number of 2 euro coins: "))
one=int(input("Enter number of 1 euro coins: "))
sum=fifty*50+twenty*20+ten*10+five*5+two*2+one*1
print("You have", sum, "euros.")
