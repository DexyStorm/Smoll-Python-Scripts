import random
import sys


a = random.randint(0, 10)
#print(a)     if you want to cheat, remove the "#" and this line
while True:
    b = input("Guess the Number! (It's a number from 0 to 10): ")
    if int(a) == int(b):
        print("Ayyy, you guessed it correct. Congratulations.")
        sys.exit()
    elif int(a) > int(b):
        print("Your number is too low, guess a bigger number!")
    elif int(b) > int(a):
        print("Your number is too high, guess a smaller number!")
