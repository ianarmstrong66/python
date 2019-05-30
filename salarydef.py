def Tax(Salary):
	if Salary > 1500:
		T=Salary*21/100
	else:
		T=Salary*15/100
	return T

def Addition(A,B):
	Result=A+B
	print("\nThe result is ",Result,"\n\n")

def WordCount(message):
	word=1
	i=0
	while i < len(message):
		if message[i]==" ":
			word+=1
		i+=1
	return word

Salary1 = int(input("Enter your Salary:\t"))
print("Your Tax\t",Tax(Salary1))
print("Net Earnings\t",(Salary1-Tax(Salary1)))

a=int(input("\n\nEnter 1st number to add:\t"))
b=int(input("Enter 2nd number to add:\t"))
Addition(a,b)
msg=input("\n\nEnter a sentence to tell you how may words are in it: ")
print("word count:\t",WordCount(msg))