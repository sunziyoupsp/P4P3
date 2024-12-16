import math
n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of sides: "))

area = (n * s * s) /(4 * math.tan(math.pi/n))

print("The area of the polygon is " + str(area))
