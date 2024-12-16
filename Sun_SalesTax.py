import math
LName = str(input("Please enter your Last Name: "))
FName = str(input("Please enter your First Name: "))
purchase = int(input("Please enter the amount of purchase:"))
sRate = int(input("Please enter the state sales tax in percentage: "))
cRate = int(input("Please enter the county sales tax in percentage: "))

sTax = purchase * (sRate/100)
cTax = purchase * (cRate/100)

print()
print("The amount of purchase is $"+ str(purchase))
print("The state sales tax is $" + str(math.trunc(sTax)))
print("The county sales tax is $" + str(cTax))
print("The total sales tax is $" + str((sTax + cTax)))
print("The total sale is $" + str((purchase + sTax + cTax)))
print()
print("Thank you "+FName + " " + LName + " for your business!")

