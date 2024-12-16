observed = int(input("Observed speed of the car: "))
limit = int(input("The speed limit: "))
while observed < 0 or limit < 0:
    print("Please enter valid numbers")
    observed = int(input("Observed speed of the car: "))
    limit = int(input("The speed limit: "))

fine = 0
if observed > limit:
    fine = 80 + 15 * (observed - limit)
elif observed > 90:
    fine +=200
else:
    fine = 0

if fine == 0:
    print("No fine is charged")
else:
    print("The fine is $"+str(fine))
