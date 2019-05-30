Alpha=input("Enter a character and we'll change the case:\t")
a=0
if ord(Alpha)>=65 and ord(Alpha) <=90:
	a=32
elif ord(Alpha)>=97 and ord(Alpha) <=122:
	a=-32
print(chr(ord(Alpha)+a))