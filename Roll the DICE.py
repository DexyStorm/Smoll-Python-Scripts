import random
import sys



while True:
    a = input("Would you like to roll the dice?")
    if a == "yes":
        print(random.randint(1, 6))
    elif a != "yes":
        print("ok then, if you want to close the script, type 'exit' ")
        b = input()
        if b == "exit":
            sys.exit()
        elif b !="exit":
            print("What?")
