import datetime
first=int(input("Enter Starting number:\t"))
occar=int(input("How many iterations:\t"))
timesBy=int(input("Enter multiple\t\t"))
jumpedUp = first+occar
ts = datetime.datetime.utcnow()
while first<=(jumpedUp):
	print (first,"x",timesBy,"=\t",(first * timesBy))
	first=first+1

te = datetime.datetime.utcnow()
print ("Started at \t",ts,"\nFinished at \t",te)
td = te - ts
print(td)