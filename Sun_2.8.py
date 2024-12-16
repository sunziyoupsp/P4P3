M = float(input("Enter the amount of water in kilograms: "))
it = float(input("Enter the initial temperature: "))
ft = float(input("Enter the final temperature: "))

result = M * (ft - it) *4184

print("The energy needed is " + str(result))
