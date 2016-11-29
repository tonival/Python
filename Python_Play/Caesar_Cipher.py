#The Caesar cipher works by substituting each character in a message with a character that occurs x places later on the alphabet, 
#wrapping around from the beginning, if neeeded. So, if x=3x=3  then "ABIGΖΟΟ" will become "DELJCRR".
#Write a program that will ask for the number of positions to shift each character and a phrase; 
#then it will output the phrase encrypted with the Caesar cipher. 

key = int(input('Enter shift: '))
text = input('Enter phrase(Use only UPPERCASE): ')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cip = ''
for c in text:
    if c in alphabet:
        cip += alphabet[(alphabet.index(c)+key)%(len(alphabet))]
print('Your encrypted massage is: ', cip)
