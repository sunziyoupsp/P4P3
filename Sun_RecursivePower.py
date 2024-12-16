def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

result = power(2, 5)  # computes 2 to the power of 5
print(result)  # prints 32
