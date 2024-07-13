#THIS IS WRONG
#Python by default thinks that all user inputs are strings.
#We need to convert those userinputs which are strings to numbers.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)




#Correct version:
#num1 and num 2 are storing the number the user inputs.
#After that the result is printed
#But it only stores WHOLE numbers. No decimals.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)





#Here it can be a decimal.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)