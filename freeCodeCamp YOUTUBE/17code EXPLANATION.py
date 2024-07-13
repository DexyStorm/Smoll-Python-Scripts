monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversion["Feb"])
#Writes February
print(monthConversion.get("Dec"))
#Writes December
print(monthConversion.get("Luv", "Not a valid Key"))
#If there was a Month, it would write the whole Month name that starts with "Luv"
#But there isn't, that's why it will print "Not a valid Key"