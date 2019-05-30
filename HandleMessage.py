def FindAndReplace(msg,find_val,replace_val):	
	# word = msg.replace(find_val,replace_val)
	words = msg.split(" ")
	word = ""
	for a in words:
		if a==find_val:
			place = words.index(a)
			words.remove(a)
			words.insert(place,replace_val)
	for a in words:
		word+=a+" "
	return word

def RemoveDuplicates(msg):
	words = msg.split(" ")
	word = ""
	for a in words:
		counter = 0
		for b in words:
			if a == b:
				counter+=1
			if counter > 1:
				for d in range(0,counter):
					words.remove(b)

	for a in words:
		word+=a+" "

	return word

def ReverseWord(msg):
	word=""
	for a in range(len(msg),0,-1):
		word+=msg[a-1]
	return word

try:
	msg1=input("\n\nEnter some text\n")
except NameError:
	print("Invalid entry, try again")

while True:

	resp=input("\nWhat would you like to do\n\n1 - Find and Replace a word from your text\n2 - Remove duplicate words\n3 - Reverse the test\nAnything else - Exit\n\n")

	if resp=="1":
		fval=input("Word to replace:\t")
		rval=input("Word to replace with:\t")
		print("\nYour string now reads as: ",FindAndReplace(msg1,fval,rval),"\n")
	elif resp=="2":
		print("\nNow we've removed all duplicates: ",RemoveDuplicates(msg1),"\n")
	elif resp=="3":
		print("\nThe reverse of your message is: ",ReverseWord(msg1),"\n")
	else:
		break