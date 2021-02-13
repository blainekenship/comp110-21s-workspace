"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(a: int) -> str:
    """A pro-Carolina program"""
    if a % 2 == 0 and a % 7 == 0:
        return("TAR HEELS")
    else:
        if a % 2 == 0:
            return("TAR")
        else:
            if a % 7 == 0:
                return("HEELS")
            else:
                return("CAROLINA")

if __name__ == "__main__":
    main()
