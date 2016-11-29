#Write a program that asks a user to enter a sequence of 0s and 1s. 
#Following that, it will identify the longest run of 0s or 1s of the sequence and will print an appropriate message. 
#Examples:
#
#Enter binary sequence: 1111000
#Longest run was ones with length: 4
#
#Enter binary sequence: 1010100000
#Longest run was zeros with length: 5

seq=input("Enter binary sequence: ")
num=[int(x) for x in seq]
sum1=0
sum2=0
zeros=[]
ones=[]
for i in range(len(num)):
    if num[i]==0:
        sum1+=1
        zeros.append(sum1)
    else:
        sum1=0
z=max(zeros)

for i in range(len(num)):
    if num[i]==1:
        sum2+=1
        ones.append(sum2)
    else:
        sum2=0
o=max(ones)

if z>o:
    print("Longest run was zeros with length:", z)
elif o>z:
    print("Longest run was ones with length:", o)
else:
    print("Equal longest run of ones and zeros with length:", z)
    

