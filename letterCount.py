while True:
	msg=input("Enter a word:\t")
	if msg=="":
		break
	msg=msg.upper()
	ans=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	b=0
	for a in range(65,91):
		ans[b]=msg.count(chr(a))
		b+=1
	for a in range(0,26):
		if ans[a] > 0:
			print("There are", ans[a], "occurrences of",chr(a+65).lower())