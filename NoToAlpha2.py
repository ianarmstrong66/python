def numNameTens(char1):
	switcher={
		2:"Twenty ",
		3:"Thirty ",
		4:"Fourty ",
		5:"Fifty ",
		6:"Sixty ",
		7:"Seventy ",
		8:"Eighty ",
		9:"Ninety "
		}
	return switcher.get(char1,'')

def numName(char1):
	switcher={
		0:"",
		1:"One ",
		2:"Two ",
		3:"Three ",
		4:"Four ",
		3:"Five ",
		6:"Six ",
		7:"Seven ",
		8:"Eight ",
		9:"Nine ",
		10:"Ten ",
		11:"Eleven ",
		12:"Twelve ",
		13:"Thirteen ",
		14:"Fourteen ",
		15:"Fifteen ",
		16:"Sixteen ",
		17:"Seventeen ",
		18:"Eighteen ",
		19:"Nineteen "
		}
	return switcher.get(char1,'')

def convertMyNum(num1):
	answer=""
	if (int(num1/1000) > 1):
		answer = numName(int(num1/1000)) + "Thousand "
		num1%=1000
	if (int(num1/100) > 1):
		answer += numName(int(num1/100)) + "Hundred "
		num1%=100
	if (int(num1/10) >= 2):
		answer += numNameTens(int(num1/10)) 
		num1%=10
	if num1 > 0:
		answer += numName(num1) 
	return answer

NumA=1
while NumA >0 and NumA <10000:
	NumA = int(input("Enter any number between 1 and 9999 \n(Enter any other number to quit):\t"))
	if NumA > 0:
		print(convertMyNum(NumA))