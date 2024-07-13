#If you do \n in a print, Then there will be a paragraph
print("Dexy\nStorm")




#If you do a \n BEFORE a special character F.e. " or ( it will actually print it.
print("Dexy\"Storm\"")




#You can print the whole print in lowercase.
my_name = "DexyStorm"
print(my_name.lower())




#You can print the whole print in uppercase
my_name = "DexyStorm"
print(my_name.upper())




#You can check whether the whole print is lowercase. If the whole print is lowercase, then you will get a True in the console.
#But here it is not. D and S are uppercase.
my_name = "DexyStorm"
print(my_name.islower())



#Makes the whole print lowercase then checks whether it is lowercase.
#But of course it is going to be lowercase. Because we made it lowercase, before we checked whether it is lowercase. by adding .lower()
my_name = "DexyStorm"
print(my_name.lower().islower())



#By adding (len before the actual thing you can check how many characters your print has.
#DexyStorm has 9 characters.
#It will not start counting from 0, but from 1. Like a normal human being.
my_name = "DexyStorm"
print(len(my_name))



#You can get a specific the index of the character you want to grab by putting the x-th number in [] brackets
#Here we will get the 1th character, which is D
my_name = "DexyStorm"
print(my_name[0])

#Here we will get the 2th character which is e
my_name = "DexyStorm"
print(my_name[1])



#If you want to find a specific character, here:o, then you can add .index("o") at the end of it.
#But remember, you have to start to count from 0
#That means D=0 e=1 x=2 y=3 S=4 t=5 o=6 r=7 m=8
my_name = "DexyStorm"
print(my_name.index("o"))

#You can also use whole words, or parts of a word.
#But again, it starts to count from 0.
my_name = "DexyStorm"
print(my_name.index("xyS"))



#You can replace words/letters of a word with a different one.
#Here: DexyStorm -> JeffStorm
my_name = "DexyStorm"
print(my_name.replace("Dexy", "Jeff"))