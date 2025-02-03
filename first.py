print("Name: Justin Fernando")
print("Student No: 202420033")
print("Year: 2 - BSIT | transferee")

vowels = "AEIOUaeiou"
consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
spaces = ""

vowelCount = 0
consonantsCount = 0
spaces = 0
otherChar = 0

input_char = input("Enter text: ")

for char in input_char:
    if char in vowels:
        vowelCount += 1
    elif char in consonants:    
        consonantsCount += 1
    elif char == " ":
        spaces += 1
    else:
        otherChar += 1
   

print("Vowels: ", vowelCount)
print("Consonants: ", consonantsCount)
print("Spaces: ", spaces)
print("Other Characters: ", otherChar)
