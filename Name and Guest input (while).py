name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
while numOfGuests <= 0:
       print("You need guests")
       numOfGuests = int(input())
print('Be sure to have enough room for all your guests.')


input()

#if numOfGuests <= 0:
#       print("You need guests")
#else:
#    print('Be sure to have enough room for all your guests.')
#print('Done')
