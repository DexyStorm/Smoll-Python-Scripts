#How to create a function:
#def is for functions
#after "def" you type the NAME of the function. The name can be whatever you want.
#Everything that is INDENTED (=Eingerückt) will appear in this function.
#This function is named say_hi (ALWAYS LOWERCASE NAMING)
#and this function will print "Hello User".
def say_hi():
    print("Hello User")





#After you created a funtion, you have to CALL it
say_hi()











#Whenever I call the "say_hi" function, Python has to give me a name.
def say_hi(name, age):
    print("Hello " + name + ", you are " + age + " years old.")

say_hi("Mike", "35")
say_hi("Steve", "70")