'''write a program to create 4 lemda functions which shall accept 2 numbers and
one arithmatic operator . as per arithmatic operator related lembda functions shall be involved'''

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Division by zero not allowed"


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = sub(num1, num2)
elif operator == "*":
    result = mul(num1, num2)
elif operator == "/":
    result = div(num1, num2)
else:
    result = "Invalid operator"

print("Result:", result)
