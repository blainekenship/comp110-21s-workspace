"""For...in loop practice"""

#Iterate through each item in a list
letters: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

#Print each letter in the letters list
print("Each letter")
for letter in letters:
    print(letter)


#Print every other letter in letter list
print("Every other letter... ")
for i in range(0, len(letters), 2):
    print(letters[i])


#Use a range to iterate through each index in a sequence
for i in range(len(letters)):
    print(f"i: {i} - letters[i]: {letters[i]}")
    