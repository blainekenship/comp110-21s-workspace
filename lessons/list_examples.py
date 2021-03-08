"""Some examples of list concepts"""

rolls: list[int] # Declare a variable whose type is a list of ints

rolls = [2, 3, 2, 6] #Initialize w/ list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last item in the list is {rolls[len(rolls)-1]}")
from random import randint
rolls.append(randint(1, 6))  #List's append method adds items to the end
print(rolls)

rolls.pop() #List's pop method removes the last item from the list
rolls.pop(0) #This pops a specific indexs
print(rolls)

words: list[str] = list() # Construct an empty list using the list constructor
words.append("Hello")
print(words)
