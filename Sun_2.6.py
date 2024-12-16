num = int(input("Enter a number between 0 and 1000: "))
    
n1 = num //100
n2 = (num - n1*100) // 10
n3 = (num %100) % 10
total = n1 + n2 + n3

print("The sum of the digits is "+ str(total))
