"""EX03 - avoid_fifth function."""

__author__: str = "730400756"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello thEre"))

def avoid_fifth(a: str) -> str:
    """Get rid of all es in a given string."""
    i: int = 0
    empty: str = ""
    while i < len(a):
        if a[i] == 'e' or a[i] == 'E':
            empty = empty + a[i]
        else:
            i += 1
    return a 

if __name__ == "__main__":
    main()
print(avoid_fifth("hello thEre"))