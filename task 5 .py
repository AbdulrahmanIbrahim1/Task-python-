#task 5: Write a Python program to test whether a passed letter is a vowel or not.
vowels = "aAeEiIoOuU"

letter = input("Enter the char : ")

if (letter.isalpha() and len(letter) == 1):
    if (letter in vowels):
        print(f"the {letter} is a vowel")
    else:
        print(f"the {letter} not vowel")
else: 
    print("Enter one char not digit number")
