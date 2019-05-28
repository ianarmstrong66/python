cash=int(input("How much do you need:\t"))
#hundred = 0
#fifty = 0
#twenty = 0
#ten = 0
#five = 0
#two = 0
#one = 0
#while cash - 100 >= 0:
#	cash = cash - 100
#	hundred = hundred + 1
#while cash - 50 >= 0:
#	fifty = fifty + 1
#	cash = cash - 50
#while cash -20 >= 0:
#	twenty = twenty + 1
#	cash = cash - 20
#while cash - 10 >= 0:
#	ten = ten + 1
#	cash = cash - 10
#while cash -5 >= 0:
#	five = five + 1
#	cash = cash - 5
#while cash - 2 >= 0:
#	two = two + 1
#	cash = cash - 2
#while cash - 1 >= 0:
#	one = one + 1
#	cash = cash - 1*/
hundred = int(cash/100)
if hundred > 0:
	cash = cash%100
	print("{0} hundred(s)".format(hundred))
fifty = int(cash/50)
if fifty > 0:
	cash = cash%50
	print("{0} fifty(s)".format(fifty))
twenty = int(cash/20)
if twenty > 0:
	cash = cash%20
	print("{0} twenty(s)".format(twenty))
ten = int(cash/10)
if ten > 0:
	cash = cash%10
	print("{0} ten(s)".format(ten))
five = int(cash/5)
if five > 0:
	cash = cash%5
	print("{0} five(s)".format(five))
two = int(cash/2)
if two > 0:
	cash = cash%2
	print("{0} two(s)".format(two))
one = cash
if one > 0:
	print("{0} one(s)".format(one))