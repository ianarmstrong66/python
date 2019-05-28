physics=80
chemistry=99
math=87
total=physics+chemistry+math
per=total*100/150
print("\n\nPhysics:\t{0} \nChemistry:\t{1} \nMath:\t\t{2}".format(physics,chemistry,math))
print("SUMMARY".center(40,'-'))
print("Result of your marks is {0} \nPercentage: \t{1}".format(total,per))
print("END".center(40,'-'))