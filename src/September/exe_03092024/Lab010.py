class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return a + b

    def sub(self):
        return a - b

    def mul(self):
        return a * b

    def div(self):
        return a / b


a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

cal = Calculator(a , b)
sum1 = cal.sum()
print(sum1)
sub1 = cal.sub()
print(sub1)
mul1 = cal.mul()
print(mul1)
div1 = cal.div()
print(div1)

