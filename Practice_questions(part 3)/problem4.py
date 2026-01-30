# Write a program check whether the passed letter is a vowel or not

letter = input("Enter a letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("It is a vowel")
else:
    print("It is not a vowel")