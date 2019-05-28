msg=input("Enter your Message: ")
qry=input("What word are you looking for? ")
wl=len(qry)
countWord = 0
for a in range(0,len(msg)):
	if msg[a] == qry[0]:
		if msg[a:a+wl] == qry:
			countWord = countWord + 1
			a=a+wl-1
print("The number of occurances of the word ", qry, " is ", countWord) 