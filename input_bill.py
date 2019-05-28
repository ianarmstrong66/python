prod=input("Product:\t")
price=input("Price:\t\t")
qty=input("Quantity:\t")
amount = int(qty)*float(price)
vat = (amount*20)/100
bill=amount+vat
print()
print("Your bill".center(80,"-"))
print("For {0} with amount {1} using vat at {2} comes to {3}.".format(prod,amount,vat,bill))