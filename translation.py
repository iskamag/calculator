translate_letter = input("enter a letter")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + translate_letter.upper()
            else:
                translation = translation + translate_letter
        else:
            translation = translation + letter
    return translation


print(translate(input("enter a phrase!\n")))
