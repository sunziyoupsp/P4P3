list = []
total = 0.0
for i in range(12):
    num = float(input("Enter the total rainfall for a month: "))
    list.append(num)
    total += num

print("The total rainfall for the year is",total)
print("The average monthly rainfall is", round(total/12,2))
print("The highest rainfall is",max(list))
print("The lowest rainfall is",min(list))
