
#Write a program that produces the following output:
#000000001
#000000022
#000000333
#000004444
#000055555
#000666666
#007777777
#088888888
#999999999

for i in range(1,10):
	sum=0
	while sum<9-i:
		print("0", end="")
		sum += 1
	while sum<9:
		print(i, end="")
		sum += 1
	print()
