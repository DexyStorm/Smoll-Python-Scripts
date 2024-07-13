open("employees.txt", "r")
#Open the file in "read-only" mode.
open("employees.txt", "w")
#Open the file in "write" mode.
open("employees.txt", "a")
#Open the file in "append" mode. (Append means add something to it,but
#cannot change existing text.
open("employees.txt", "r+")
#Open the file in "read-only" AND write mode... pretty useless... right?





employee_file = open("employees.txt", "r")

employee_file.close()
#After opening a file, you should close it.







employee_file = open("employees.txt", "r")

print(employee_file.readable())

employee_file.close()
#This is going to check, whether a file is readable.
#If it print "Ture" then it is.








employee_file = open("employees.txt", "w")

print(employee_file.readable())

employee_file.close()
#This will print "False" because it is "writeable".
#Makes no sense... but ok.








employee_file = open("employees.txt", "r")

print(employee_file.readline())

employee_file.close()
#This will read the first line.








employee_file = open("employees.txt", "r")

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

employee_file.close()
#This will read the first line.
#This will read the second line.
#This will read the third line.
#This will read the fourth line.










employee_file = open("employees.txt", "r")

print(employee_file.readlines())

employee_file.close()
#This will read the file as a LIST.








employee_file = open("employees.txt", "r")

print(employee_file.readlines()[1])

employee_file.close()
#This will ONLY read the first line as a LIST.