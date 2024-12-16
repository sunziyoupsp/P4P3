def isSorted(lst):
    for i in range(len(lst)-1):
        if lst[i+1] < lst[i]:
            return False
    return True

user_input = input("Enter list: ").split()
lst = []
for i in range(len(user_input)):
    lst.append(int(user_input[i]))

if (isSorted(lst)):
    print("The list already sorted")
else:
    print("The list is not sorted")