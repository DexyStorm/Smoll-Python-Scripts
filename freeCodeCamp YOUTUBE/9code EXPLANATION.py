#How to store stuff in a list
#friends is the container. in friends there is "David", "Karen", "Jim", "Oscar", "Toby".
#If i want to see my 2nd friend, i type print(friends[1]) because it starts from 0.
#David is my 0th friend.

#if you want to go from the back, type print(friends[-1])
#-1 is Toby. It starts from 1 from the back.

friends = ["David", "Karen", "Jim", "Oscar", "Toby"]

print(friends[0])



#If you want to get everthing with it and after it, do a [x:]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]

print(friends[1:])




#If you want to get everthing with it to something other, do [x:y]
friends = ["David", "Karen", "Jim", "Oscar", "Toby"]

print(friends[1:3])