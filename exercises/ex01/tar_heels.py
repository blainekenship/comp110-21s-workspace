"""An exercise in remainders and boolean logic."""

__author__ = "730400756"

# Begin your solution here...

val: int = int(input( "Pick a number, any number: "))

if val % 2 == 0 and val % 7 == 0:
    print("TAR HEELS")
else:
    if val % 2 == 0:
        print("TAR")
    else:
        if val % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")
            
