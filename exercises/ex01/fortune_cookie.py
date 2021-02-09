"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400756"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = randint(1, 4)

if fortune == 1:
    print("An unlit candle frightens no monkeys")
else:
    if fortune == 2:
        print("Today you will surpass all others")
    else:
        if fortune == 3:
            print("I have a dream... time to go to bed!")
        else:
            print("Those who do not seek do not find")


print("Now, go spread positive vibes!")
