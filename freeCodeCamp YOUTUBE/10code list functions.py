lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Jeff")
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Toby"]
print(friends.index("Oscar"))


friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Oscar", "Oscar", "Oscar", "Toby"]
print(friends.count("Oscar"))


friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends.sort()
print(friends)


friends = ["David", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)