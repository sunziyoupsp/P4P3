quantity = int(input("How many items: "))
if quantity > 100:
    sale = 35
elif quantity >= 50:
    sale = 25
elif quantity >= 20:
    sale = 15
elif quantity >= 10:
    sale = 5
else:
    sale = 0

principal = quantity*100
discount = sale / 100 * principal
total = principal - discount

print("Total amount before the discounts is",quantity,"* 100 = $"+str(principal))
print("The discount amount would be",sale,"/ 100 *",principal," = $"+str(discount))
print("The final amount will be",principal,"–",discount,"= $"+str(total))