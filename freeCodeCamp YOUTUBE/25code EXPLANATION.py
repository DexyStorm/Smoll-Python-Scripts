#If you do not enter an actual number like 0 or 6 or 453534 or 2344 then it
#will print out "Invalid Input, enter a number."
#Would have probably been useful when I made the calculator.


try:
    number = int(input("Enter a number "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input, enter a number.")