num1 = float(input("Enter first number: "))
# float will convert the string into a number. (NEEDED)
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("\nInvalid operator. \nValid operators are: +, -, /, *")

# Explanation not really needed...
# User inputs one Number then an operator (=op) and then one more number.
# If the operator is not  "+, -, /, *" then it will print
# "Invalid operator. Valid operators are: +, -, /, *"