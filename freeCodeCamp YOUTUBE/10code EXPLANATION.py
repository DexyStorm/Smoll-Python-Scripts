#You can extend lists by adding .extend

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)


#You can append (=add) something to your list by typing .append
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Jeff")
print(friends)


#You can insert something into your list, at a specific point.
#Here you add "Kelly" to the 2nd position.
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)



#You can remove stuff from your list
#Here: Remove Jim
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)



#You can clear your list
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)



#You can remove the last thing from your list
#By writing .pop
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)



#You can check which number which thing has
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index("Oscar"))




#You can check how many thimes the same thing in your list appears.
friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Oscar", "Oscar", "Oscar", "Toby"]

print(friends.count("Oscar"))



#You can sort your list by alphaet.
#Also works with numbers.
friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends.sort()
print(friends)



#You can reverse the list.
#Also works with numbers.
friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends.reverse()
print(friends)



#You can copy lists.
#Here you coppied the list "friends" and create another list which is names "friends2"
#Then you coppied everything from "friends" to "friends2"
friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)