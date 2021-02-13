"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    # TODO 2: Print the result of calling your fortune_cookie function.
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    """A fortune cookie"""
    fortune: int = randint(1,4)

    if fortune == 1:
        return("An unlit candle frightens no monkeys")
    else:
        if fortune == 2:
            return("Today you will surpass all others")
        else:
            if fortune == 3:
                return("I have a dream... time to go to bed!")
            else:
                return("Those who do not seek do not find")



# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
