def find_max_num(num1, num2):



    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")


num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
print(find_max_num(num1, num2))