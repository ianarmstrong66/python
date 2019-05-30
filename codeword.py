msg=input("Enter your string here (include all case, numbers and symbols:\t")
word=""
for a in range(0,len(msg)):
	if ord(msg[a]) >=65 and ord(msg[a]) <=90:
		word+=chr(ord(msg[a])+32)
	elif ord(msg[a]) >=97 and ord(msg[a]) <=122:
		word+=chr(ord(msg[a])-32)
	elif ord(msg[a]) >=48 and ord(msg[a]) <=57:
		b=int(msg[a])*2
		word+=str(b)
	else:
		word+=msg[a]
print("\n\nDecoded to:\t",word)