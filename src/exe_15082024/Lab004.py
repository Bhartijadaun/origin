def power(num1, num2):
    # Calculate num1 raised to the power of num2
    result = num1 ** num2
    return result

# Get user input and convert to float
num1 = float(input("Enter the base number (num1): "))
num2 = float(input("Enter the exponent (num2): "))


result = power(num1, num2)

# Display the result
print(f"{num1} raised to the power of {num2} is {result}")
