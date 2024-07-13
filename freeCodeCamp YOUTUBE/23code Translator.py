def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeoiu":
            if letter.isupper():
                translation = + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase")))







def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeoiu":
            if letter.isupper():
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase")))