is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")










is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are either not male or not tall or both(=a small female")










is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and (is_tall):
    print("You are not a male and you are tall")
else:
    print("You are not a male and not tall")