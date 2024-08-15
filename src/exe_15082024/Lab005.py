def perform_operations(num1, num2):

    res1 = num1 + num2
    res2 = num1 - num2
    res3 = num1 * num2
    # Handle division by zero
    if num2 != 0:
        res4 = num1 / num2
    else:
        res4 = "undefined (division by zero)"
    return res1, res2, res3, res4

# Get user input and convert to float
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))


res = perform_operations(num1, num2)


print(f"Sum: {res[0]}")
print(f"Difference: {res[1]}")
print(f"Product: {res[2]}")
print(f"Quotient: {res[3]}")
