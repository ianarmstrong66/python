def numNameTeens(char1):
	switcher={
		48:"Ten",
		49:"Eleven",
		50:"Twelve",
		51:"Thirteen",
		52:"Fourteen",
		53:"Fifteen",
		54:"Sixteen",
		55:"Seventeen",
		56:"Eighteen",
		57:"Nineteen"
		}
	return switcher.get(char1,'')

def numNameTens(char1):
	switcher={
		48:"",
		49:"",
		50:"Twenty",
		51:"Thirty",
		52:"Fourty",
		53:"Fifty",
		54:"Sixty",
		55:"Seventy",
		56:"Eighty",
		57:"Ninety"
		}
	return switcher.get(char1,'')

def numName(char1):
	switcher={
		48:"",
		49:"One",
		50:"Two",
		51:"Three",
		52:"Four",
		53:"Five",
		54:"Six",
		55:"Seven",
		56:"Eight",
		57:"Nine"
		}
	return switcher.get(char1,'')

def convertMyNum(num1):
	word=str(num1)
	t_num=""
	h_num=""
	answer=""
	if len(word) > 3:
		t_num = " Thousand "
	if len(word) > 2:
		h_num = " Hundred "
	for a in range(len(word),0,-1):
		if a==len(word):
			answer=" "+numName(ord(word[a-1]))
		elif a==(len(word)-1):
			if word[a-1] == "1":
				answer=numNameTeens(ord(word[0]))
			else:
				answer= numNameTens(ord(word[a-1])) + answer
		elif a==(len(word)-2):
			if word[a-1] == "0":
				h_num=""
			answer= numName(ord(word[a-1])) + h_num + answer
		elif a==(len(word)-3):			
			if word[a-1] == "0":
				t_num=""
			answer= numName(ord(word[a-1])) + t_num + answer
	return answer

NumA=1
while NumA >0 and NumA <10000:
	NumA = int(input("Enter any number between 1 and 9999 \n(Enter any other number to quit):\t"))
	if NumA > 0:
		print(convertMyNum(NumA))