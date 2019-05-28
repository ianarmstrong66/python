msg=input("Enter your message please:\t")
query=input("what character are you looking for?\t")
a=len(msg)
aChars=[]
found=False
for b in range(0,a):
	if msg[b]==query:
		found=True
		aChars.append(b+1)
if found:
	print("We found ", query," in your message ","\"", msg,"\"", " at positions ")
	for b in aChars:
		print(b)
else:
	print("We still haven't found, what you're looking for") 