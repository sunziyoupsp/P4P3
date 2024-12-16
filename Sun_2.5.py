subtotal = float(input("Enter the subtotal: "))
tipRate = float(input("Enter the gratuity: "))/100

tip = round(subtotal * tipRate,2)
total = subtotal + tip

print("The gratuity is "+ str(tip) + " and the total is "+ str(total))
