name=input("Please enter your name:\t\t")
sal=int(input("Please enter your Salary:\t"))
if sal<2000:
	tax=sal*15/100
elif sal<4000:
	tax=sal*22/100
elif sal<10000:
	tax=sal*40/100
else: 
	tax=0
netsal=sal-tax
print("\n\n\n")
print("Summary".center(40,"-"))
print("Name:\t{0}\nSalary:\t{1}\nNet:\t{2:.2f}".format(name,sal,netsal))
print("".center(40,"-"))