def split_(directionA):
	msg=input("Enter your message: ")
	word=""
	a = 1
	if (directionA ==""):
		a=0
		
	if a==0:
		i=0
		while i < len(msg):
			if msg[i] == " " or msg[i] == "," or msg[i] == "."  or msg[i] == "?":
				if word != "":
					print(word)
				word = ""
			else:
				word = word + msg[i]
				i=i+1
	else:
		i=len(msg)-1
		while i >= 0:
			if msg[i] == " "  or msg[i] == "," or msg[i] == ".":
				if word != "":
					print(word)
				word = ""
			else:
				word =  msg[i] + word
			i=i-1
	print(word)
	return
split_(0)
split_(1)